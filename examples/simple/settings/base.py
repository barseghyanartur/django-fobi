# Django settings for example project.
import os
from nine.versions import (
    DJANGO_GTE_2_0,
    DJANGO_GTE_1_10,
    DJANGO_GTE_1_8,
    DJANGO_GTE_1_9,
)


def project_dir(base):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), base).replace('\\', '/')
    )


PROJECT_DIR = project_dir


def gettext(s):
    return s


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = False
DEBUG_TOOLBAR = False
DEV = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': PROJECT_DIR('../../db/example.db'),
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        # Empty for localhost through domain sockets or '127.0.0.1' for
        # localhost through TCP.
        'HOST': '',
        # Set to empty string for default.
        'PORT': '',
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
LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', gettext("English")),  # Main language!
    ('hy', gettext("Armenian")),
    ('nl', gettext("Dutch")),
    ('ru', gettext("Russian")),
    ('de', gettext("German")),
    ('fr', gettext("French")),
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

# Absolute filesystem path to the directory that will hold user-uploaded
# files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_DIR(os.path.join('..', '..', 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_DIR(os.path.join('..', '..', 'static'))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR(os.path.join('..', '..', 'media', 'static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '97818c*w97Zi8a-m^1coRRrmurMI6+q5_kyn*)s@(*_Pk6q423'

try:
    from .local_settings import DEBUG_TEMPLATE
except Exception as err:
    DEBUG_TEMPLATE = False

if DJANGO_GTE_1_10:
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            # 'APP_DIRS': True,
            'DIRS': [PROJECT_DIR(os.path.join('..', 'templates'))],
            'OPTIONS': {
                'context_processors': [
                    "django.template.context_processors.debug",
                    'django.template.context_processors.request',
                    "django.contrib.auth.context_processors.auth",
                    # "django.core.context_processors.i18n",
                    # "django.core.context_processors.media",
                    # "django.core.context_processors.static",
                    # "django.core.context_processors.tz",
                    "django.contrib.messages.context_processors.messages",
                    "fobi.context_processors.theme",  # Important!
                    "fobi.context_processors.dynamic_values",  # Optional
                    "context_processors.testing",  # Testing
                ],
                'loaders': [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    # 'django.template.loaders.eggs.Loader',
                    'admin_tools.template_loaders.Loader',
                ],
                'debug': DEBUG_TEMPLATE,
            }
        },
    ]
elif DJANGO_GTE_1_8:
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            # 'APP_DIRS': True,
            'DIRS': [PROJECT_DIR(os.path.join('..', 'templates'))],
            'OPTIONS': {
                'context_processors': [
                    "django.contrib.auth.context_processors.auth",
                    "django.template.context_processors.debug",
                    "django.template.context_processors.i18n",
                    "django.template.context_processors.media",
                    "django.template.context_processors.static",
                    "django.template.context_processors.tz",
                    "django.contrib.messages.context_processors.messages",
                    "django.template.context_processors.request",
                    "fobi.context_processors.theme",  # Important!
                    "fobi.context_processors.dynamic_values",  # Optional
                    "context_processors.testing",  # Testing
                ],
                'loaders': [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    'django.template.loaders.eggs.Loader',
                    'admin_tools.template_loaders.Loader',
                ],
                'debug': DEBUG_TEMPLATE,
            }
        },
    ]
else:
    TEMPLATE_DEBUG = DEBUG_TEMPLATE

    # List of callables that know how to import templates from various
    # sources.
    TEMPLATE_LOADERS = [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader',

    ]
    if DJANGO_GTE_1_8:
        TEMPLATE_LOADERS.append('admin_tools.template_loaders.Loader')

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.core.context_processors.tz",
        "django.contrib.messages.context_processors.messages",
        "django.core.context_processors.request",
        "fobi.context_processors.theme",  # Important!
        "fobi.context_processors.dynamic_values",  # Optional
        "context_processors.testing",  # Testing
    )

    TEMPLATE_DIRS = (
        # Put strings here, like "/home/html/django_templates" or
        # "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        PROJECT_DIR(os.path.join('..', 'templates')),
    )

