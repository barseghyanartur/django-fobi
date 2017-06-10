# Django settings for wagtaildemo project.

import os

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '..', '..')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Default to dummy email backend. Configure dev/production/local backend
# as per https://docs.djangoproject.com/en/dev/topics/email/#email-backends
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wagtaildemo',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',  # Set to empty string for localhost.
        'PORT': '',  # Set to empty string for default.
        'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
# Note that with this set to True, Wagtail will fall back on using numeric dates
# in date fields, as opposed to 'friendly' dates like "24 Sep 2013", because
# Python's strptime doesn't support localised month names: https://code.djangoproject.com/ticket/13339
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# ** You would never normally put the SECRET_KEY in a public repository,
# ** however this is a demo app so we're using the default settings.
# ** Don't use this key in any non-demo usage!
# Make this unique, and don't share it with anybody.
SECRET_KEY = 'wq21wtjo3@d_qfjvd-#td!%7gfy2updj2z+nev^k$iy%=m4_tr'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',

    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    "fobi.context_processors.theme",  # Important!
    "fobi.context_processors.dynamic_values",  # Optional
    "context_processors.testing",  # Testing
)

ROOT_URLCONF = 'wagtaildemo.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wagtaildemo.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',  # Wagtail uses its own site management logic
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'south',
    'compressor',
    'taggit',
    'modelcluster',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailimages',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsearch',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',
    'wagtail.wagtailsites',

    'demo',

    # Third party apps used in the project
    # 'south',  # Database migration app
    # 'tinymce',  # TinyMCE
    'easy_thumbnails',  # Thumbnailer
    'registration',  # Auth views and registration app

    # ***********************************************************************
    # ***********************************************************************
    # **************************** Fobi core ********************************
    # ***********************************************************************
    # ***********************************************************************
    'fobi',

    # ***********************************************************************
    # ***********************************************************************
    # ************************* Fobi form elements **************************
    # ***********************************************************************
    # ***********************************************************************

    # ***********************************************************************
    # **************************** Form fields ******************************
    # ***********************************************************************
    # 'fobi.contrib.plugins.form_elements.fields.birthday',
    'fobi.contrib.plugins.form_elements.fields.boolean',
    'fobi.contrib.plugins.form_elements.fields.checkbox_select_multiple',
    'fobi.contrib.plugins.form_elements.fields.date',
    'fobi.contrib.plugins.form_elements.fields.date_drop_down',
    'fobi.contrib.plugins.form_elements.fields.datetime',
    'fobi.contrib.plugins.form_elements.fields.decimal',
    'fobi.contrib.plugins.form_elements.fields.email',
    'fobi.contrib.plugins.form_elements.fields.file',
    'fobi.contrib.plugins.form_elements.fields.float',
    'fobi.contrib.plugins.form_elements.fields.hidden',
    # 'fobi.contrib.plugins.form_elements.fields.hidden_model_object',
    'fobi.contrib.plugins.form_elements.fields.input',
    'fobi.contrib.plugins.form_elements.fields.integer',
    'fobi.contrib.plugins.form_elements.fields.ip_address',
    'fobi.contrib.plugins.form_elements.fields.null_boolean',
    'fobi.contrib.plugins.form_elements.fields.password',
    'fobi.contrib.plugins.form_elements.fields.radio',
    'fobi.contrib.plugins.form_elements.fields.range_select',
    'fobi.contrib.plugins.form_elements.fields.regex',
    'fobi.contrib.plugins.form_elements.fields.select',
    'fobi.contrib.plugins.form_elements.fields.select_model_object',
    'fobi.contrib.plugins.form_elements.fields.select_multiple',
    'fobi.contrib.plugins.form_elements.fields.select_multiple_with_max',
    'fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects',
    'fobi.contrib.plugins.form_elements.fields.slider',
    'fobi.contrib.plugins.form_elements.fields.slug',
    'fobi.contrib.plugins.form_elements.fields.text',
    'fobi.contrib.plugins.form_elements.fields.textarea',
    'fobi.contrib.plugins.form_elements.fields.time',
    'fobi.contrib.plugins.form_elements.fields.url',

    # ***********************************************************************
    # ************************ Security elements ****************************
    # ***********************************************************************
    'fobi.contrib.plugins.form_elements.security.honeypot',

    # ***********************************************************************
    # ************************* Testing elements ****************************
    # ***********************************************************************
    'fobi.contrib.plugins.form_elements.test.dummy',

    # ***********************************************************************
    # ************************* Content elements ****************************
    # ***********************************************************************
    'fobi.contrib.plugins.form_elements.content.content_image',
    'fobi.contrib.plugins.form_elements.content.content_text',
    'fobi.contrib.plugins.form_elements.content.content_video',

    # ***********************************************************************
    # ***********************************************************************
    # ************************* Fobi form handlers **************************
    # ***********************************************************************
    # ***********************************************************************
    'fobi.contrib.plugins.form_handlers.db_store',
    'fobi.contrib.plugins.form_handlers.http_repost',
    'fobi.contrib.plugins.form_handlers.mail',

    # ***********************************************************************
    # ***********************************************************************
    # ************************* Fobi form importers *************************
    # ***********************************************************************
    # ***********************************************************************
    'fobi.contrib.plugins.form_importers.mailchimp_importer',

    # ***********************************************************************
    # ***********************************************************************
    # ************************** Fobi themes ********************************
    # ***********************************************************************
    # ***********************************************************************

    # ***********************************************************************
    # ************************ Bootstrap 3 theme ****************************
    # ***********************************************************************
    'fobi.contrib.themes.bootstrap3',  # Bootstrap 3 theme
    # DateTime widget
    'fobi.contrib.themes.bootstrap3.widgets.form_elements.'
    'datetime_bootstrap3_widget',

    'fobi.contrib.themes.bootstrap3.widgets.form_elements.'
    'date_bootstrap3_widget',

    # SliderPercentage widget
    'fobi.contrib.themes.bootstrap3.widgets.form_elements.'
    'slider_bootstrap3_widget',

    # ***********************************************************************
    # ************************ Foundation 5 theme ***************************
    # ***********************************************************************
    'fobi.contrib.themes.foundation5',  # Foundation 5 theme

    'fobi.contrib.themes.foundation5.widgets.form_handlers.'
    'db_store_foundation5_widget',

    # ***********************************************************************
    # **************************** Simple theme *****************************
    # ***********************************************************************
    'fobi.contrib.themes.simple',  # Simple theme
)

EMAIL_SUBJECT_PREFIX = '[wagtaildemo] '

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')

# django-compressor settings
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

# Auth settings
LOGIN_URL = 'django.contrib.auth.views.login'
LOGIN_REDIRECT_URL = 'wagtailadmin_home'

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
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# WAGTAIL SETTINGS

WAGTAIL_SITE_NAME = 'wagtaildemo'

# Override the search results template for wagtailsearch
WAGTAILSEARCH_RESULTS_TEMPLATE = 'demo/search_results.html'
