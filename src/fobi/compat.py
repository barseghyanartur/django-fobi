__title__ = 'fobi.compat'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('AUTH_USER_MODEL',)

from django.conf import settings

# ****************************************************************************
# **************** Safe User import for Django > 1.5, < 1.8 ******************
# ****************************************************************************
AUTH_USER_MODEL = settings.AUTH_USER_MODEL

# Note, that this may cause circular imports - thus the ``get_user_model``
# should be moved elsewhere (be used on the function/method level). For
# now leave commented and solve in future. Possible use the DjangoCMS solution
# https://github.com/divio/django-cms/blob/develop/cms/models/permissionmodels.py#L18

# Sanity checks.
#user = User()
#
#if not hasattr(user, 'username'):
#    from fobi.exceptions import ImproperlyConfigured
#    raise ImproperlyConfigured("Your custom user model ({0}.{1}) doesn't "
#                               "have ``username`` property, while "
#                               "``django-fobi`` relies on its' presence"
#                               ".".format(user._meta.app_label, user._meta.object_name))

# ****************************************************************************
# ****************************************************************************
# ****************************************************************************
