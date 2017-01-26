from django.conf import settings

from . import defaults

__title__ = 'fobi.contrib.plugins.form_elements.fields.' \
            'select_mptt_model_object.conf'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('get_setting',)


def get_setting(setting, override=None):
    """Get setting.

    Get a setting from
    `fobi.contrib.plugins.form_elements.fields.select_mptt_model_object` conf
    module, falling back to the default.

    If override is not None, it will be used instead of the setting.

    :param setting: String with setting name
    :param override: Value to use when no setting is available. Defaults
        to None.
    :return: Setting value.
    """
    if override is not None:
        return override
    if hasattr(
            settings,
            'FOBI_FORM_ELEMENT_SELECT_MPTT_MODEL_OBJECT_{0}'.format(setting)
    ):
        return getattr(
            settings,
            'FOBI_FORM_ELEMENT_SELECT_MPTT_MODEL_OBJECT_{0}'.format(setting)
        )
    else:
        return getattr(defaults, setting)
