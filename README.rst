===========
django-fobi
===========
`django-fobi` (or just `fobi`) is a customisable, modular, user- and developer-
friendly form generator/builder application for Django. With `fobi` you can
build Django forms using an intuitive GUI, save or mail posted form data or
even export forms into JSON format and import them on other instances. API
allows you to build your own form elements and form handlers (mechanisms for
handling the submitted form data).

Prerequisites
=============
- Django 1.8, 1.9, 1.10, 1.11, 2.0 and 2.1.
- Python 2.7, 3.4, 3.5, 3.6, 3.7 and PyPy.

Key concepts
============
- Each form consists of elements. Form elements are divided into two groups:

  (a) form fields (input field, textarea, hidden field, file field, etc.).
  (b) content (presentational) elements (text, image, embed video, etc.).

- Number of form elements is not limited.
- Each form may contain handlers. Handler processes the form data (for example,
  saves it or mails it). Number of the handlers is not limited.
- Both form elements and form handlers are made with Django permission system
  in mind.
- As an addition to form handlers, form callbacks are implemented. Form
  callbacks are fired on various stages of pre- and post-processing the form
  data (on POST). Form callbacks do not make use of permission system (unless
  you intentionally do so in the code of your callback) and are fired for all
  forms (unlike form handlers, that are executed only if assigned).
- Each plugin (form element or form handler) or a callback - is a Django
  micro-app.
- In addition for form element and form handler plugins, integration form
  element and integration form handler plugins are implemented for integration
  with diverse third-party apps and frameworks (such as Django REST framework).

Note, that `django-fobi` does not require django-admin and administrative
rights/permissions to access the UI, although almost seamless integration with
django-admin is implemented through the ``simple`` theme.

Main features and highlights
============================
- User-friendly GUI to quickly build forms.
- Large variety of `Bundled form element plugins`_. Most of the Django fields
  are supported. `HTML5 fields`_ are supported as well.
- `Form wizards`_. Combine your forms into wizards. Form wizards may contain
  handlers. Handler processes the form wizard data (for example, saves it or
  mails it). Number of the form wizard handlers is not limited.
- Forms can be automatically enabled/disabled based on dates (start date, end
  date).
- Anti-spam solutions like `CAPTCHA
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/security/captcha>`_,
  `ReCAPTCHA
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/security/recaptcha>`_,
  `Honeypot
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/security/honeypot>`_
  or `Invisible reCAPTCHA
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/security/invisible_recaptcha>`__
  come out of the box (CAPTCHA and ReCAPTCHA do require additional third-party
  apps to be installed; Invisible reCAPTCHA doesn't).
- In addition to standard form elements, there are cosmetic (presentational)
  form elements (for adding a piece of text, image or a embed video)
  alongside standard form elements.
- Data handling in plugins (form handlers). Save the data, mail it to some
  address or re-post it to some other endpoint. See the
  `Bundled form handler plugins`_ for more information.
- Developer-friendly API, which allows to edit existing or build new form
  fields and handlers without touching the core.
- Support for custom user model.
- `Theming`_. There are 4 ready to use `Bundled themes`_: "Bootstrap 3",
  "Foundation 5", "Simple" (with editing interface in style of Django admin)
  and "DjangoCMS admin style" theme (which is another simple theme with editing
  interface in style of `djangocms-admin-style
  <https://github.com/divio/djangocms-admin-style>`_).
- Implemented `integration with Django REST framework
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/apps/drf_integration>`_.
- Implemented `integration with Wagtail
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/apps/wagtail_integration>`_
  (in a form of a Wagtail page).
- Implemented `integration with FeinCMS
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/apps/feincms_integration>`_
  (in a form of a FeinCMS page widget).
- Implemented `integration with DjangoCMS
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/apps/djangocms_integration>`_
  (in a form of a DjangoCMS page plugin).
- Implemented `integration with Mezzanine
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/apps/mezzanine_integration>`_
  (in a form of a Mezzanine page).
- Reordering of form elements using drag-n-drop.
- Data export (`DB store
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_handlers/db_store>`_
  form handler plugin) into XLS/CSV format.
- `Dynamic initial values`_ for form elements.
- Import/export forms to/from JSON format.
- Import forms from MailChimp using `mailchimp importer
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_importers/mailchimp_importer>`_.

Roadmap
=======
Some of the upcoming/in-development features/improvements are:

- Implement disabling forms based on dates.
- Class based views.
- Cloning of forms.
- JSON schema support.
- Webpack integration.
- Improved Django REST framework OPTIONS.
- Bootstrap 4 support.
- Foundation 6 support.

See the `TODOS
<https://raw.githubusercontent.com/barseghyanartur/django-fobi/master/TODOS.rst>`_
for the full list of planned-, pending- in-development- or to-be-implemented
features.

Some screenshots
================
See the documentation for some screen shots:

- `ReadTheDocs <http://django-fobi.readthedocs.org/#screenshots>`_

Demo
====
Live demo
---------
See the `live demo app <https://django-fobi.herokuapp.com/>`_ on Heroku.
Additionally, see the `Django REST framework integration demo
<https://django-fobi.herokuapp.com/api/>`_.

Credentials:

- username: test_user
- password: test_user

Run demo locally
----------------
In order to be able to quickly evaluate the ``django-fobi``, a demo app (with a
quick installer) has been created (works on Ubuntu/Debian, may work on other
Linux systems as well, although not guaranteed). Follow the instructions below
for having the demo running within a minute.

Grab the latest ``django_fobi_example_app_installer.sh``:

.. code-block:: sh

    wget https://raw.github.com/barseghyanartur/django-fobi/stable/examples/django_fobi_example_app_installer.sh

Assign execute rights to the installer and run the
`django_fobi_example_app_installer.sh`:

.. code-block:: sh

    chmod +x django_fobi_example_app_installer.sh
    ./django_fobi_example_app_installer.sh

Open your browser and test the app.

Dashboard:

- URL: http://127.0.0.1:8001/fobi/
- Admin username: test_admin
- Admin password: test

Django admin interface:

- URL: http://127.0.0.1:8001/admin/
- Admin username: test_admin
- Admin password: test

If quick installer doesn't work for you, see the manual steps on running the
`example project
<https://github.com/barseghyanartur/django-fobi/tree/stable/examples>`_.

Quick start
===========
See the `quick start <http://django-fobi.readthedocs.io/en/latest/quickstart.html>`_.

Installation
============

(1) Install latest stable version from PyPI:

.. code-block:: sh

    pip install django-fobi

Or latest stable version from GitHub:

.. code-block:: sh

    pip install https://github.com/barseghyanartur/django-fobi/archive/stable.tar.gz

Or latest stable version from BitBucket:

.. code-block:: sh

    pip install https://bitbucket.org/barseghyanartur/django-fobi/get/stable.tar.gz

(2) Add `fobi` to ``INSTALLED_APPS`` of the your projects' Django settings.
    Furthermore, all themes and plugins to be used, shall be added to the
    ``INSTALLED_APPS`` as well. Note, that if a plugin has additional
    dependencies, you should be mentioning those in the ``INSTALLED_APPS``
    as well.

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
        # `django-fobi` core
        'fobi',

        # `django-fobi` themes
        'fobi.contrib.themes.bootstrap3', # Bootstrap 3 theme
        'fobi.contrib.themes.foundation5', # Foundation 5 theme
        'fobi.contrib.themes.simple', # Simple theme

        # `django-fobi` form elements - fields
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

        # `django-fobi` form elements - content elements
        'fobi.contrib.plugins.form_elements.test.dummy',
        'easy_thumbnails', # Required by `content_image` plugin
        'fobi.contrib.plugins.form_elements.content.content_image',
        'fobi.contrib.plugins.form_elements.content.content_image_url',
        'fobi.contrib.plugins.form_elements.content.content_text',
        'fobi.contrib.plugins.form_elements.content.content_video',

        # `django-fobi` form handlers
        'fobi.contrib.plugins.form_handlers.db_store',
        'fobi.contrib.plugins.form_handlers.http_repost',
        'fobi.contrib.plugins.form_handlers.mail',

        # Other project specific apps
        'foo', # Test app
        # ...
    )

(3) Make appropriate changes to the ``TEMPLATES`` of the your projects'
    Django settings.

And ``fobi.context_processors.theme`` and
``fobi.context_processors.dynamic_values``. See the following example.

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

Make sure that ``django.core.context_processors.request`` is in
``context_processors`` too.

(4) Configure URLs

Add the following line to urlpatterns of your `urls` module.

.. code-block:: python

    # View URLs
    url(r'^fobi/', include('fobi.urls.view')),

    # Edit URLs
    url(r'^fobi/', include('fobi.urls.edit')),

Note, that some plugins require additional URL includes. For instance, if you
listed the ``fobi.contrib.plugins.form_handlers.db_store`` form handler plugin
in the ``INSTALLED_APPS``, you should mention the following in ``urls``
module.

.. code-block:: python

    # DB Store plugin URLs
    url(r'^fobi/plugins/form-handlers/db-store/',
        include('fobi.contrib.plugins.form_handlers.db_store.urls')),

