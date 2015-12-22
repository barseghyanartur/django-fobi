__title__ = 'fobi.form_utils'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'ErrorDict', 'ErrorList',
)

from nine.versions import DJANGO_GTE_1_7

if DJANGO_GTE_1_7:
    from django.forms.utils import (
        ErrorDict as DjangoErrorDict, ErrorList as DjangoErrorList
    )
else:
    from django.forms.util import (
        ErrorDict as DjangoErrorDict, ErrorList as DjangoErrorList
    )

from django.utils.encoding import force_text


class ErrorDict(DjangoErrorDict):
    """
    A better ErrorDict.
    """
    def as_text(self):
        return '\n'.join(
            [' %s\n%s' % (k, '\n'.join([' %s' % force_text(i) for i in v])) \
             for k, v in self.items()]
            )


class ErrorList(DjangoErrorList):
    """
    A better ErrorList.
    """
    def as_text(self):
        if not self: return ''
        return '\n'.join([' %s' % force_text(e) for e in self])
