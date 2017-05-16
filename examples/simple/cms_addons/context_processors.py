from fobi.contrib.apps.djangocms_integration.cms_version import (
    CMS_VERSION_GT_3_0,
    CMS_VERSION_LTE_3_0,
)


def cms_version(request):
    return {
        'CMS_VERSION_GT_3_0': CMS_VERSION_GT_3_0,
        'CMS_VERSION_LTE_3_0': CMS_VERSION_LTE_3_0,
    }
