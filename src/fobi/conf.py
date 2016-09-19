from django.conf import settings

from fobi import defaults

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('get_setting',)


def get_setting(setting, override=None):
    """Get setting.

    Get a setting from `fobi` conf module, falling back to the default.

    If override is not None, it will be used instead of the setting.

    :param setting: String with setting name
    :param override: Value to use when no setting is available. Defaults to
        None.
    :return: Setting value.
    """
    if override is not None:
        return override
    if hasattr(settings, 'FOBI_{0}'.format(setting)):
        return getattr(settings, 'FOBI_{0}'.format(setting))
    else:
        return getattr(defaults, setting)