# Final declaration of the middleware is done on the bottom of this file
_MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

# FIXTURE_DIRS = (
#   PROJECT_DIR(os.path.join('..', 'fixtures'))
# )

INSTALLED_APPS = [
    # Admin dashboard
    'admin_tools',
    'admin_tools.menu',
    'admin_tools.dashboard',

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
    # 'tinymce',  # TinyMCE
    'easy_thumbnails',  # Thumbnailer
    'registration',  # Auth views and registration app
    'captcha',
    'ckeditor',
    'fobi.reusable.markdown_widget',
    # 'ckeditor_uploader',

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
    'fobi.contrib.plugins.form_elements.fields.duration',
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
    'fobi.contrib.plugins.form_elements.security.invisible_recaptcha',

    # ***********************************************************************
    # ************************* Testing elements ****************************
    # ***********************************************************************
    'fobi.contrib.plugins.form_elements.test.dummy',

    # ***********************************************************************
    # ************************* Content elements ****************************
    # ***********************************************************************
    'fobi.contrib.plugins.form_elements.content.content_image',
    'fobi.contrib.plugins.form_elements.content.content_image_url',
    'fobi.contrib.plugins.form_elements.content.content_markdown',
    'fobi.contrib.plugins.form_elements.content.content_text',
    'fobi.contrib.plugins.form_elements.content.content_richtext',
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
    'fobi.contrib.themes.bootstrap3.widgets.form_elements.datetime_bootstrap3_widget',  # NOQA

    'fobi.contrib.themes.bootstrap3.widgets.form_elements.date_bootstrap3_widget',  # NOQA

    # Slider widget
    'fobi.contrib.themes.bootstrap3.widgets.form_elements.slider_bootstrap3_widget',  # NOQA

    # CKEditor widget
    'fobi.contrib.themes.bootstrap3.widgets.form_elements.content_richtext_bootstrap3_widget',  # NOQA

    # Invisible reCAPTCHA widget
    'fobi.contrib.themes.bootstrap3.widgets.form_elements.invisible_recaptcha_bootstrap3_widget',  # NOQA

    # # Markdown
    # 'fobi.contrib.themes.bootstrap3.widgets.form_elements.content_markdown_bootstrap3_widget',  # NOQA

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

    # ***********************************************************************
    # ***********************************************************************
    # ************************* Fobi form importers *************************
    # ***********************************************************************
    # ***********************************************************************
    # 'fobi.contrib.plugins.form_importers.mailchimp_importer',

    # ***********************************************************************
    # ***********************************************************************
    # ********************* Custom field instance plugins *******************
    # ***********************************************************************
    # ***********************************************************************

    # ***********************************************************************
    # ************************** DRF integration ****************************
    # ***********************************************************************
    'rest_framework',  # Django REST framework
    'fobi.contrib.apps.drf_integration',  # DRF integration app

    # Form fields
    'fobi.contrib.apps.drf_integration.form_elements.fields.boolean',
    'fobi.contrib.apps.drf_integration.form_elements.fields.checkbox_select_multiple',  # NOQA
    'fobi.contrib.apps.drf_integration.form_elements.fields.date',
    'fobi.contrib.apps.drf_integration.form_elements.fields.date_drop_down',
    'fobi.contrib.apps.drf_integration.form_elements.fields.datetime',
    'fobi.contrib.apps.drf_integration.form_elements.fields.decimal',
    'fobi.contrib.apps.drf_integration.form_elements.fields.duration',
    'fobi.contrib.apps.drf_integration.form_elements.fields.email',
    'fobi.contrib.apps.drf_integration.form_elements.fields.file',
    'fobi.contrib.apps.drf_integration.form_elements.fields.float',
    'fobi.contrib.apps.drf_integration.form_elements.fields.hidden',
    'fobi.contrib.apps.drf_integration.form_elements.fields.input',
    'fobi.contrib.apps.drf_integration.form_elements.fields.integer',
    'fobi.contrib.apps.drf_integration.form_elements.fields.ip_address',
    'fobi.contrib.apps.drf_integration.form_elements.fields.null_boolean',
    'fobi.contrib.apps.drf_integration.form_elements.fields.password',
    'fobi.contrib.apps.drf_integration.form_elements.fields.radio',
    'fobi.contrib.apps.drf_integration.form_elements.fields.range_select',
    'fobi.contrib.apps.drf_integration.form_elements.fields.regex',
    'fobi.contrib.apps.drf_integration.form_elements.fields.select',
    # 'fobi.contrib.apps.drf_integration.form_elements.fields.select_model_object',  # NOQA
    'fobi.contrib.apps.drf_integration.form_elements.fields.select_multiple',
    # 'fobi.contrib.apps.drf_integration.form_elements.fields.select_multiple_model_objects',  # NOQA
    'fobi.contrib.apps.drf_integration.form_elements.fields.select_multiple_with_max',  # NOQA
    'fobi.contrib.apps.drf_integration.form_elements.fields.slider',
    'fobi.contrib.apps.drf_integration.form_elements.fields.slug',
    'fobi.contrib.apps.drf_integration.form_elements.fields.text',
    'fobi.contrib.apps.drf_integration.form_elements.fields.textarea',
    'fobi.contrib.apps.drf_integration.form_elements.fields.time',
    'fobi.contrib.apps.drf_integration.form_elements.fields.url',

    # Presentational elements
    'fobi.contrib.apps.drf_integration.form_elements.content.content_image',
    'fobi.contrib.apps.drf_integration.form_elements.content.content_image_url',  # NOQA
    'fobi.contrib.apps.drf_integration.form_elements.content.content_markdown',
    'fobi.contrib.apps.drf_integration.form_elements.content.content_richtext',
    'fobi.contrib.apps.drf_integration.form_elements.content.content_text',
    'fobi.contrib.apps.drf_integration.form_elements.content.content_video',

    # Form handlers
    'fobi.contrib.apps.drf_integration.form_handlers.db_store',
    'fobi.contrib.apps.drf_integration.form_handlers.mail',
    'fobi.contrib.apps.drf_integration.form_handlers.http_repost',

    # ***********************************************************************
    # ***********************************************************************
    # ***********************************************************************

    # Other project specific apps
    'foo',  # Test app
]