View URLs are put separately from edit URLs in order to make it possible
to prefix the edit URLs differently. For example, if you're using the
"Simple" theme, you would likely want to prefix the edit URLs with "admin/"
so that it looks more like django-admin.

Creating a new form element plugin
==================================
Form element plugins represent the elements of which the forms is made:
Inputs, checkboxes, textareas, files, hidden fields, as well as pure
presentational elements (text or image). Number of form elements in a form
is not limited.

Presentational form elements are inherited from ``fobi.base.FormElementPlugin``.

The rest (real form elements, that are supposed to have a value)
are inherited from ``fobi.base.FormFieldPlugin``.

You should see a form element plugin as a Django micro app, which could have
its' own models, admin interface, etc.

`django-fobi` comes with several bundled form element plugins. Do check the
source code as example.

Let's say, you want to create a textarea form element plugin.

There are several properties, each textarea should have. They are:

- `label` (string): HTML label of the textarea.
- `name` (string): HTML name of the textarea.
- `initial` (string): Initial value of the textarea.
- `required` (bool): Flag, which tells us whether the field is required or
  optional.

Let's name that plugin ``sample_textarea``. The plugin directory should then
have the following structure.

.. code-block:: sh

    path/to/sample_textarea/
    ├── __init__.py
    ├── fobi_form_elements.py # Where plugins are defined and registered
    ├── forms.py # Plugin configuration form
    └── widgets.py # Where plugins widgets are defined

Form element plugins should be registered in "fobi_form_elements.py" file. Each
plugin module should be put into the ``INSTALLED_APPS`` of your Django
projects' settings.

In some cases, you would need plugin specific overridable settings (see
``fobi.contrib.form_elements.fields.content.content_image`` plugin as an
example). You are advised to write your settings in such a way, that variables
of your Django project settings module would have `FOBI_PLUGIN_` prefix.

Define and register the form element plugin
-------------------------------------------
Step by step review of a how to create and register a plugin and plugin
widgets. Note, that `django-fobi` auto-discovers your plugins if you place
them into a file named ``fobi_form_elements.py`` of any Django app listed in
``INSTALLED_APPS`` of your Django projects' settings module.

path/to/sample_textarea/fobi_form_elements.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A single form element plugin is registered by its' UID.

Required imports.

.. code-block:: python

    from django import forms
    from fobi.base import FormFieldPlugin, form_element_plugin_registry
    from path.to.sample_textarea.forms import SampleTextareaForm

Defining the Sample textarea plugin.

.. code-block:: python

    class SampleTextareaPlugin(FormFieldPlugin):
        """Sample textarea plugin."""

        uid = "sample_textarea"
        name = "Sample Textarea"
        form = SampleTextareaForm
        group = "Samples" # Group to which the plugin belongs to

        def get_form_field_instances(self,
                                     request=None,
                                     form_entry=None,
                                     form_element_entries=None,
                                     **kwargs):
            kwargs = {
                'required': self.data.required,
                'label': self.data.label,
                'initial': self.data.initial,
                'widget': forms.widgets.Textarea(attrs={})
            }

            return [(self.data.name, forms.CharField, kwargs),]

Registering the ``SampleTextareaPlugin`` plugin.

.. code-block:: python

    form_element_plugin_registry.register(SampleTextareaPlugin)

Note, that in case you want to define a pure presentational element, make use
of ``fobi.base.FormElementPlugin`` for subclassing, instead of
``fobi.base.FormFieldPlugin``.
See the source of the content plugins
(fobi.contrib.plugins.form_elements.content) as a an example.

For instance, the ``captcha`` and ``honeypot`` fields are implemented
as form elements (subclasses the ``fobi.base.FormElementPlugin``). The
``db_store`` form handler plugin does not save the form data of
those elements. If you want the form element data to be saved, do inherit
from ``fobi.base.FormFieldPlugin``.

Hidden form element plugins, should be also having set the ``is_hidden``
property to True. By default it's set to False. That makes the hidden
form elements to be rendered using as ``django.forms.widgets.TextInput``
widget in edit mode. In the view mode, the original widget that you
assigned in your form element plugin would be used.

There might be cases, when you need to do additional handling of the data upon
the successful form submission. In such cases, you will need to define a
``submit_plugin_form_data`` method in the plugin, which accepts the
following arguments:

- `form_entry` (fobi.models.FormEntry): Form entry, which is being submitted.
- `request` (django.http.HttpRequest): The Django HTTP request.
- `form` (django.forms.Form): Form object (a valid one, which contains
  the ``cleaned_data`` attribute).
- `form_element_entries` (fobi.models.FormElementEntry): Form element entries
  for the `form_entry` given.
- (**)kwargs : Additional arguments.

Example (taken from fobi.contrib.plugins.form_elements.fields.file):

.. code-block:: python

    def submit_plugin_form_data(self,
                                form_entry,
                                request,
                                form,
                                form_element_entries=None,
                                **kwargs):
        """Submit plugin form data."""
        # Get the file path
        file_path = form.cleaned_data.get(self.data.name, None)
        if file_path:
            # Handle the upload
            saved_file = handle_uploaded_file(FILES_UPLOAD_DIR, file_path)
            # Overwrite ``cleaned_data`` of the ``form`` with path to moved
            # file.
            form.cleaned_data[self.data.name] = "{0}{1}".format(
                settings.MEDIA_URL, saved_file
            )

        # It's critically important to return the ``form`` with updated
        # ``cleaned_data``
        return form

In the example below, the original form is being modified. If you don't want
the original form to be modified, do not return anything.

Check the file form element plugin
(fobi.contrib.plugins.form_elements.fields.file) for complete example.

path/to/sample_textarea/forms.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Why to have another file for defining forms? Just to keep the code clean and
less messy, although you could perfectly define all your plugin forms in the
module ``fobi_form_elements.py``, it's recommended to keep it separate.

Take into consideration, that ``forms.py`` is not an auto-discovered file
pattern. All your form element plugins should be registered in modules named
``fobi_form_elements.py``.

Required imports.

.. code-block:: python

    from django import forms
    from fobi.base import BasePluginForm

Form for for ``SampleTextareaPlugin`` form element plugin.

.. code-block:: python

    class SampleTextareaForm(forms.Form, BasePluginForm):
        """Sample textarea form."""

        plugin_data_fields = [
            ("name", ""),
            ("label", ""),
            ("initial", ""),
            ("required", False)
        ]

        name = forms.CharField(label="Name", required=True)
        label = forms.CharField(label="Label", required=True)
        initial = forms.CharField(label="Initial", required=False)
        required = forms.BooleanField(label="Required", required=False)

Note that although it's not being checked in the code, but for form
field plugins the following fields should be present in the plugin
form (``BasePluginForm``) and the form plugin (``FormFieldPlugin``):

- name

In some cases, you might want to do something with the data
before it gets saved. For that purpose, ``save_plugin_data`` method
has been introduced.

See the following `example
<https://github.com/barseghyanartur/django-fobi/blob/stable/src/fobi/contrib/plugins/form_elements/content/content_image/forms.py>`_.

.. code-block:: python

    def save_plugin_data(self, request=None):
        """Saving the plugin data and moving the file."""
        file_path = self.cleaned_data.get('file', None)
        if file_path:
            saved_image = handle_uploaded_file(IMAGES_UPLOAD_DIR, file_path)
            self.cleaned_data['file'] = saved_image

path/to/sample_textarea/widgets.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Required imports.

.. code-block:: python

    from fobi.base import FormElementPluginWidget

Defining the base plugin widget.

.. code-block:: python

    class BaseSampleTextareaPluginWidget(FormElementPluginWidget):
        """Base sample textarea plugin widget."""

        # Same as ``uid`` value of the ``SampleTextareaPlugin``.
        plugin_uid = "sample_textarea"

path/to/sample_layout/fobi_form_elements.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Register in the registry (in some module which is for sure to be loaded; it's
handy to do it in the theme module).

Required imports.

.. code-block:: python

    from fobi.base import form_element_plugin_widget_registry
    from path.to.sample_textarea.widgets import BaseSampleTextareaPluginWidget

Define the theme specific plugin.

.. code-block:: python

    class SampleTextareaPluginWidget(BaseSampleTextareaPluginWidget):
        """Sample textarea plugin widget."""

        theme_uid = 'bootstrap3' # Theme for which the widget is loaded
        media_js = [
            'sample_layout/js/fobi.plugins.form_elements.sample_textarea.js',
        ]
        media_css = [
            'sample_layout/css/fobi.plugins.form_elements.sample_textarea.css',
        ]

Register the widget.

.. code-block:: python

    form_element_plugin_widget_registry.register(SampleTextareaPluginWidget)

Form element plugin final steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now, that everything is ready, make sure your plugin module is added to
``INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'path.to.sample_textarea',
        # ...
    )

Afterwards, go to terminal and type the following command.

.. code-block:: sh

    ./manage.py fobi_sync_plugins

If your HTTP server is running, you would then be able to see the new plugin
in the edit form interface.

