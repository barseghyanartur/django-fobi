from django.conf import settings

from nine.user import User

__title__ = 'fobi.compat'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'AUTH_USER_MODEL',
    'User',
)

AUTH_USER_MODEL = settings.AUTH_USER_MODEL
