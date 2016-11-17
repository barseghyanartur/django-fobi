from nine.versions import DJANGO_GTE_1_8

from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS.remove('django.contrib.admin')
INSTALLED_APPS += [
    'cms',  # DjangoCMS
    'mptt',
    'menus',
    'sekizai',
    # 'djangocms_admin_style',

    # Some plugins
    'djangocms_picture',
    'djangocms_snippet',
    'treebeard',

    'fobi.contrib.apps.djangocms_integration',  # Fobi DjangoCMS app

    # Django-CMS admin style
    'djangocms_admin_style',
    'django.contrib.admin',
    'fobi.contrib.themes.djangocms_admin_style_theme',
]

try:
    INSTALLED_APPS.remove('admin_tools') \
        if 'admin_tools' in INSTALLED_APPS else None
    INSTALLED_APPS.remove('admin_tools.menu') \
        if 'admin_tools.menu' in INSTALLED_APPS else None
    INSTALLED_APPS.remove('admin_tools.dashboard') \
        if 'admin_tools.dashboard' in INSTALLED_APPS else None
except Exception as e:
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
    TEMPLATES[0]['OPTIONS']['context_processors'] += [
        'cms.context_processors.cms_settings',
        'sekizai.context_processors.sekizai',
        'cms.context_processors.cms_settings',
    ]
else:
    TEMPLATE_CONTEXT_PROCESSORS = list(TEMPLATE_CONTEXT_PROCESSORS)
    TEMPLATE_CONTEXT_PROCESSORS += [
        'cms.context_processors.cms_settings',
        'sekizai.context_processors.sekizai',
        'cms.context_processors.cms_settings',
    ]

# FOBI_DEFAULT_THEME = 'bootstrap3'
# FOBI_DEFAULT_THEME = 'foundation5'
# FOBI_DEFAULT_THEME = 'simple'
FOBI_DEFAULT_THEME = 'djangocms_admin_style_theme'

CMS_TEMPLATES = (
    ('cms_page/{0}/page_with_sidebar.html'.format(FOBI_DEFAULT_THEME),
     'General template with sidebar for {0}'.format(FOBI_DEFAULT_THEME)),
    ('cms_page/{0}/page_without_sidebar.html'.format(FOBI_DEFAULT_THEME),
     'General template without sidebar for {0}'.format(FOBI_DEFAULT_THEME)),
)

MIGRATION_MODULES = {
    'cms': 'cms.migrations_django',
    'menus': 'menus.migrations_django',
}

LANGUAGE_CODE = 'en'