Dashboard URL: http://127.0.0.1:8000/fobi/

Note, that you have to be logged in, in order to use the dashboard. If your
new plugin doesn't appear, set the ``FOBI_DEBUG`` to True in your Django's
local settings module, re-run your code and check console for error
notifications.

Creating a new form handler plugin
==================================
Form handler plugins handle the form data. `django-fobi` comes with several
bundled form handler plugins, among which is the ``db_store`` and ``mail``
plugins, which are responsible for saving the submitted form data into the
database and mailing the data to recipients specified. Number of form handlers
in a form is not limited. Certain form handlers are not configurable (for
example the ``db_store`` form handler isn't), while others are (``mail``,
``http_repost``).

You should see a form handler as a Django micro app, which could have its' own
models, admin interface, etc.

By default, it's possible to use a form handler plugin multiple times per form.
If you wish to allow form handler plugin to be used only once in a form,
set the ``allow_multiple`` property of the plugin to False.

As said above, `django-fobi` comes with several bundled form handler plugins.
Do check the source code as example.

Define and register the form handler plugin
-------------------------------------------
Let's name that plugin ``sample_mail``. The plugin directory should then have
the following structure.

.. code-block:: text

    path/to/sample_mail/
    ├── __init__.py
    ├── fobi_form_handlers.py  # Where plugins are defined and registered
    └── forms.py  # Plugin configuration form

Form handler plugins should be registered in "fobi_form_handlers.py" file.
Each plugin module should be put into the ``INSTALLED_APPS`` of your Django
projects' settings.

path/to/sample_mail/fobi_form_handlers.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A single form handler plugin is registered by its' UID.

Required imports.

.. code-block:: python

    import json
    from django.core.mail import send_mail
    from fobi.base import FormHandlerPlugin, form_handler_plugin_registry
    from path.to.sample_mail.forms import SampleMailForm

Defining the Sample mail handler plugin.

.. code-block:: python

    class SampleMailHandlerPlugin(FormHandlerPlugin):
        """Sample mail handler plugin."""

        uid = "sample_mail"
        name = _("Sample mail")
        form = SampleMailForm

        def run(self, form_entry, request, form):
            """To be executed by handler."""
            send_mail(
                self.data.subject,
                json.dumps(form.cleaned_data),
                self.data.from_email,
                [self.data.to_email],
                fail_silently=True
            )

Some form handlers are configurable, some others not. In order to
have a user friendly way of showing the form handler settings, what's
sometimes needed, a ``plugin_data_repr`` method has been introduced.
Simplest implementation of it would look as follows:

.. code-block:: python

    def plugin_data_repr(self):
        """Human readable representation of plugin data.

        :return string:
        """
        return self.data.__dict__

path/to/sample_mail/forms.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If plugin is configurable, it has configuration data. A single form may have
unlimited number of same plugins. Imagine, you want to have different subjects
and additional body texts for different user groups. You could then assign two
form handler ``mail`` plugins to the form. Of course, saving the posted form
data many times does not make sense, but it's up to the user. So, in case if
plugin is configurable, it should have a form.

Why to have another file for defining forms? Just to keep the code clean and
less messy, although you could perfectly define all your plugin forms in the
module ``fobi_form_handlers.py``, it's recommended to keep it separate.

Take into consideration, that ``forms.py`` is not an auto-discovered file
pattern. All your form handler plugins should be registered in modules named
``fobi_form_handlers.py``.

Required imports.

.. code-block:: python

    from django import forms
    from django.utils.translation import ugettext_lazy as _
    from fobi.base import BasePluginForm

Defining the form for Sample mail handler plugin.

.. code-block:: python

    class MailForm(forms.Form, BasePluginForm):
        """Mail form."""

        plugin_data_fields = [
            ("from_name", ""),
            ("from_email", ""),
            ("to_name", ""),
            ("to_email", ""),
            ("subject", ""),
            ("body", ""),
        ]

        from_name = forms.CharField(label=_("From name"), required=True)
        from_email = forms.EmailField(label=_("From email"), required=True)
        to_name = forms.CharField(label=_("To name"), required=True)
        to_email = forms.EmailField(label=_("To email"), required=True)
        subject = forms.CharField(label=_("Subject"), required=True)
        body = forms.CharField(
            label=_("Body"),
            required=False,
            widget=forms.widgets.Textarea
        )

After the plugin has been processed, all its' data is available in a
``plugin_instance.data`` container (for example,
``plugin_instance.data.subject`` or ``plugin_instance.data.from_name``).

Prioritise the execution order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Some form handlers shall be executed prior others. A good example of such, is
a combination of "mail" and "db_save" form handlers for the form. In case if
large files are posted, submission of form data would fail if "mail" plugin
would be executed after "db_save" has been executed. That's why it's possible
to prioritise that ordering in a ``FOBI_FORM_HANDLER_PLUGINS_EXECUTION_ORDER``
setting variable.

If not specified or left empty, form handler plugins would be ran in the order
of discovery. All form handler plugins that are not listed in the
``FORM_HANDLER_PLUGINS_EXECUTION_ORDER``, would be ran after the plugins that
are mentioned there.

.. code-block:: python

    FORM_HANDLER_PLUGINS_EXECUTION_ORDER = (
        'http_repost',
        'mail',
        # The 'db_store' is left out intentionally, since it should
        # be the last plugin to be executed.
    )

Form handler plugin custom actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
By default, a single form handler plugin has at least a "delete" action.
If plugin is configurable, it gets an "edit" action as well.

For some of your plugins, you may want to register a custom action. For
example, the "db_store" plugin does have one, for showing a link to
a listing page with saved form data for the form given.

For such cases, define a ``custom_actions`` method in your form handler
plugin. That method shall return a list of triples. In each triple,
first value is the URL, second value is the title and the third value
is the icon of the URL.

The following example is taken from the "db_store" plugin.

.. code-block:: python

    def custom_actions(self):
        """Adding a link to view the saved form entries.

        :return iterable:
        """
        return (
            (
                reverse('fobi.contrib.plugins.form_handlers.db_store.view_saved_form_data_entries'),
                _("View entries"),
                'glyphicon glyphicon-list'
            ),
        )

Form handler plugin final steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Do not forget to add the form handler plugin module to ``INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'path.to.sample_mail',
        # ...
    )

Afterwards, go to terminal and type the following command.

.. code-block:: sh

    ./manage.py fobi_sync_plugins

If your HTTP server is running, you would then be able to see the new plugin
in the edit form interface.

Creating a new form importer plugin
===================================
Form importer plugins import the forms from some external data source into
`django-fobi` form format. Number of form importers is not limited. Form
importers are implemented in forms of wizards (since they may contain several
steps).

You should see a form importer as a Django micro app, which could have its' own
models, admin interface, etc.

At the moment `django-fobi` comes with only one bundled form handler plugin,
which is the ``mailchimp_importer``, which is responsible for importing
existing MailChimp forms into `django-fobi`.

Define and register the form importer plugin
--------------------------------------------
Let's name that plugin ``sample_importer``. The plugin directory should then
have the following structure.

.. code-block:: text

    path/to/sample_importer/
    ├── templates
    │   └── sample_importer
    │       ├── 0.html
    │       └── 1.html
    ├── __init__.py
    ├── fobi_form_importers.py # Where plugins are defined and registered
    ├── forms.py # Wizard forms
    └── views.py # Wizard views

Form importer plugins should be registered in "fobi_form_importers.py" file.
Each plugin module should be put into the ``INSTALLED_APPS`` of your Django
projects' settings.

path/to/sample_importer/fobi_form_importers.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A single form importer plugin is registered by its' UID.

Required imports.

.. code-block:: python

    from django.utils.translation import ugettext_lazy as _
    from fobi.form_importers import BaseFormImporter, form_importer_plugin_registry
    from fobi.contrib.plugins.form_elements import fields
    from path.to.sample_importer.views import SampleImporterWizardView

Defining the Sample importer plugin.

.. code-block:: python

    class SampleImporterPlugin(FormHandlerPlugin):
        """Sample importer plugin."""

        uid = 'sample_importer'
        name = _("Sample importer")
        wizard = SampleImporterWizardView
        templates = [
            'sample_importer/0.html',
            'sample_importer/1.html',
        ]

        # field_type (at importer): uid (django-fobi)
        fields_mapping = {
            # Implemented
            'email': fields.email.UID,
            'text': fields.text.UID,
            'number': fields.integer.UID,
            'dropdown': fields.select.UID,
            'date': fields.date.UID,
            'url': fields.url.UID,
            'radio': fields.radio.UID,

            # Transformed into something else
            'address': fields.text.UID,
            'zip': fields.text.UID,
            'phone': fields.text.UID,
        }

        # Django standard: remote
        field_properties_mapping = {
            'label': 'name',
            'name': 'tag',
            'help_text': 'helptext',
            'initial': 'default',
            'required': 'req',
            'choices': 'choices',
        }

        field_type_prop_name = 'field_type'
        position_prop_name = 'order'

        def extract_field_properties(self, field_data):
            field_properties = {}
            for prop, val in self.field_properties_mapping.items():
                if val in field_data:
                    if 'choices' == val:
                        field_properties[prop] = "\n".join(field_data[val])
                    else:
                        field_properties[prop] = field_data[val]
            return field_properties


    form_importer_plugin_registry.register(SampleImporter)

