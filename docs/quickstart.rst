===========
Quick start
===========
Tutorial for very quick start with ``django-fobi``. Consists of
several parts listed below::

- Part 1: Standard Django installation
- Part 2: Integration with DjangoCMS (coming soon)

Part 1: standard Django installation
====================================
Example project code available `here
<https://github.com/barseghyanartur/django-fobi/tree/master/examples/quick_start>`_.

Installation and configuration
------------------------------
Install the package in your environment.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: sh

    pip install django-fobi

INSTALLED_APPS
^^^^^^^^^^^^^^
Add ``fobi`` core and the plugins to the ``INSTALLED_APPS`` of the your
``settings`` module.

1. The core.

.. code-block:: python

    'fobi',

2. The preferred theme. Bootstrap 3 theme is the default. If you have chosen a
   different theme, update the value of ``FOBI_DEFAULT_THEME`` accordingly.

.. code-block:: python

    'fobi.contrib.themes.bootstrap3',

3. The form field plugins. Plugins are like blocks. You are recommended to have
   them all installed. Note, that the following plugins do not have
   additional dependencies, while some others (like
   `fobi.contrib.plugins.form_elements.security.captcha
   <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/security/captcha/>`_
   or `fobi.contrib.plugins.form_elements.security.recaptcha
   <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/security/recaptcha/>`_
   would require additional packages to be installed. If so, make sure to have
   installed and configured those dependencies prior adding the dependant
   add-ons to the ``settings`` module.

.. code-block:: python

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
    'fobi.contrib.plugins.form_elements.fields.input',
    'fobi.contrib.plugins.form_elements.fields.integer',
    'fobi.contrib.plugins.form_elements.fields.ip_address',
    'fobi.contrib.plugins.form_elements.fields.null_boolean',
    'fobi.contrib.plugins.form_elements.fields.password',
    'fobi.contrib.plugins.form_elements.fields.radio',
    'fobi.contrib.plugins.form_elements.fields.regex',
    'fobi.contrib.plugins.form_elements.fields.select',
    'fobi.contrib.plugins.form_elements.fields.select_model_object',
    'fobi.contrib.plugins.form_elements.fields.select_multiple',
    'fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects',
    'fobi.contrib.plugins.form_elements.fields.slug',
    'fobi.contrib.plugins.form_elements.fields.text',
    'fobi.contrib.plugins.form_elements.fields.textarea',
    'fobi.contrib.plugins.form_elements.fields.time',
    'fobi.contrib.plugins.form_elements.fields.url',

4. The presentational form elements (images, texts, videos).

.. code-block:: python

    'easy_thumbnails',  # Required by `content_image` plugin
    'fobi.contrib.plugins.form_elements.content.content_image',
    'fobi.contrib.plugins.form_elements.content.content_text',
    'fobi.contrib.plugins.form_elements.content.content_video',

5. Form handlers. Note, that some of them may require database sync/migration.

.. code-block:: python

    'fobi.contrib.plugins.form_handlers.db_store',
    'fobi.contrib.plugins.form_handlers.http_repost',
    'fobi.contrib.plugins.form_handlers.mail',

Putting all together, you would have something like this.

.. code-block:: python

    INSTALLED_APPS = (
        # Used by fobi
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',

        # ...
        # Core
        'fobi',

        # Theme
        'fobi.contrib.themes.bootstrap3',

        # Form field plugins
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
        'fobi.contrib.plugins.form_elements.fields.input',
        'fobi.contrib.plugins.form_elements.fields.integer',
        'fobi.contrib.plugins.form_elements.fields.ip_address',
        'fobi.contrib.plugins.form_elements.fields.null_boolean',
        'fobi.contrib.plugins.form_elements.fields.password',
        'fobi.contrib.plugins.form_elements.fields.radio',
        'fobi.contrib.plugins.form_elements.fields.regex',
        'fobi.contrib.plugins.form_elements.fields.select',
        'fobi.contrib.plugins.form_elements.fields.select_model_object',
        'fobi.contrib.plugins.form_elements.fields.select_multiple',
        'fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects',
        'fobi.contrib.plugins.form_elements.fields.slug',
        'fobi.contrib.plugins.form_elements.fields.text',
        'fobi.contrib.plugins.form_elements.fields.textarea',
        'fobi.contrib.plugins.form_elements.fields.time',
        'fobi.contrib.plugins.form_elements.fields.url',

        # Form element plugins
        'easy_thumbnails',  # Required by ``content_image`` plugin
        'fobi.contrib.plugins.form_elements.content.content_image',
        'fobi.contrib.plugins.form_elements.content.content_text',
        'fobi.contrib.plugins.form_elements.content.content_video',

        # Form handlers
        'fobi.contrib.plugins.form_handlers.db_store',
        'fobi.contrib.plugins.form_handlers.http_repost',
        'fobi.contrib.plugins.form_handlers.mail',

        # ...
    )

TEMPLATE_CONTEXT_PROCESSORS
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Add ``django.core.context_processors.request`` and
``fobi.context_processors.theme`` to ``TEMPLATES`` of
your ``settings`` module.

.. code-block:: python

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [(os.path.join('path', 'to', 'your', 'templates'))],
            'OPTIONS': {
                'context_processors': [
                    "django.template.context_processors.debug",
                    'django.template.context_processors.request',
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                    "fobi.context_processors.theme",  # Important!
                    "fobi.context_processors.dynamic_values",  # Optional
                ],
                'loaders': [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    'admin_tools.template_loaders.Loader',
                ],
                'debug': DEBUG_TEMPLATE,
            }
        },
    ]

