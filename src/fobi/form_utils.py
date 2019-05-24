from django.forms.utils import (
    ErrorDict as DjangoErrorDict,
    ErrorList as DjangoErrorList,
)
from django.utils.encoding import force_text

__title__ = 'fobi.form_utils'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'ErrorDict',
    'ErrorList',
)


class ErrorDict(DjangoErrorDict):
    """A better ErrorDict."""

    def as_text(self):
        """As text."""
        return '\n'.join(
            [' %s\n%s' % (k, '\n'.join([' %s' % force_text(i) for i in v]))
             for k, v in self.items()]
        )


class ErrorList(DjangoErrorList):
    """A better ErrorList."""

    def as_text(self):
        """As text."""
        if not self:
            return ''
        return '\n'.join([' %s' % force_text(e) for e in self])