path/to/sample_importer/forms.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
As mentioned above, form importers are implemented in form of wizards. The
forms are the wizard steps.

Required imports.

.. code-block:: python

    from django import forms
    from django.utils.translation import ugettext_lazy as _
    from sample_service_api import sample_api  # Just an imaginary API client

Defining the form for Sample importer plugin.

.. code-block:: python

    class SampleImporterStep1Form(forms.Form):
        """First form the the wizard."""

        api_key = forms.CharField(required=True)


    class SampleImporterStep2Form(forms.Form):
        """Second form of the wizard."""

        list_id = forms.ChoiceField(required=True, choices=[])

        def __init__(self, *args, **kwargs):
            self._api_key = None

            if 'api_key' in kwargs:
                self._api_key = kwargs.pop('api_key', None)

            super(SampleImporterStep2Form, self).__init__(*args, **kwargs)

            if self._api_key:
                client = sample_api.Api(self._api_key)
                lists = client.lists.list()
                choices = [(l['id'], l['name']) for l in lists['data']]
                self.fields['list_id'].choices = choices

path/to/sample_importer/views.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The wizard views.

Required imports.

.. code-block:: python

    from sample_service_api import sample_api  # Just an imaginary API client

    from django.shortcuts import redirect
    from django.core.urlresolvers import reverse
    from django.contrib import messages
    from django.utils.translation import ugettext_lazy as _

    # For django LTE 1.8 import from `django.contrib.formtools.wizard.views`
    from formtools.wizard.views import SessionWizardView

    from path.to.sample_importer.forms import (
        SampleImporterStep1Form,
        SampleImporterStep2Form,
    )

Defining the wizard view for Sample importer plugin.

.. code-block:: python

    class SampleImporterWizardView(SessionWizardView):
        """Sample importer wizard view."""

        form_list = [SampleImporterStep1Form, SampleImporterStep2Form]

        def get_form_kwargs(self, step):
            """Get form kwargs (to be used internally)."""
            if '1' == step:
                data = self.get_cleaned_data_for_step('0') or {}
                api_key = data.get('api_key', None)
                return {'api_key': api_key}
            return {}

        def done(self, form_list, **kwargs):
            """After all forms are submitted."""
            # Merging cleaned data into one dict
            cleaned_data = {}
            for form in form_list:
                cleaned_data.update(form.cleaned_data)

            # Connecting to sample client API
            client = sample_client.Api(cleaned_data['api_key'])

            # Fetching the form data
            form_data = client.lists.merge_vars(
                id={'list_id': cleaned_data['list_id']}
            )

            # We need the first form only
            try:
                form_data = form_data['data'][0]
            except Exception as err:
                messages.warning(
                    self.request,
                    _('Selected form could not be imported due errors.')
                )
                return redirect(reverse('fobi.dashboard'))

            # Actually, import the form
            form_entry = self._form_importer.import_data(
                {'name': form_data['name'], 'user': self.request.user},
                form_data['merge_vars']
            )

            redirect_url = reverse(
                'fobi.edit_form_entry',
                kwargs={'form_entry_id': form_entry.pk}
            )

            messages.info(
                self.request,
                _('Form {0} imported successfully.').format(form_data['name'])
            )

            return redirect("{0}".format(redirect_url))

Form importer plugin final steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Do not forget to add the form importer plugin module to ``INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'path.to.sample_importer',
        # ...
    )

Afterwards, go to terminal and type the following command.

.. code-block:: sh

    ./manage.py fobi_sync_plugins

If your HTTP server is running, you would then be able to see the new plugin
in the dashboard form interface (implemented in all bundled themes).

Creating a form callback
========================
Form callbacks are additional hooks, that are executed on various stages of
the form submission.

Let's place the callback in the ``foo`` module. The plugin directory should
then have the following structure.

.. code-block:: text

    path/to/foo/
    ├── __init__.py
    └── fobi_form_callbacks.py # Where callbacks are defined and registered

See the callback example below.

Required imports.

.. code-block:: python

    from fobi.constants import (
        CALLBACK_BEFORE_FORM_VALIDATION,
        CALLBACK_FORM_VALID_BEFORE_SUBMIT_PLUGIN_FORM_DATA,
        CALLBACK_FORM_VALID, CALLBACK_FORM_VALID_AFTER_FORM_HANDLERS,
        CALLBACK_FORM_INVALID
    )
    from fobi.base import FormCallback, form_callback_registry

Define and register the callback

.. code-block:: python

    class SampleFooCallback(FormCallback):
        """Sample foo callback."""

        stage = CALLBACK_FORM_VALID

        def callback(self, form_entry, request, form):
            """Define your callback code here."""
            print("Great! Your form is valid!")

    form_callback_registry.register(SampleFooCallback)

Add the callback module to ``INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'path.to.foo',
        # ...
    )

Suggestions
===========
Custom action for the form
--------------------------
Sometimes, you would want to specify a different action for the form.
Although it's possible to define a custom form action (``action`` field
in the "Form properties" tab), you're advised to use the ``http_repost``
plugin instead, since then the form would be still validated locally
and only then the valid data, as is, would be sent to the desired
endpoint.

Take in mind, that if both cases, if CSRF protection is enabled on
the endpoint, your post request would result an error.

When you want to customise too many things
------------------------------------------
`django-fobi`, with its' flexible form elements, form handlers and form
callbacks is very customisable. However, there might be cases when you need to
override entire view to fit your needs. Take a look at the
`FeinCMS integration
<https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/apps/feincms_integration/widgets.py>`_
or `DjangoCMS integration
<https://github.com/barseghyanartur/django-fobi/blob/stable/src/fobi/contrib/apps/djangocms_integration/cms_plugins.py>`_
as a good example of such. You may also want to compare the code from original
view ``fobi.views.view_form_entry`` with the code from the widget to get a
better idea of what could be changed in your case. If need a good advice,
just ask me.

Theming
=======
`django-fobi` comes with theming API. While there are several ready-to-use
themes:

- "Bootstrap 3" theme
- "Foundation 5" theme
- "Simple" theme in (with editing interface in style of the Django admin)
- "DjangoCMS admin style" theme (which is another simple theme with editing
  interface in style of ``djangocms-admin-style``)

Obviously, there are two sorts of views when it comes to editing and viewing
the form.

- The "view-view", when the form as it has been made is exposed to the
  site end- users/visitors.
- The "edit-view" (builder view), where the authorised users build their forms.

Both "Bootstrap 3" and "Foundation 5" themes are making use of the same style
for both "view-view" and "edit-view" views.

Both "Simple" and "DjangoCMS admin style" themes are styling for the
"edit-view" only. The "view-view" is pretty much blank, as shown on the one
of the screenshots [2.6]_.

Have in mind, that creating a brand new theme could be time consuming.
Instead, you are advised to extend existing themes or in the worst case,
if too much customisation required, create your own themes based on
existing ones (just copy the desired theme to your project directory and
work it out further).

It's possible to use different templates for all "view" and "edit"
actions (see the source code of the "simple" theme). Both "Bootstrap 3" and
"Foundation 5" themes look great. Although if you can't use any of those,
the "Simple" theme is the best start, since it looks just like django-admin.

Create a new theme
------------------

Let's place the theme in the ``sample_theme`` module. The theme directory
should then have the following structure.

.. code-block:: text

    path/to/sample_theme/
    ├── static
    │   ├── css
    │   │   └── sample_theme.css
    │   └── js
    │       └── sample_theme.js
    ├── templates
    │   └── sample_theme
    │       ├── _base.html
    │       ├── add_form_element_entry.html
    │       ├── ...
    │       └── view_form_entry_ajax.html
    ├── __init__.py
    ├── fobi_form_elements.py
    └── fobi_themes.py # Where themes are defined and registered

See the theme example below.

