__title__ = 'fobi.data_structures'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('SortableDict', )

import copy

import six


class SortableDict(dict):
    """
    A dictionary that keeps its keys in the order in which they're
    inserted. Very similar to (and partly based on) ``SortedDict`` of
    the ``Django``, but has several additional methods implemented,
    such as: ``insert_before_key`` and ``insert_after_key``.
    """

    def __new__(cls, *args, **kwargs):
        instance = super(SortableDict, cls).__new__(cls, *args, **kwargs)
        instance.key_order = []
        return instance

    def __init__(self, data=None):
        if data is None or isinstance(data, dict):
            data = data or []
            super(SortableDict, self).__init__(data)
            self.key_order = list(data) if data else []
        else:
            super(SortableDict, self).__init__()
            super_set = super(SortableDict, self).__setitem__
            for key, value in data:
                # Take the ordering from first key
                if key not in self:
                    self.key_order.append(key)
                # But override with last value in data (dict() does this)
                super_set(key, value)

    def __deepcopy__(self, memo):
        return self.__class__([(key, copy.deepcopy(value, memo))
                               for key, value in self.items()])

    def __copy__(self):
        # The Python's default copy implementation will alter the state
        # of self. The reason for this seems complex but is likely related to
        # subclassing dict.
        return self.copy()

    def __setitem__(self, key, value):
        if key not in self:
            self.key_order.append(key)
        super(SortableDict, self).__setitem__(key, value)

    def __delitem__(self, key):
        super(SortableDict, self).__delitem__(key)
        self.key_order.remove(key)

    def __iter__(self):
        return iter(self.key_order)

    def __reversed__(self):
        return reversed(self.key_order)

    def pop(self, k, *args):
        result = super(SortableDict, self).pop(k, *args)
        try:
            self.key_order.remove(k)
        except ValueError:
            # Key wasn't in the dictionary in the first place. No problem.
            pass
        return result

    def popitem(self):
        result = super(SortableDict, self).popitem()
        self.key_order.remove(result[0])
        return result

    def _iteritems(self):
        for key in self.key_order:
            yield key, self[key]

    def _iterkeys(self):
        for key in self.key_order:
            yield key

    def _itervalues(self):
        for key in self.key_order:
            yield self[key]

    if six.PY3:
        items = _iteritems
        keys = _iterkeys
        values = _itervalues
    else:
        iteritems = _iteritems
        iterkeys = _iterkeys
        itervalues = _itervalues

        def items(self):
            return [(k, self[k]) for k in self.key_order]

        def keys(self):
            return self.key_order[:]

        def values(self):
            return [self[k] for k in self.key_order]

    def update(self, dict_):
        for k, v in six.iteritems(dict_):
            self[k] = v

    def setdefault(self, key, default):
        if key not in self:
            self.key_order.append(key)
        return super(SortableDict, self).setdefault(key, default)

    def value_for_index(self, index):
        """Returns the value of the item at the given zero-based index."""
        # This, and insert() are deprecated because they cannot be implemented
        # using collections.OrderedDict (Python 2.7 and up), which we'll
        # eventually switch to
        return self[self.key_order[index]]

    def insert(self, index, key, value):
        """Inserts the key, value pair before the item with the given index."""
        if key in self.key_order:
            n = self.key_order.index(key)
            del self.key_order[n]
            if n < index:
                index -= 1
        self.key_order.insert(index, key)
        super(SortableDict, self).__setitem__(key, value)

    def copy(self):
        """Returns a copy of this object."""
        # This way of initializing the copy means it works for subclasses, too.
        return self.__class__(self)

    def __repr__(self):
        """
        Replaces the normal dict.__repr__ with a version that returns the keys
        in their sorted order.
        """
        return '{%s}' % ', '.join(['%r: %r' % (k, v)
                                   for k, v in six.iteritems(self)])

    def clear(self):
        super(SortableDict, self).clear()
        self.key_order = []

    # *************************************************************************
    # ************************** Additional methods ***************************
    # *************************************************************************

    def insert_before_key(self, target_key, key, value,
                          fail_silently=True,
                          offset=0):
        """
        Inserts the {``key``: ``value``} before the ``target_key``.

        :param immutable target_key:
        :param immutable key:
        :param mutable value:
        :param boolean fail_silently:
        :param int offset:
        :return bool:
        """
        if target_key in self.key_order:
            index = self.key_order.index(target_key) + offset
            self.insert(index, key, value)
            return True
        elif not fail_silently:
            raise ValueError(
                "Target key ``{0}`` does not exist.".format(target_key))
        else:
            return False

    def insert_after_key(self, target_key, key, value, fail_silently=True):
        """
        Inserts the {``key``: ``value``} after the ``target_key``.

        :param immutable target_key:
        :param immutable key:
        :param mutable value:
        :param boolean fail_silently:
        :param int offset:
        :return bool:
        """
        return self.insert_before_key(target_key=target_key,
                                      key=key,
                                      value=value,
                                      fail_silently=fail_silently,
                                      offset=1)

    def move_before_key(self, source_key, target_key,
                        fail_silently=True,
                        offset=0):
        """
        Moves the {``key``: ``value``} before the given ``source_key``.

        :param immutable source_key:
        :param immutable target_key:
        :param boolean fail_silently:
        :param int offset:
        :return bool:
        """
        if target_key in self.key_order and source_key in self.key_order:
            source_value = self.pop(source_key)
            return self.insert_before_key(target_key, source_key, source_value,
                                          fail_silently=True,
                                          offset=offset)
        elif not fail_silently:
            raise ValueError("Non existing keys: {0}, {1}.".format(source_key,
                                                                   target_key))
        else:
            return False

    def move_after_key(self, source_key, target_key, fail_silently=True):
        """
        Moves the {``key``: ``value``} after the given ``source_key``.

        :param immutable source_key:
        :param immutable target_key:
        :param boolean fail_silently:
        :return bool:
        """
        return self.move_before_key(source_key=source_key,
                                    target_key=target_key,
                                    fail_silently=fail_silently,
                                    offset=1)
