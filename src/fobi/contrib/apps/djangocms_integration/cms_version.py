from cms import __version__

__title__ = 'fobi.contrib.apps.djangocms_integration.cms_version'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'CMS_VERSION',
    'CMS_VERSION_LTE_3_0',
    'CMS_VERSION_GT_3_0',
)

CMS_VERSION = [int(__v) for __v in __version__.split('.')]

CMS_VERSION_LTE_3_0 = CMS_VERSION[0] <= 2 \
                      or (CMS_VERSION[0] == 3 and CMS_VERSION[1] == 0)
CMS_VERSION_GT_3_0 = not CMS_VERSION_LTE_3_0