.. code-block:: python

    from django.utils.translation import ugettext_lazy as _

    from fobi.base import BaseTheme, theme_registry

    class SampleTheme(BaseTheme):
        """Sample theme."""

        uid = 'sample'
        name = _("Sample")

        media_css = (
            'sample_theme/css/sample_theme.css',
            'css/fobi.core.css',
        )

        media_js = (
            'js/jquery-1.10.2.min.js',
            'jquery-ui/js/jquery-ui-1.10.3.custom.min.js',
            'js/jquery.slugify.js',
            'js/fobi.core.js',
            'sample_theme/js/sample_theme.js',
        )

        # Form element specific
        form_element_html_class = 'form-control'
        form_radio_element_html_class = 'radio'
        form_element_checkbox_html_class = 'checkbox'

        form_edit_form_entry_option_class = 'glyphicon glyphicon-edit'
        form_delete_form_entry_option_class = 'glyphicon glyphicon-remove'
        form_list_container_class = 'list-inline'

        # Templates
        master_base_template = 'sample_theme/_base.html'
        base_template = 'sample_theme/base.html'

        form_ajax = 'sample_theme/snippets/form_ajax.html'
        form_snippet_template_name = 'sample_theme/snippets/form_snippet.html'
        form_properties_snippet_template_name = 'sample_theme/snippets/form_properties_snippet.html'
        messages_snippet_template_name = 'sample_theme/snippets/messages_snippet.html'

        add_form_element_entry_template = 'sample_theme/add_form_element_entry.html'
        add_form_element_entry_ajax_template = 'sample_theme/add_form_element_entry_ajax.html'

        add_form_handler_entry_template = 'sample_theme/add_form_handler_entry.html'
        add_form_handler_entry_ajax_template = 'sample_theme/add_form_handler_entry_ajax.html'

        create_form_entry_template = 'sample_theme/create_form_entry.html'
        create_form_entry_ajax_template = 'bootstrap3/create_form_entry_ajax.html'

        dashboard_template = 'sample_theme/dashboard.html'

        edit_form_element_entry_template = 'sample_theme/edit_form_element_entry.html'
        edit_form_element_entry_ajax_template = 'sample_theme/edit_form_element_entry_ajax.html'

        edit_form_entry_template = 'sample_theme/edit_form_entry.html'
        edit_form_entry_ajax_template = 'sample_theme/edit_form_entry_ajax.html'

        edit_form_handler_entry_template = 'sample_theme/edit_form_handler_entry.html'
        edit_form_handler_entry_ajax_template = 'sample_theme/edit_form_handler_entry_ajax.html'

        form_entry_submitted_template = 'sample_theme/form_entry_submitted.html'
        form_entry_submitted_ajax_template = 'sample_theme/form_entry_submitted_ajax.html'

        view_form_entry_template = 'sample_theme/view_form_entry.html'
        view_form_entry_ajax_template = 'sample_theme/view_form_entry_ajax.html'

Registering the ``SampleTheme`` plugin.

.. code-block:: python

    theme_registry.register(SampleTheme)

Sometimes you would want to attach additional properties to the theme
in order to use them later in templates (remember, current theme object
is always available in templates under name ``fobi_theme``).

For such cases you would need to define a variable in your project's settings
module, called ``FOBI_CUSTOM_THEME_DATA``. See the following code as example:

.. code-block:: python

    # `django-fobi` custom theme data for to be displayed in third party apps
    # like `django-registraton`.
    FOBI_CUSTOM_THEME_DATA = {
        'bootstrap3': {
            'page_header_html_class': '',
            'form_html_class': 'form-horizontal',
            'form_button_outer_wrapper_html_class': 'control-group',
            'form_button_wrapper_html_class': 'controls',
            'form_button_html_class': 'btn',
            'form_primary_button_html_class': 'btn-primary pull-right',
        },
        'foundation5': {
            'page_header_html_class': '',
            'form_html_class': 'form-horizontal',
            'form_button_outer_wrapper_html_class': 'control-group',
            'form_button_wrapper_html_class': 'controls',
            'form_button_html_class': 'radius button',
            'form_primary_button_html_class': 'btn-primary',
        },
        'simple': {
            'page_header_html_class': '',
            'form_html_class': 'form-horizontal',
            'form_button_outer_wrapper_html_class': 'control-group',
            'form_button_wrapper_html_class': 'submit-row',
            'form_button_html_class': 'btn',
            'form_primary_button_html_class': 'btn-primary',
        }
    }

You would now be able to access the defined extra properties in templates
as shown below.

.. code-block:: html

    <div class="{{ fobi_theme.custom_data.form_button_wrapper_html_class }}">

You likely would want to either remove the footer text or change it. Define
a variable in your project's settings module, called ``FOBI_THEME_FOOTER_TEXT``.
See the following code as example:

.. code-block:: python

    FOBI_THEME_FOOTER_TEXT = gettext('&copy; django-fobi example site 2014')

Below follow the properties of the theme:

- ``base_edit``
- ``base_view``

There are generic templates made in order to simplify theming. Some
of them you would never need to override. Some others, you would likely
want to.

Templates that you likely would want to re-write in your custom
theme implementation are marked with three asterisks (\*\*\*):

.. code-block:: text

    generic
    ├── snippets
    │   ├── form_ajax.html
    │   ├── form_edit_ajax.html
    │   ├── *** form_properties_snippet.html
    │   ├── *** form_snippet.html
    │   ├── --- form_edit_snippet.html (does not exist in generic templates)
    │   ├── --- form_view_snippet.html (does not exist in generic templates)
    │   ├── form_view_ajax.html
    │   └── messages_snippet.html
    │
    ├── _base.html
    ├── add_form_element_entry.html
    ├── add_form_element_entry_ajax.html
    ├── add_form_handler_entry.html
    ├── add_form_handler_entry_ajax.html
    ├── base.html
    ├── create_form_entry.html
    ├── create_form_entry_ajax.html
    ├── *** dashboard.html
    ├── edit_form_element_entry.html
    ├── edit_form_element_entry_ajax.html
    ├── edit_form_entry.html
    ├── *** edit_form_entry_ajax.html
    ├── edit_form_handler_entry.html
    ├── edit_form_handler_entry_ajax.html
    ├── form_entry_submitted.html
    ├── *** form_entry_submitted_ajax.html
    ├── *** theme.html
    ├── view_form_entry.html
    └── view_form_entry_ajax.html

From all of the templates listed above, the _base.html template is
the most influenced by the Bootstrap 3 theme.

Make changes to an existing theme
---------------------------------
As said above, making your own theme from scratch could be costly. Instead,
you can override/reuse an existing one and change it to your needs with
minimal efforts. See the `override simple theme
<https://github.com/barseghyanartur/django-fobi/tree/master/examples/simple/override_simple_theme/>`_
example. In order to see it in action, run the project with
`settings_override_simple_theme
<https://github.com/barseghyanartur/django-fobi/blob/master/examples/simple/settings_override_simple_theme.py>`_
option:

.. code-block:: sh

    ./manage.py runserver --settings=settings_override_simple_theme

Details explained below.

Directory structure
~~~~~~~~~~~~~~~~~~~
.. code-block:: text

    override_simple_theme/
    ├── static
    │   └── override_simple_theme
    │       ├── css
    │       │   └── override-simple-theme.css
    │       └── js
    │           └── override-simple-theme.js
    │
    ├── templates
    │   └── override_simple_theme
    │       ├── snippets
    │       │   └── form_ajax.html
    │       └── base_view.html
    ├── __init__.py
    └── fobi_themes.py # Where themes are defined and registered

fobi_themes.py
~~~~~~~~~~~~~~
Overriding the "simple" theme.

.. code-block:: python

    __all__ = ('MySimpleTheme',)

    from fobi.base import theme_registry

    from fobi.contrib.themes.simple.fobi_themes import SimpleTheme

    class MySimpleTheme(SimpleTheme):
        """My simple theme, inherited from `SimpleTheme` theme."""

        html_classes = ['my-simple-theme',]
        base_view_template = 'override_simple_theme/base_view.html'
        form_ajax = 'override_simple_theme/snippets/form_ajax.html'

Register the overridden theme. Note, that it's important to set the `force`
argument to True, in order to override the original theme. Force can be
applied only once (for an overridden element).

.. code-block:: python

    theme_registry.register(MySimpleTheme, force=True)

templates/override_simple_theme/base_view.html
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: html

    {% extends "simple/base_view.html" %}

    {% load static %}

    {% block stylesheets %}
    <link
      href="{% static 'override_simple_theme/css/override-simple-theme.css' %}"
      rel="stylesheet" media="all" />
    {% endblock stylesheets %}

    {% block main-wrapper %}
    <div id="sidebar">
      <h2>It's easy to override a theme!</h2>
    </div>

    {{ block.super }}
    {% endblock main-wrapper %}

templates/override_simple_theme/snippets/form_ajax.html
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: html

    {% extends "fobi/generic/snippets/form_ajax.html" %}

    {% block form_html_class %}basic-grey{% endblock %}

Form wizards
============
Basics
------
With form wizards you can split forms across multiple pages. State is
maintained in one of the backends (at the moment the Session backend). Data
processing is delayed until the submission of the final form.

In `django-fobi` wizards work in the following way:

- Number of forms in a form wizard is not limited.
- Form callbacks, handlers are totally ignored in form wizards. Instead,
  the form-wizard specific handlers (form wizard handlers) take over handling
  of the form data on the final step.

Bundled form wizard handler plugins
-----------------------------------
Below a short overview of the form wizard handler plugins. See the
README.rst file in directory of each plugin for details.

- `DB store
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_handlers/db_store/>`__:
  Stores form data in a database.
- `HTTP repost
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_handlers/http_repost/>`__:
  Repost the POST request to another endpoint.
- `Mail
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_handlers/mail/>`__:
  Send the form data by email.

Integration with third-party apps and frameworks
================================================
`django-fobi` has been successfully integrated into a number of diverse
third-party apps and frameworks, such as: Django REST framework, Django CMS,
FeinCMS, Mezzanine and Wagtail.

