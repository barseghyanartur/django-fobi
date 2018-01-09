from cms import __version__
from nine.versions import DJANGO_GTE_1_8
from .base import *

CMS_VERSION = [int(__v) for __v in __version__.split('.')]

INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS += [
    'cms',  # DjangoCMS
    'menus',
    'sekizai',
    'djangocms_admin_style',

    # Some plugins
    'filer',
    # 'cmsplugin_filer_image',
    # 'djangocms_picture',
    # 'djangocms_snippet',

    'fobi.contrib.apps.djangocms_integration',  # Fobi DjangoCMS app

    # 'djangocms_page',  # Example
]

DJANGO_CMS_CONTEXT_PROCESSORS = []
MIGRATION_MODULES = {}

if CMS_VERSION[0] <= 2 or (CMS_VERSION[0] == 3 and CMS_VERSION[1] == 0):
    INSTALLED_APPS.append('mptt')
    DJANGO_CMS_CONTEXT_PROCESSORS = [
        'cms.context_processors.media',
        'sekizai.context_processors.sekizai',
        'cms.context_processors.cms_settings',
        'nine.context_processors.versions',
        'cms_addons.context_processors.cms_version',
    ]
    MIGRATION_MODULES = {
        'cms': 'cms.migrations_django',
        'menus': 'menus.migrations_django',
    }

else:
    INSTALLED_APPS.append('treebeard')
    INSTALLED_APPS.append('cms_addons')
    DJANGO_CMS_CONTEXT_PROCESSORS = [
        'cms.context_processors.cms_settings',
        'sekizai.context_processors.sekizai',
        'cms.context_processors.cms_settings',
        'nine.context_processors.versions',
        'cms_addons.context_processors.cms_version',
    ]
    MIGRATION_MODULES = {
        'cms': 'cms.migrations',
        'menus': 'menus.migrations',
    }

try:
    INSTALLED_APPS.remove('admin_tools.dashboard') \
        if 'admin_tools.dashboard' in INSTALLED_APPS else None
except Exception as err:
    pass

MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
MIDDLEWARE_CLASSES += [
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

if DJANGO_GTE_1_8:
    TEMPLATES[0]['OPTIONS']['context_processors'] += \
        DJANGO_CMS_CONTEXT_PROCESSORS
else:
    TEMPLATE_CONTEXT_PROCESSORS = list(TEMPLATE_CONTEXT_PROCESSORS)
    TEMPLATE_CONTEXT_PROCESSORS += DJANGO_CMS_CONTEXT_PROCESSORS

FOBI_DEFAULT_THEME = 'bootstrap3'
# FOBI_DEFAULT_THEME = 'foundation5'
# FOBI_DEFAULT_THEME = 'simple'

CMS_TEMPLATES = (
    ('cms_page/{0}/page_with_sidebar.html'.format(FOBI_DEFAULT_THEME),
     'General template with sidebar for {0}'.format(FOBI_DEFAULT_THEME)),
    ('cms_page/{0}/page_without_sidebar.html'.format(FOBI_DEFAULT_THEME),
     'General template without sidebar for {0}'.format(FOBI_DEFAULT_THEME)),
)

LANGUAGE_CODE = 'en'