STATIC_ROOT = PROJECT_DIR(os.path.join('..', '..', 'static'))
CKEDITOR_UPLOAD_PATH = PROJECT_DIR(
    os.path.join('..', '..', 'media', 'uploads')
)
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent',
             'HorizontalRule', '-', 'JustifyLeft', 'JustifyCenter',
             'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Image'],
            ['Table'],
            ['RemoveFormat'],
        ],
        # 'height': 300,
        'width': '100%',
    }
}

# LOGIN_URL = '/accounts/login/'
# LOGIN_REDIRECT_URL = '/fobi/' # Important for passing the selenium tests

# if DJANGO_GTE_1_8:
LOGIN_URL = '/en/accounts/login/'
LOGIN_REDIRECT_URL = '/en/fobi/'  # Important for passing the selenium tests

# LOGIN_URL = '/accounts/login/'
# LOGIN_ERROR_URL = '/accounts/login/'
# LOGOUT_URL = '/accounts/logout/'

PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"  # Just for tests
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"  # Just for tests

# MIGRATION_MODULES = {
#    'fobi': 'migrations',
#    'db_store': 'fobi.contrib.plugins.form_handlers.db_store.migrations'
# }
# SOUTH_MIGRATION_MODULES = 'south_migrations'

# **************************************************************
# ********************* Registration settings ******************
# **************************************************************


ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_FORM = 'registration_addons.forms.CaptchaRegistrationForm'
SIMPLE_BACKEND_REDIRECT_URL = '/en/'