Certainly, integration into CMS is one case, integration into REST framework -
totally another. In REST frameworks we no longer have forms as such. Context
is very different. Handling of form data should obviously happen in a
different way. Assembling of the form class isn't enough (in case of Django
REST framework we assemble the serializer class).

In order to handle such level of integration, two additional sort of plugins
have been introduced:

- IntegrationFormElementPlugin
- IntegrationFormHandlerPlugin

These plugins are in charge of representation of the form elements in a
proper way for the package to be integrated and handling the submitted form
data.

`Additional documentation
<https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/apps/drf_integration/>`_
is available in the sub-package.

Sample `IntegrationFormElementPlugin`
-------------------------------------
Sample is taken from `here
<https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/apps/drf_integration/form_elements/fields/email/>`__.

base.py
~~~~~~~
Define the form element plugin.

.. code-block:: python

    from django.utils.translation import ugettext_lazy as _

    from rest_framework.fields import EmailField

    from fobi.base import IntegrationFormFieldPlugin
    from fobi.contrib.apps.drf_integration import UID as INTEGRATE_WITH_UID
    from fobi.contrib.apps.drf_integration.base import (
        DRFIntegrationFormElementPluginProcessor,
        DRFSubmitPluginFormDataMixin,
    )
    from fobi.contrib.apps.drf_integration.form_elements.fields.email import UID


    class EmailInputPlugin(IntegrationFormFieldPlugin,
                           DRFSubmitPluginFormDataMixin):
        """EmailField plugin."""

        uid = UID
        integrate_with = INTEGRATE_WITH_UID
        name = _("Decimal")
        group = _("Fields")

        def get_custom_field_instances(self,
                                       form_element_plugin,
                                       request=None,
                                       form_entry=None,
                                       form_element_entries=None,
                                       **kwargs):
            """Get form field instances."""
            field_kwargs = {
                'required': form_element_plugin.data.required,
                'initial': form_element_plugin.data.initial,
                'label': form_element_plugin.data.label,
                'help_text': form_element_plugin.data.help_text,
                'max_length': form_element_plugin.data.max_length,
            }
            return [
                DRFIntegrationFormElementPluginProcessor(
                    field_class=EmailField,
                    field_kwargs=field_kwargs
                )
            ]

fobi_integration_form_elements.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Register the plugin. Note the name pattern `fobi_integration_form_elements`.

.. code-block:: python

    from fobi.base import integration_form_element_plugin_registry
    from .base import EmailInputPlugin

    integration_form_element_plugin_registry.register(EmailInputPlugin)

Don't forget to list your plugin in the ``INSTALLED_APPS`` afterwards.

Sample `IntegrationFormHandlerPlugin`
-------------------------------------
Sample is taken from `here
<https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/apps/drf_integration/form_handlers/db_store/>`__.

base.py
~~~~~~~
Define the form handler plugin.

.. code-block:: python

    import logging
    from mimetypes import guess_type
    import os

    from django.conf import settings
    from django.utils.translation import ugettext_lazy as _

    from fobi.base import IntegrationFormHandlerPlugin
    from fobi.helpers import extract_file_path

    from fobi.contrib.apps.drf_integration import UID as INTEGRATE_WITH_UID
    from fobi.contrib.apps.drf_integration.base import get_processed_serializer_data

    from . import UID


    class MailHandlerPlugin(IntegrationFormHandlerPlugin):
        """Mail handler form handler plugin.

        Can be used only once per form.
        """

        uid = UID
        name = _("Mail")
        integrate_with = INTEGRATE_WITH_UID

        def run(self,
                form_handler_plugin,
                form_entry,
                request,
                form_element_entries=None,
                **kwargs):
            """Run."""
            base_url = form_handler_plugin.get_base_url(request)

            serializer = kwargs['serializer']

            # Clean up the values, leave our content fields and empty values.
            field_name_to_label_map, cleaned_data = get_processed_serializer_data(
                serializer,
                form_element_entries
            )

            rendered_data = form_handler_plugin.get_rendered_data(
                serializer.validated_data,
                field_name_to_label_map,
                base_url
            )

            files = self._prepare_files(request, serializer)

            form_handler_plugin.send_email(rendered_data, files)

        def _prepare_files(self, request, serializer):
            """Prepares the files for being attached to the mail message."""
            files = {}

            def process_path(file_path, imf):
                """Processes the file path and the file."""
                if file_path:
                    file_path = file_path.replace(
                        settings.MEDIA_URL,
                        os.path.join(settings.MEDIA_ROOT, '')
                    )
                    mime_type = guess_type(imf.name)
                    files[field_name] = (
                        imf.name,
                        ''.join([c for c in imf.chunks()]),
                        mime_type[0] if mime_type else ''
                    )

            for field_name, imf in request.FILES.items():
                try:
                    file_path = serializer.validated_data.get(field_name, '')
                    process_path(file_path, imf)
                except Exception as err:
                    file_path = extract_file_path(imf.name)
                    process_path(file_path, imf)

            return files

fobi_integration_form_handlers.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Register the plugin. Note the name pattern `fobi_integration_form_handlers`.

.. code-block:: python

    from fobi.base import integration_form_handler_plugin_registry
    from .base import MailHandlerPlugin

    integration_form_handler_plugin_registry.register(MailHandlerPlugin)

Don't forget to list your plugin in the ``INSTALLED_APPS`` afterwards.

Permissions
===========
Plugin system allows administrators to specify the access rights to every
plugin. `django-fobi` permissions are based on Django Users and User Groups.
Access rights are manageable via Django admin ("/admin/fobi/formelement/",
"/admin/fobi/formhandler/"). If user doesn't have the rights to access plugin,
it doesn't appear on his form even if has been added to it (imagine, you have
once granted the right to use the news plugin to all users, but later on
decided to limit it to Staff members group only). Note, that superusers have
access to all plugins.

.. code-block:: text

            Plugin access rights management interface in Django admin

    ┌──────────────────────────┬───────────────────────┬───────────────────────┐
    │ `Plugin`                 │ `Users`               │ `Groups`              │
    ├──────────────────────────┼───────────────────────┼───────────────────────┤
    │ Text                     │ John Doe              │ Form builder users    │
    ├──────────────────────────┼───────────────────────┼───────────────────────┤
    │ Textarea                 │                       │ Form builder users    │
    ├──────────────────────────┼───────────────────────┼───────────────────────┤
    │ File                     │ Oscar, John Doe       │ Staff members         │
    ├──────────────────────────┼───────────────────────┼───────────────────────┤
    │ URL                      │                       │ Form builder users    │
    ├──────────────────────────┼───────────────────────┼───────────────────────┤
    │ Hidden                   │                       │ Form builder users    │
    └──────────────────────────┴───────────────────────┴───────────────────────┘

Management commands
===================
There are several management commands available.

- `fobi_find_broken_entries`. Find broken form element/handler entries that
  occur when some plugin which did exist in the system, no longer exists.
- `fobi_sync_plugins`. Should be ran each time a new plugin is being added to
  the `django-fobi`.
- `fobi_update_plugin_data`. A mechanism to update existing plugin data in
  case if it had become invalid after a change in a plugin. In order for it
  to work, each plugin should implement and ``update`` method, in which the
  data update happens.

Tuning
======
There are number of `django-fobi` settings you can override in the settings
module of your Django project:

- `FOBI_RESTRICT_PLUGIN_ACCESS` (bool): If set to True, (Django) permission
  system for dash plugins is enabled. Defaults to True. Setting this to False
  makes all plugins available for all users.
- `FOBI_DEFAULT_THEME` (str): Active (default) theme UID. Defaults to
  "bootstrap3".
- `FORM_HANDLER_PLUGINS_EXECUTION_ORDER` (list of tuples): Order in which the
  form handlers are executed. See the "Prioritise the execution order"
  section for details.

For tuning of specific contrib plugin, see the docs in the plugin directory.

Bundled plugins and themes
==========================
`django-fobi` ships with number of bundled form element- and form handler-
plugins, as well as themes which are ready to be used as is.

Bundled form element plugins
----------------------------
Below a short overview of the form element plugins. See the README.rst file
in directory of each plugin for details.

Fields
~~~~~~
Fields marked with asterisk (*) fall under the definition of text elements.
It's possible to provide `Dynamic initial values`_ for text elements.

- `Boolean (checkbox)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/boolean/>`_
- `Date
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/date/>`_
- `DateTime
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/datetime/>`_
- `Date drop down (year, month, day selection drop-downs)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/date_drop_down/>`_
- `Decimal
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/decimal>`_
- `Duration
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/duration>`_
- `Email*
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/email/>`_
- `File
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/file/>`_
- `Float
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/float>`_
- `Hidden*
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/hidden/>`_
- `Input
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/input/>`_
- `IP address*
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/ip_address>`_
- `Integer
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/integer/>`_
- `Null boolean
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/null_boolean>`_
- `Password*
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/password/>`_
- `Radio select (radio button)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/radio/>`_
- `Range select
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/range_select/>`_
- `Select (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select/>`_
- `Select model object (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select_model_object/>`_
- `Select multiple (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select_multiple/>`_
- `Select multiple model objects (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select_multiple_model_objects/>`_
- `Slider
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/slider>`_
- `Slug*
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/slug>`_
- `Text*
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/text/>`_
- `Textarea*
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/textarea/>`_
- `Time
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/time>`_
- `URL*
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/url/>`_

