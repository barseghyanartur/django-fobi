__title__ = 'fobi.form_utils'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'ErrorDict', 'ErrorList',
)

from django.forms import util
from django.utils.encoding import force_text

class ErrorDict(util.ErrorDict):
    """
    A better ErrorDict.
    """
    def as_text(self):
        return '\n'.join(
            [' %s\n%s' % (k, '\n'.join([' %s' % force_text(i) for i in v])) \
             for k, v in self.items()]
            )

class ErrorList(util.ErrorList):
    """
    A better ErrorList.
    """
    def as_text(self):
        if not self: return ''
        return '\n'.join([' %s' % force_text(e) for e in self])