# **************************************************************
# ************************ Fobi settings ***********************
# **************************************************************

# Fobi custom theme data for to be displayed in third party apps
# like `django-registraton`.
FOBI_CUSTOM_THEME_DATA = {
    'bootstrap3': {
        'page_header_html_class': '',
        'form_html_class': 'form-horizontal',
        'form_button_outer_wrapper_html_class': 'control-group',
        'form_button_wrapper_html_class': 'controls',
        'form_button_html_class': 'btn',
        'form_primary_button_html_class': 'btn-primary pull-right',
        'feincms_integration': {
            'form_template_choices': [
                (
                    'fobi/bootstrap3_extras/view_embed_form_entry_ajax.html',
                    gettext("Custom bootstrap3 embed form view template")
                ),
            ],
            'success_page_template_choices': [
                (
                    'fobi/bootstrap3_extras/embed_form_entry_submitted_ajax.html',  # NOQA
                    gettext("Custom bootstrap3 embed form entry submitted "
                            "template")
                ),
            ],
        },
        'djangocms_integration': {
            'form_template_choices': [
                (
                    'fobi/bootstrap3_extras/view_embed_form_entry_ajax.html',
                    gettext("Custom bootstrap3 embed form view template")
                ),
            ],
            'success_page_template_choices': [
                (
                    'fobi/bootstrap3_extras/embed_form_entry_submitted_ajax.html',  # NOQA
                    gettext("Custom bootstrap3 embed form entry submitted "
                            "template")
                ),
            ],
        },
    },
    'foundation5': {
        'page_header_html_class': '',
        'form_html_class': 'form-horizontal',
        'form_button_outer_wrapper_html_class': 'control-group',
        'form_button_wrapper_html_class': 'controls',
        'form_button_html_class': 'radius button',
        'form_primary_button_html_class': 'btn-primary',
        'feincms_integration': {
            'form_template_choices': [
                (
                    'fobi/foundation5_extras/view_embed_form_entry_ajax.html',
                    gettext("Custom foundation5 embed form view template")
                ),
            ],
            'success_page_template_choices': [
                (
                    'fobi/foundation5_extras/embed_form_entry_submitted_ajax.html',  # NOQA
                    gettext("Custom foundation5 embed form entry submitted "
                            "template")
                ),
            ],
        },
        'djangocms_integration': {
            'form_template_choices': [
                (
                    'fobi/foundation5_extras/view_embed_form_entry_ajax.html',
                    gettext("Custom foundation5 embed form view template")
                ),
            ],
            'success_page_template_choices': [
                (
                    'fobi/foundation5_extras/embed_form_entry_submitted_ajax.html',  # NOQA
                    gettext("Custom foundation5 embed form entry submitted "
                            "template")
                ),
            ],
        },
    },
    'simple': {
        'page_header_html_class': '',
        'form_html_class': 'form-horizontal',
        'form_button_outer_wrapper_html_class': 'control-group',
        'form_button_wrapper_html_class': 'submit-row',
        'form_button_html_class': 'btn',
        'form_primary_button_html_class': 'btn-primary',
        'feincms_integration': {
        },
        'djangocms_integration': {
        },
    }
}

FOBI_THEME_FOOTER_TEXT = gettext('&copy; django-fobi example site 2014-2015')

FOBI_PLUGIN_MAIL_AUTO_MAIL_TO = ['to@example.info']
FOBI_PLUGIN_MAIL_AUTO_MAIL_SUBJECT = 'Automatic email'
FOBI_PLUGIN_MAIL_AUTO_MAIL_BODY = 'Automatic email'
FOBI_PLUGIN_MAIL_AUTO_MAIL_FROM = 'from@example.com'