Content/presentation
~~~~~~~~~~~~~~~~~~~~
Content plugins are presentational plugins, that make your forms look more
complete and content rich.

- `Content image
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/content/content_image/>`_:
  Insert an image.
- `Content image URL
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/content/content_image_url/>`_:
  Insert an image URL.
- `Content text
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/content/content_text/>`_:
  Add text.
- `Content richtext
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/content/content_richtext/>`_:
  Add rich text (based on `django-ckeditor <https://github.com/django-ckeditor/django-ckeditor>`_
  package).
- `Content markdown
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/content/content_markdown/>`_:
  Add markdown text.
- `Content video
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/content/content_video/>`_:
  Add an embed YouTube or Vimeo video.

Security
~~~~~~~~
- `CAPTCHA
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/security/captcha/>`__:
  CAPTCHA integration, requires ``django-simple-captcha`` package.
- `ReCAPTCHA
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/security/recaptcha/>`__:
  CAPTCHA integration, requires ``django-recaptcha`` package.
- `Invisible ReCAPTCHA
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/security/invisible_recaptcha/>`__:
  Google invisible reCAPTCHA integration, with no additional dependencies.
- `Honeypot
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/security/honeypot/>`__:
  `Anti-spam honeypot <http://en.wikipedia.org/wiki/Anti-spam_techniques#Honeypots>`_
  field.

MPTT fields
~~~~~~~~~~~
- `Select MPTT model object (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select_mptt_model_object/>`_
- `Select multiple MPTT model objects (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select_multiple_mptt_model_objects/>`_

Test
~~~~
Test plugins are made for dev purposes only.

- `Dummy
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/test/dummy/>`_:
  Solely for dev purposes.

Bundled form handler plugins
----------------------------
Below a short overview of the form handler plugins. See the README.rst file
in directory of each plugin for details.

- `DB store
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_handlers/db_store/>`__:
  Stores form data in a database.
- `HTTP repost
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_handlers/http_repost/>`__:
  Repost the POST request to another endpoint.
- `Mail
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_handlers/mail/>`__:
  Send the form data by email.

Bundled themes
--------------
Below a short overview of the themes. See the README.rst file in directory
of each theme for details.

- `Bootstrap 3
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/themes/bootstrap3/>`_:
  Bootstrap 3 theme.
- `Foundation 5
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/themes/foundation5/>`_:
  Foundation 5 theme.
- `Simple
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/themes/simple/>`_:
  Basic theme with form editing is in a style of Django admin.
- `DjangoCMS admin style
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/themes/djangocms_admin_style_theme/>`_:
  Basic theme with form editing is in a style of `djangocms-admin-style
  <https://github.com/divio/djangocms-admin-style>`_.

Third-party plugins and themes
==============================
List of remarkable third-party plugins:

- `fobi-phonenumber <https://pypi.python.org/pypi/fobi-phonenumber>`_ - A Fobi
  PhoneNumber form field plugin. Makes use of the
  `phonenumber_field.formfields.PhoneNumberField` and
  `phonenumber_field.widgets.PhoneNumberPrefixWidget`.

HTML5 fields
============
The following HTML5 fields are supported in corresponding bundled plugins:

- date
- datetime
- email
- max
- min
- number
- url
- placeholder
- type

With the ``fobi.contrib.plugins.form_elements.fields.input`` support for
HTML5 fields is extended to the following fields:

- autocomplete
- autofocus
- list
- multiple
- pattern
- step

Loading initial data using GET arguments
========================================
It's possible to provide initial data for the form using the GET arguments.

In that case, along with the field values, you should be providing
an additional argument named "fobi_initial_data", which doesn't have to
hold a value. For example, if your form contains of fields named "email" and
"age" and you want to provide initial values for those using GET arguments, you
should be constructing your URL to the form as follows:

http://127.0.0.1:8001/fobi/view/test-form/?fobi_initial_data&email=test@example.com&age=19

Dynamic initial values
======================
It's possible to provide a dynamic initial value for any of the text elements.
In order to do that, you should use the build-in context processor or make
your own one. The only requirement is that you should store all values that
should be exposed in the form as a dict for ``fobi_dynamic_values`` dictionary
key. Beware, that passing the original request object might be unsafe in
many ways. Currently, a stripped down version of the request object is being
passed as a context variable.

.. code-block:: python

    TEMPLATES = [
        {
            # ...
            'OPTIONS': {
                # ...
                'context_processors': [
                    # ...
                    "fobi.context_processors.theme",  # Important!
                    "fobi.context_processors.dynamic_values",  # Optional
                ]
            },
        },
    ]

.. code-block:: python

    def dynamic_values(request):
        return {
            'fobi_dynamic_values': {
                'request': StrippedRequest(request),
                'now': datetime.datetime.now(),
                'today': datetime.date.today(),
            }
        }

In your GUI, you should be referring to the initial values in the following
way:

.. code-block:: html

    {{ request.path }} {{ now }} {{ today }}

Note, that you should not provide the `fobi_dynamic_values.` as a prefix.
Currently, the following variables are available in the
`fobi.context_processors.dynamic_values` context processor:

.. code-block:: text

    - request: Stripped HttpRequest object.

        - request.path: A string representing the full path to the requested
          page, not including the scheme or domain.

        - request.get_full_path(): Returns the path, plus an appended query
          string, if applicable.

        - request.is_secure():  Returns True if the request is secure; that
          is, if it was made with HTTPS.

        - request.is_ajax(): Returns True if the request was made via an
          XMLHttpRequest, by checking the HTTP_X_REQUESTED_WITH header for the
          string 'XMLHttpRequest'.

        - request.META: A stripped down standard Python dictionary containing
          the available HTTP headers.

            - HTTP_ACCEPT_ENCODING: Acceptable encodings for the response.

            - HTTP_ACCEPT_LANGUAGE: Acceptable languages for the response.

            - HTTP_HOST: The HTTP Host header sent by the client.

            - HTTP_REFERER: The referring page, if any.

            - HTTP_USER_AGENT: The client’s user-agent string.

            - QUERY_STRING: The query string, as a single (un-parsed) string.

            - REMOTE_ADDR: The IP address of the client.

        - request.user: Authenticated user.

            - request.user.email:

            - request.user.get_username(): Returns the username for the user.
              Since the User model can be swapped out, you should use this
              method instead of referencing the username attribute directly.

            - request.user.get_full_name(): Returns the first_name plus the
              last_name, with a space in between.

            - request.user.get_short_name(): Returns the first_name.

            - request.user.is_anonymous():

    - now: datetime.datetime.now()

    - today: datetime.date.today()

Submitted form element plugins values
=====================================
While some values of form element plugins are submitted as is, some others
need additional processing. There are 3 types of behaviour taken into
consideration:

- "val": value is being sent as is.
- "repr": (human readable) representation of the value is used.
- "mix": mix of value as is and human readable representation.

The following plugins have been made configurable in such a way, that
developers can choose the desired behaviour in projects' settings:

- ``FOBI_FORM_ELEMENT_CHECKBOX_SELECT_MULTIPLE_SUBMIT_VALUE_AS``
- ``FOBI_FORM_ELEMENT_RADIO_SUBMIT_VALUE_AS``
- ``FOBI_FORM_ELEMENT_SELECT_SUBMIT_VALUE_AS``
- ``FOBI_FORM_ELEMENT_SELECT_MULTIPLE_SUBMIT_VALUE_AS``
- ``FOBI_FORM_ELEMENT_SELECT_MODEL_OBJECT_SUBMIT_VALUE_AS``
- ``FOBI_FORM_ELEMENT_SELECT_MULTIPLE_MODEL_OBJECTS_SUBMIT_VALUE_AS``

See the README.rst in each of the following plugins for more information.

- `Checkbox select multiple (multiple checkboxes)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/radio/>`__
- `Radio select (radio button)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/radio/>`__
- `Select (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select/>`__
- `Select model object (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select_model_object/>`__
- `Select MPTT model object (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select_mptt_model_object/>`__
- `Select multiple (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select_multiple/>`__
- `Select multiple model objects (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select_multiple_model_objects/>`__
- `Select multiple MPTT model objects (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select_multiple_mptt_model_objects/>`__

Rendering forms using third-party libraries
===========================================
You might want to render your forms using third-party libraries such as
`django-crispy-forms <http://django-crispy-forms.readthedocs.org/>`_,
`django-floppyforms <http://django-floppyforms.readthedocs.org/>`_ or
other alternatives.

For that purpose you should override the "snippets/form_snippet.html" used
by the theme you have chosen. Your template would then look similar to the
one below (make sure to setup/configure your third-party form rendering library
prior doing this).

