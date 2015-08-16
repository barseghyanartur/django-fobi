__title__ = 'fobi.compat'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('AUTH_USER_MODEL', 'User',)

from django.conf import settings

from nine.user import User

# Sanity checks. Possibly rely on the dynamic username field in future.
#user = User()
#
#if not hasattr(user, 'username'):
#    from fobi.exceptions import ImproperlyConfigured
#    raise ImproperlyConfigured("Your custom user model ({0}.{1}) doesn't "
#                               "have ``username`` property, while "
#                               "``django-fobi`` relies on its' presence."
#                               "".format(user._meta.app_label,
#                                         user._meta.object_name))

AUTH_USER_MODEL = settings.AUTH_USER_MODEL