# django-admin-tools custom dashboard
ADMIN_TOOLS_INDEX_DASHBOARD = 'admin_tools_dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = \
    'admin_tools_dashboard.CustomAppIndexDashboard'
ADMIN_TOOLS_MENU = 'admin_tools_dashboard.menu.CustomMenu'

SOUTH_MIGRATION_MODULES = {
    'fobi': 'fobi.south_migrations',
    'db_store': 'ignore',
}

MIGRATION_MODULES = {
    'fobi': 'fobi.migrations',
    'db_store': 'fobi.contrib.plugins.form_handlers.db_store.migrations',
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
    'root': {
        'level': 'INFO',
        'handlers': ['all_log'],
    },
    'formatters': {
        'verbose': {
            'format': '\n%(levelname)s %(asctime)s [%(pathname)s:%(lineno)s] '
                      '%(message)s'
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
        'all_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR("../../logs/all.log"),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
        'django_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR("../../logs/django.log"),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
        'django_request_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR("../../logs/django_request.log"),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
        'fobi_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR("../../logs/fobi.log"),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['django_request_log'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['django_log'],
            'level': 'ERROR',
            'propagate': False,
        },
        'fobi': {
            'handlers': ['console', 'fobi_log'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Make settings quite compatible among various Django versions used.
if DJANGO_GTE_1_8:
    INSTALLED_APPS = list(INSTALLED_APPS)

    # Django 1.8 specific checks
    if DJANGO_GTE_1_8:
        try:
            INSTALLED_APPS.remove('admin_tools') \
                if 'admin_tools' in INSTALLED_APPS else None
            INSTALLED_APPS.remove('admin_tools.menu') \
                if 'admin_tools.menu' in INSTALLED_APPS else None
            INSTALLED_APPS.remove('admin_tools.dashboard') \
                if 'admin_tools.dashboard' in INSTALLED_APPS else None
        except Exception as e:
            pass

# For Selenium tests
FIREFOX_BIN_PATH = ''
PHANTOM_JS_EXECUTABLE_PATH = None

# Testing mode
TESTING = False

# Do not put any settings below this line
try:
    from .local_settings import *
except Exception as err:
    pass

if DEBUG and DEBUG_TOOLBAR:
    try:
        # Make sure the django-debug-toolbar is installed
        import debug_toolbar

        # debug_toolbar
        _MIDDLEWARE += (
            'debug_toolbar.middleware.DebugToolbarMiddleware',
        )

        INSTALLED_APPS += (
            'debug_toolbar',
        )

        DEBUG_TOOLBAR_CONFIG = {
            'INTERCEPT_REDIRECTS': False,
        }
    except ImportError:
        pass

# Only now make proper assignments
if DJANGO_GTE_2_0:
    MIDDLEWARE = _MIDDLEWARE
else:
    MIDDLEWARE_CLASSES = _MIDDLEWARE

if DEBUG:
    try:
        # Make sure the django-template-debug is installed. You can then
        # in templates use it as follows:
        #
        # {% load debug_tags %}
        # {% set_trace %}
        import template_debug
        INSTALLED_APPS += (
            'template_debug',
        )
    except ImportError:
        pass

# if DEBUG:
#     try:
#         # Make sure the django-template-debug is installed. You can then
#         # in templates use it as follows:
#         #
#         # {% load debug_tags %}
#         # {% set_trace %}
#         import debug_toolbar_mongo
#         INSTALLED_APPS += (
#             'debug_toolbar_mongo',
#         )
#         DEBUG_TOOLBAR_PANELS = (
#             'debug_toolbar_mongo.panel.MongoDebugPanel',
#         )
#     except ImportError:
#         pass

# Make the `django-fobi` package available without installation.
if DEV:
    import sys
    fobi_source_path = os.environ.get('FOBI_SOURCE_PATH', 'src')
    # sys.path.insert(0, os.path.abspath('src'))
    sys.path.insert(0, os.path.abspath(fobi_source_path))