Using `django-crispy-forms`
---------------------------

.. code-block:: html

    {% load crispy_forms_tags fobi_tags %}

    {% block form_non_field_and_hidden_errors %}
        {% get_form_hidden_fields_errors form as form_hidden_fields_errors %}
        {% if form.non_field_errors or form_hidden_fields_errors %}
            {% include fobi_theme.form_non_field_and_hidden_errors_snippet_template %}
        {% endif %}
    {% endblock form_non_field_and_hidden_errors %}

    {% crispy form %}

Using `django-floppyforms`
--------------------------

.. code-block:: html

    {% load floppyforms fobi_tags %}

    {% block form_non_field_and_hidden_errors %}
        {% get_form_hidden_fields_errors form as form_hidden_fields_errors %}
        {% if form.non_field_errors or form_hidden_fields_errors %}
            {% include fobi_theme.form_non_field_and_hidden_errors_snippet_template %}
        {% endif %}
    {% endblock form_non_field_and_hidden_errors %}

    {% form form %}

See how it's done in the `override simple theme
<https://github.com/barseghyanartur/django-fobi/tree/master/examples/simple/override_simple_theme/>`__
example.

Import/export forms
===================
There might be cases when you have `django-fobi` running on multiple instances
and have already spend some time on making forms on one of the instances,
and want to reuse those forms on another. You could of course re-create entire
form in the GUI, but we can do better than that. It's possible to export forms
into JSON format and import the exported forms again. It's preferable that
you run both instances on the same versions of `django-fobi`, otherwise imports
might break (although it might just work). There many ways to deal with
missing plugin errors, but the chosen strategy (which you don't yet have full
control of) is safest (import everything possible, but warn user about errors).
If both instances have the same set of form element and form handler plugins
imports should go smoothly. It is though possible to make an import ignoring
missing form element and form handler plugins. You would get an appropriate
notice about that, but import will continue leaving the broken plugin data out.

Translations
============
Available translations
----------------------
English is the primary language. The following translations are
available (core and plugins)

- `Dutch <https://django-fobi.herokuapp.com/nl/>`_
- `German <https://django-fobi.herokuapp.com/de/>`_
- `Russian <https://django-fobi.herokuapp.com/ru/>`_
- `French <https://django-fobi.herokuapp.com/fr/>`_

Overriding translations
-----------------------
There might be cases when you want to override certain translations. It's
easily achievable with introduction of custom locale paths in your project.

See the following as a good example of overriding some English plugin labels.

- `custom settings
  <https://raw.githubusercontent.com/barseghyanartur/django-fobi/master/examples/simple/settings/alternative_labels.py>`__
- `custom locales directory
  <https://github.com/barseghyanartur/django-fobi/tree/master/examples/simple/fobi_locale/>`__

Run the example project as follows:

.. code-block:: sh

    cd examples/simple/
    ./manage.py runserver --settings=settings.alternative_labels

In the example given, "Boolean" and "Checkbox select multiple" plugin names
are renamed to "Checkbox" and "Multiple checkboxes" respectively.

All built-in plugin ``name`` values are almost equivalent to the plugin ``uid``
values. By default plugins are sorted by ``uid`` value. When you override the
``name`` of the plugin, sorting breaks. Therefore, it's recommended to
set the ``FOBI_SORT_PLUGINS_BY_VALUE`` value to True in your settings module.
Default value is False, which means that plugins are sorted by their ``uid``
value.

.. code-block:: python

    FOBI_SORT_PLUGINS_BY_VALUE = True

Debugging
=========
By default debugging is turned off. It means that broken form entries, which
are entries with broken data, that are not possible to be shown, are just
skipped. That's safe in production. Although, you for sure would want to
see the broken entries in development. Set the ``FOBI_DEBUG`` to True
in the ``settings.py`` of your project in order to do so.

Most of the errors are logged (DEBUG). If you have written a plugin and it
somehow doesn't appear in the list of available plugins, do run the following
management command since it not only syncs your plugins into the database,
but also is a great way of checking for possible errors.

.. code-block:: sh

    ./manage.py fobi_sync_plugins

Run the following command in order to identify the broken plugins.

.. code-block:: sh

    ./manage.py fobi_find_broken_entries

If you have forms referring to form element- of form handler- plugins
that are currently missing (not registered, removed, failed to load - thus
there would be a risk that your form would't be rendered properly/fully and
the necessary data handling wouldn't happen either) you will get an
appropriate exception. Although it's fine to get an instant error message about
such failures in development, in production is wouldn't look appropriate.
Thus, there are two settings related to the non-existing (not-found) form
element- and form handler- plugins.

- FOBI_DEBUG: Set this to True in your development environment anyway. Watch
  error logs closely.
- FOBI_FAIL_ON_MISSING_FORM_ELEMENT_PLUGINS: If you want no error to be
  shown in case of missing form element plugins, set this to False in
  your settings module. Default value is True.
- FOBI_FAIL_ON_MISSING_FORM_HANDLER_PLUGINS: If you want no error to be
  shown in case of missing form element handlers, set this to False in
  your settings module. Default value is True.

Testing
=======
Project is covered by test (functional- and browser-tests).

.. note::

    You are recommended to use Postgres or MySQL for testing. Tests
    occasionally fail on SQLite due to very intensive IO and SQLite table
    locking.

To test with all supported Python/Django versions type:

.. code-block:: sh

    tox

To test against specific environment, type:

.. code-block:: sh

    tox -e py37-django21

To test just your working environment type:

.. code-block:: sh

    ./runtests.py

It's assumed that you have all the requirements installed. If not, first
install the test requirements:

.. code-block:: sh

    pip install -r examples/requirements/test.txt

Browser tests
-------------
For browser tests you may choose between Firefox, headless Firefox and
PhantomJS. PhantomJS is faster, headless Firefox is fast as well, but
normal Firefox tests tell you more (as you see what exactly happens on the
screen). Both cases require some effort and both have disadvantages regarding
the installation (although once you have them installed they work perfect).

Latest versions of Firefox are often not supported by Selenium. Current
version of the Selenium for Python (2.53.6) works fine with Firefox 47.
Thus, instead of using system Firefox you could better use a custom one.

For PhantomJS you need to have NodeJS installed.

Set up Firefox 47
~~~~~~~~~~~~~~~~~
1. Download Firefox 47 from
   `this
   <https://ftp.mozilla.org/pub/firefox/releases/47.0.1/linux-x86_64/en-GB/firefox-47.0.1.tar.bz2>`__
   location and unzip it into ``/usr/lib/firefox47/``

2. Specify the full path to your Firefox in ``FIREFOX_BIN_PATH``
   setting. Example:

   .. code-block:: python

       FIREFOX_BIN_PATH = '/usr/lib/firefox47/firefox'

   If you set to use system Firefox, remove or comment-out the
   ``FIREFOX_BIN_PATH`` setting.

After that your Selenium tests would work.

Set up headless Firefox
~~~~~~~~~~~~~~~~~~~~~~~
1. Install ``xvfb`` package which is used to start Firefox in headless mode.

   .. code-block:: sh

        sudo apt-get install xvfb

2. Run the tests using headless Firefox.

   .. code-block:: sh

        ./scripts/runtests.sh

   Or run tox tests using headless Firefox.

   .. code-block:: sh

        ./scripts/tox.sh

   Or run specific tox tests using headless Firefox.

   .. code-block:: sh

        ./scripts/tox.sh -e py36-django111

Setup PhantomJS
~~~~~~~~~~~~~~~
You could also run tests in headless mode (faster). For that you will need
PhantomJS.

1. Install PhantomJS and dependencies.

   .. code-block:: sh

       curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh
       sudo bash nodesource_setup.sh
       sudo apt-get install nodejs
       sudo apt-get install build-essential libssl-dev
       sudo npm -g install phantomjs-prebuilt

2. Specify the ``PHANTOM_JS_EXECUTABLE_PATH`` setting. Example:

   .. code-block:: python

       PHANTOM_JS_EXECUTABLE_PATH = ""

   If you want to use Firefox for testing, remove or comment-out the
   ``PHANTOM_JS_EXECUTABLE_PATH`` setting.

Writing documentation
=====================
Keep the following hierarchy.

.. code-block:: text

    =====
    title
    =====

    header
    ======

    sub-header
    ----------

    sub-sub-header
    ~~~~~~~~~~~~~~

    sub-sub-sub-header
    ##################

    sub-sub-sub-sub-header
    ^^^^^^^^^^^^^^^^^^^^^^

    sub-sub-sub-sub-sub-header
    ++++++++++++++++++++++++++

Troubleshooting
===============
If you get a ``FormElementPluginDoesNotExist`` or a
``FormHandlerPluginDoesNotExist`` exception, make sure you have listed your
plugin in the ``settings`` module of your project.

Contributing
============
If you want to contribute to the library, but don't know where to start,
do check the `open issues where help is appreciated
<https://github.com/barseghyanartur/django-fobi/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+appreciated%22>`_
or ask the `Author`_ how you could help.

License
=======
GPL 2.0/LGPL 2.1

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