urlpatterns
^^^^^^^^^^^
Add the following line to ``urlpatterns`` of your ``urls`` module.

.. code-block:: python

    urlpatterns = [
        # ...

        # DB Store plugin URLs
        url(r'^fobi/plugins/form-handlers/db-store/',
            include('fobi.contrib.plugins.form_handlers.db_store.urls')),

        # View URLs
        url(r'^fobi/', include('fobi.urls.view')),

        # Edit URLs
        url(r'^fobi/', include('fobi.urls.edit')),

        # ...
    ]

Update the database
^^^^^^^^^^^^^^^^^^^
1. First you should migrate the database. Depending on your
   Django version and migration app, this step may vary. Typically as follows:

.. code-block:: sh

    ./manage.py migrate --fake-initial

2. Sync installed ``fobi`` plugins. Go to terminal and type the following
   command.

.. code-block:: sh

    ./manage.py fobi_sync_plugins

Specify the active theme
^^^^^^^^^^^^^^^^^^^^^^^^
Specify the default theme in your ``settings`` module.

.. code-block:: python

    FOBI_DEFAULT_THEME = 'bootstrap3'

Permissions
^^^^^^^^^^^
``fobi`` has been built with permissions in mind. Every single form element
plugin or handler is permission based. If user hasn't been given permission
to work with a form element or a form handler plugin, he won't be. If you want
to switch the permission checks off, set the value of
``FOBI_RESTRICT_PLUGIN_ACCESS`` to False in your `settings` module.

.. code-block:: python

    FOBI_RESTRICT_PLUGIN_ACCESS = False

Otherwise, after having completed all the steps above, do log into the
Django administration and assign the permissions (to certain user or a group)
for every single form element or form handler plugin. Bulk assignments work
as well.

- http://yourdomain.com/admin/fobi/formelement/
- http://yourdomain.com/admin/fobi/formhandler/

Also, make sure to have the Django model permissions set for following models:

- `fobi.models.FormEntry
  <https://github.com/barseghyanartur/django-fobi/blob/stable/src/fobi/models.py#L253>`_
- `fobi.models.FormElementEntry
  <https://github.com/barseghyanartur/django-fobi/blob/stable/src/fobi/models.py#L427>`_
- `fobi.models.FormHandlerEntry
  <https://github.com/barseghyanartur/django-fobi/blob/stable/src/fobi/models.py#L463>`_
- `fobi.contrib.plugins.form_handlers.db_store.models.SavedFormDataEntry
  <https://github.com/barseghyanartur/django-fobi/blob/stable/src/fobi/contrib/plugins/form_handlers/db_store/models.py#L52>`_

Part 2: Integration with DjangoCMS
==================================
Coming soon...
