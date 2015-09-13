# Django settings for example project.
import os
PROJECT_DIR = lambda base : os.path.abspath(os.path.join(os.path.dirname(__file__), base).replace('\\','/'))
gettext = lambda s: s

DEBUG = False
DEBUG_TOOLBAR = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': PROJECT_DIR('../db/example.db'), # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', gettext("English")), # Main language!
    ('hy', gettext("Armenian")),
    ('nl', gettext("Dutch")),
    ('ru', gettext("Russian")),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_DIR(os.path.join('..', 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_DIR(os.path.join('..', 'static'))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR(os.path.join('..', 'media', 'static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '97818c*w97Zi8a-m^1coRRrmurMI6+q5_kyn*)s@(*_Pk6q423'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "fobi.context_processors.theme", # Important!
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR('templates'),
)

#FIXTURE_DIRS = (
#   PROJECT_DIR(os.path.join('..', 'fixtures'))
#)

INSTALLED_APPS = (
    # Admin dashboard
    #'admin_tools',
    #'admin_tools.menu',
    #'admin_tools.dashboard',

    # Django core and contrib apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sitemaps',

    # Third party apps used in the project
    'south', # Database migration app
    'tinymce', # TinyMCE
    'easy_thumbnails', # Thumbnailer
    'registration', # Auth views and registration app
    #'localeurl', # Locale URL

    # Fobi core
    'fobi',

    # Fobi themes
    #'fobi.contrib.themes.bootstrap3', # Bootstrap 3 theme
    #'fobi.contrib.themes.foundation5', # Foundation 5 theme
    #'fobi.contrib.themes.simple', # Simple theme

    # Fobi form elements - fields
    #'fobi.contrib.plugins.form_elements.fields.boolean',
    #'fobi.contrib.plugins.form_elements.fields.email',
    #'fobi.contrib.plugins.form_elements.fields.file',
    #'fobi.contrib.plugins.form_elements.fields.hidden',
    #'fobi.contrib.plugins.form_elements.fields.integer',
    #'fobi.contrib.plugins.form_elements.fields.select',
    #'fobi.contrib.plugins.form_elements.fields.select_model_object',
    #'fobi.contrib.plugins.form_elements.fields.select_multiple',
    #'fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects',
    #'fobi.contrib.plugins.form_elements.fields.text',
    #'fobi.contrib.plugins.form_elements.fields.textarea',

    # Fobi form elements - content elements
    'fobi.contrib.plugins.form_elements.test.dummy',
    'fobi.contrib.plugins.form_elements.content.content_image',
    'fobi.contrib.plugins.form_elements.content.content_text',
    'fobi.contrib.plugins.form_elements.content.content_video',

    # Form handlers
    #'fobi.contrib.plugins.form_handlers.db_store',
    #'fobi.contrib.plugins.form_handlers.http_repost',
    #'fobi.contrib.plugins.form_handlers.mail',

    # Your custom fobi apps
    'sample_layout', # Sample theme/layout
    'sample_textarea', # Sample text area form element plugin
    'sample_mail', # Sample mail form handler plugin

    # Other project specific apps
    'foo', # Test app
)

LOGIN_REDIRECT_URL = '/fobi/' # Important for passing the selenium tests

#LOGIN_URL = '/accounts/login/'
#LOGIN_ERROR_URL = '/accounts/login/'
#LOGOUT_URL = '/accounts/logout/'

# localeurl locale independent paths (language code won't be appended)
LOCALE_INDEPENDENT_PATHS = (
    r'^/sitemap.*\.xml$', # Global regex for all XML sitemaps
    #r'^/admin/',
    #r'^/dashboard/',
)

# Tell localeurl to use sessions for language store.
LOCALEURL_USE_SESSION = True

# django-admin-tools custom dashboard
ADMIN_TOOLS_INDEX_DASHBOARD = 'admin_tools_dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'admin_tools_dashboard.CustomAppIndexDashboard'
ADMIN_TOOLS_MENU = 'admin_tools_dashboard.menu.CustomMenu'

SOUTH_MIGRATION_MODULES = {
    'fobi': 'fobi.south_migrations',
}

MIGRATION_MODULES = {
    'fobi': 'fobi.migrations',
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '\n%(levelname)s %(asctime)s [%(pathname)s:%(lineno)s] %(message)s'
        },
        'simple': {
            'format': '\n%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'django_log': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR("../logs/django.log"),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
        'fobi_log': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR("../logs/fobi.log"),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['django_log'],
            'level': 'ERROR',
            'propagate': True,
        },
        'fobi': {
            'handlers': ['console', 'fobi_log'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Do not put any settings below this line
try:
    from local_settings import *
except:
    pass

if DEBUG and DEBUG_TOOLBAR:
    # debug_toolbar
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
	)

    INSTALLED_APPS += (
        'debug_toolbar',
    )

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

if DEBUG and TEMPLATE_DEBUG:
    INSTALLED_APPS += (
        'template_debug',
    )
