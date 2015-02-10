__title__ = 'fobi.fields'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('NoneField',)

from django.forms.fields import Field

from fobi.widgets import NoneWidget

class NoneField(Field):
    """
    To be used with content elements like text or images, that need to be
    present, for instance, in between form input elements.
    """
    widget = NoneWidget

    def bound_data(self, data, initial):
        """
        Return the value that should be shown for this field on render of a
        bound form, given the submitted POST data for the field and the initial
        data, if any.

        For most fields, this will simply be data; FileFields need to handle it
        a bit differently.
        """
        return initial

    def validate(self, value):
        return True
