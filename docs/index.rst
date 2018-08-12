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



Screenshots
===========
Bootstrap3 theme
----------------
Dashboard
~~~~~~~~~
.. [1.1] Dashboard

.. image:: _static/bootstrap3/01_dashboard.png
    :scale: 80 %

Create a form
~~~~~~~~~~~~~
.. [1.2] Create a form

.. image:: _static/bootstrap3/02_create_form.png
    :scale: 80 %

View/edit form
~~~~~~~~~~~~~~
Form elements
#############
.. [1.3] Edit form - form elements tab active, no elements yet

.. image:: _static/bootstrap3/03_edit_form_-_form_elements_tab_active_-_no_elements_yet.png
    :scale: 80 %

.. [1.4] Edit form - form elements tab active, add a form element menu

.. image:: _static/bootstrap3/04_edit_form_-_form_elements_tab_active_-_add_element_menu.png
    :scale: 80 %

.. [1.5] Edit form - add a form element (URL plugin)

.. image:: _static/bootstrap3/05_edit_form_-_add_form_element_url_plugin.png
    :scale: 80 %

.. [1.6] Edit form - form elements tab active, with form elements

.. image:: _static/bootstrap3/06_edit_form_-_form_elements_tab_active_-_with_elements.png
    :scale: 80 %

Form handlers
#############

.. [1.7] Edit form - form handlers tab active, no handlers yet

.. image:: _static/bootstrap3/07_edit_form_-_form_handlers_tab_active_-_no_handlers_yet.png
    :scale: 80 %

.. [1.8] Edit form - form handlers tab tactive, add form handler menu

.. image:: _static/bootstrap3/08_edit_form_-_form_handlers_tab_active_-_add_handler_menu.png
    :scale: 80 %

.. [1.9] Edit form - add a form handler (Mail plugin)

.. image:: _static/bootstrap3/09_edit_form_-_add_form_handler_mail_plugin.png
    :scale: 80 %

.. [1.10] Edit form - form handlers tab active, with form handlers

.. image:: _static/bootstrap3/10_edit_form_-_form_handlers_tab_active_with_handlers.png
    :scale: 80 %

.. [1.11] Edit form - form properties tab active

.. image:: _static/bootstrap3/11_edit_form_-_form_properties_tab_active.png
    :scale: 80 %

.. [1.12] View form

.. image:: _static/bootstrap3/12_view_form.png
    :scale: 80 %

.. [1.13] View form - form submitted (thanks page)

.. image:: _static/bootstrap3/13_view_form_-_form_submitted.png
    :scale: 80 %

.. [1.14] Edit form - add a form element (Video plugin)

.. image:: _static/bootstrap3/14_edit_form_-_add_form_element_video_plugin.png
    :scale: 80 %

.. [1.15] Edit form - add a form element (Boolean plugin)

.. image:: _static/bootstrap3/15_edit_form_-_add_form_element_boolean_plugin.png
    :scale: 80 %

.. [1.16] Edit form

.. image:: _static/bootstrap3/16_edit_form.png
    :scale: 80 %

.. [1.17] View form

.. image:: _static/bootstrap3/17_view_form.png
    :scale: 80 %

Simple theme
------------
View/edit form
~~~~~~~~~~~~~~
.. [2.1] Edit form - form elements tab active, with form elements

.. image:: _static/simple/01_edit_form_-_form_elements_tab_active_with_elements.png
    :scale: 80 %

.. [2.2] Edit form - form elements tab active, add a form element menu

.. image:: _static/simple/02_edit_form_-_form_elements_tab_active_add_elements_menu.png
    :scale: 80 %

.. [2.3] Edit form - add a form element (Hidden plugin)

.. image:: _static/simple/03_edit_form_-_add_form_element_hidden.png
    :scale: 80 %

.. [2.4] Edit form - form handlers tab active, with form handlers

.. image:: _static/simple/04_edit_form_-_form_handlers_tab_active_with_handlers.png
    :scale: 80 %

.. [2.5] Edit form - form properties tab active

.. image:: _static/simple/05_edit_form_-_form_properties_tab_active.png
    :scale: 80 %

.. [2.6] View form

.. image:: _static/simple/06_view_form.png
    :scale: 80 %



Documentation
=============
Contents:

.. toctree::
   :maxdepth: 20

   index
   quickstart
   changelog
   licenses
   fobi

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



(Sub)modules
============
Some additional documentation on ``django-fobi`` sub-modules are listed
below.


fobi.contrib.apps.djangocms_integration
---------------------------------------
A ``django-fobi`` integration with DjangoCMS.

Prerequisites
~~~~~~~~~~~~~
Tested with DjangoCMS 2.4.3, 3.0.6 and 3.4.3 only. Might work on earlier (or
later) versions as well.

Installation
~~~~~~~~~~~~
Versions
########
See the requirements files:

- `DjangoCMS 2.4.3 requirements
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/requirements/djangocms_2.txt>`_.
- `DjangoCMS 3.0.6 requirements
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/requirements/djangocms_3_0_6.txt>`_.
- `DjangoCMS 3.4.3 requirements
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/requirements/djangocms_3_4_3.txt>`_.

your_project/settings.py
########################
See the example settings files:

- `DjangoCMS 2.4.3 settings
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/simple/settings/bootstrap3_theme_djangocms_2.py>`_.
- `DjangoCMS 3.0.6/3.4.3. settings
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/simple/settings/bootstrap3_theme_djangocms.py>`_.

.. code-block:: python

    INSTALLED_APPS = list(INSTALLED_APPS)
    INSTALLED_APPS += [
        'cms',  # DjangoCMS

        'fobi.contrib.apps.djangocms_integration',  # Fobi DjangoCMS app
    ]

Information for developers
~~~~~~~~~~~~~~~~~~~~~~~~~~
Templates for DjangoCMS
#######################
Django-CMS templates are quite specific and in some aspects are not 100%
compatible with built-in themes (due to the fact that DjangoCMS intensively 
makes use of ``django-sekizai`` which isn't used in the generic templates).

That does not anyhow affect the core ``fobi`` and the built-in themes,
although you can't magically reuse built-in ``fobi`` themes with Django-CMS
(as it's done for `FeinCMS page templates
<https://github.com/barseghyanartur/django-fobi/blob/stable/examples/simple/templates/page/base.html>`_).

You would have to make custom page templates from scratch (or based on a
copy of the desired bundled template). See how I did it for all bundled themes
`here
<https://github.com/barseghyanartur/django-fobi/tree/stable/examples/simple/templates/cms_page>`_:

- `Bootstrap 3
  <https://github.com/barseghyanartur/django-fobi/tree/stable/examples/simple/templates/cms_page/bootstrap3>`_
- `Foundation 5
  <https://github.com/barseghyanartur/django-fobi/tree/stable/examples/simple/templates/cms_page/foundation5>`_
- `Simple
  <https://github.com/barseghyanartur/django-fobi/tree/stable/examples/simple/templates/cms_page/simple>`_

Template rendering
##################
The embed DjangoCMS widget is rendered with use of two theme templates:

- ``view_embed_form_entry_ajax_template``: Used for rendering the form.
- ``embed_form_entry_submitted_ajax_template``: Used for rendering the form
  sent event.

Using custom templates for rendering the widget
###############################################
In the widget, you can specify a template which you want to be used for
rendering the form or the form-sent event.

Example:

.. code-block:: python

    FOBI_DJANGOCMS_INTEGRATION_FORM_TEMPLATE_CHOICES = (
        ("yourapp/custom_view_embed_form_v1.html",
         "Custom embed form view template #1"),
        ("yourapp/custom_view_embed_form_v2.html",
         "Custom embed form view template #2"),
    )

Same goes for form-sent templates.

.. code-block:: python

    FOBI_DJANGOCMS_INTEGRATION_SUCCESS_PAGE_TEMPLATE_CHOICES = (
        ("yourapp/custom_embed_form_submitted_v1.html",
         "Custom form-sent template #1"),
        ("yourapp/custom_embed_form_submitted_v2.html",
         "Custom form-sent template #2"),
    )

Registering a template in the ``FORM_TEMPLATE_CHOICES`` makes it available
for all the themes. If you rather want to use different custom templates
for different themes, use the ``FOBI_CUSTOM_THEME_DATA`` as shown in the
example below.

.. code-block:: python

    FOBI_CUSTOM_THEME_DATA = {
        'bootstrap3': {
            'djangocms_integration': {
                'form_template_choices': [
                    ('fobi/bootstrap3_extras/view_embed_form.html',
                     "Custom bootstrap3 embed form view template"),
                ],
                'success_page_template_choices': [
                    ('fobi/bootstrap3_extras/embed_form_submitted.html',
                     "Custom bootstrap3 embed form entry submitted template"),
                ],
            },
        },
        'foundation5': {
            'djangocms_integration': {
                'form_template_choices': [
                    ('fobi/foundation5_extras/view_embed_form.html',
                     "Custom foundation5 embed form view template"),
                ],
                'success_page_template_choices': [
                    ('fobi/foundation5_extras/embed_form_submitted.html',
                     "Custom foundation5 embed form entry submitted template"),
                ],
            },
        },
    }

Usage
~~~~~
The ``fobi.contrib.apps.djangocms_integration.models.FobiFormWidget`` consists
of the following fields:

- Form: The form to be used.
- Form template name: Template to be used to render the embed form.
- Hide form title: If checked, no form title would be shown.
- Form title: Overrides the standard form title.
- Submit button text: Overrides the default submit button text.
- Success page template name: Template to be used to render the embed form-sent
  event.
- Hide success page title: If checked, no form-sent title would be shown.
- Success page title: Overrides the form-sent title.
- Success page text: Overrides the form-sent text.


fobi.contrib.apps.drf_integration
---------------------------------
A ``django-fobi`` integration with ``Django REST framework``.

Supported actions are:

- `LIST`_: List all the forms.
- `OPTIONS`_: Describe the given form.
- `PUT`_: Submit form data.

Live demo
~~~~~~~~~
Live demo is available on Heroku.

- `The core <https://django-fobi.herokuapp.com/>`_
- `Django REST framework integration <https://django-fobi.herokuapp.com/api/>`_

Supported fields
~~~~~~~~~~~~~~~~
The following fields are supported.

Content (presentational form elements)
######################################
Unlike standard fields, ``content`` fields are purely presentational.
You're not supposed to make write actions on them (it won't work). Neither
will they be displayed in the browsable API (list/retrieve actions). However,
they will be listed in the options action call. All content fields are of type
"content".

- content_image
- content_image_url
- content_richtext
- content_text
- content_video

Fields
######
- boolean
- checkbox_select_multiple
- date
- date_drop_down
- datetime
- decimal
- duration
- email
- file
- float
- hidden (in terms of the Django REST framework - a read-only field)
- input (some sort of a copy of ``text`` plugin)
- integer
- ip_address
- null_boolean
- password (some sort of a copy of ``text`` plugin)
- radio
- range_select
- regex
- select
- select_multiple
- select_multiple_with_max
- slider (just a copy of range_select, for compatibility with main package)
- slug
- text
- textarea (some sort of a copy of ``text`` plugin)
- time
- url

Not (yet) supported fields
~~~~~~~~~~~~~~~~~~~~~~~~~~
The following fields are not supported. Those marked with asterisk are planned
to be supported in the upcoming releases.

- select_model_object
- select_mptt_model_object
- select_multiple_model_objects
- select_multiple_mptt_model_objects

Implementation details
~~~~~~~~~~~~~~~~~~~~~~
Each ``django-fobi`` plugin has its' own representative integration plugin
within ``fobi.contrib.aps.drf_integration`` package.

Some of the plugins may seam to have zero-added-value and in fact they are.
For instance, DRF integration ``slider`` plugin is just an exact copy of the
``range_select`` plugin, created in order to provide exactly the same form
fields generated in the API.

You should mention all the plugins you want to use explicitly in the
project settings. Thus, if you have used (included in the ``INSTALLED_APPS``)
the core plugins:

- fobi.contrib.plugins.form_elements.fields.boolean
- fobi.contrib.plugins.form_elements.fields.checkbox_select_multiple
- fobi.contrib.plugins.form_elements.fields.date
- fobi.contrib.plugins.form_elements.fields.date_drop_down
- fobi.contrib.plugins.form_elements.fields.datetime
- fobi.contrib.plugins.form_elements.fields.decimal
- fobi.contrib.plugins.form_elements.fields.duration
- fobi.contrib.plugins.form_elements.fields.email
- fobi.contrib.plugins.form_elements.fields.file
- fobi.contrib.plugins.form_elements.fields.float
- fobi.contrib.plugins.form_elements.fields.hidden
- fobi.contrib.plugins.form_elements.fields.input
- fobi.contrib.plugins.form_elements.fields.integer
- fobi.contrib.plugins.form_elements.fields.ip_address
- fobi.contrib.plugins.form_elements.fields.null_boolean
- fobi.contrib.plugins.form_elements.fields.password
- fobi.contrib.plugins.form_elements.fields.radio
- fobi.contrib.plugins.form_elements.fields.range_select
- fobi.contrib.plugins.form_elements.fields.regex
- fobi.contrib.plugins.form_elements.fields.select
- fobi.contrib.plugins.form_elements.fields.select_multiple
- fobi.contrib.plugins.form_elements.fields.select_multiple_with_max
- fobi.contrib.plugins.form_elements.fields.slider
- fobi.contrib.plugins.form_elements.fields.slug
- fobi.contrib.plugins.form_elements.fields.text
- fobi.contrib.plugins.form_elements.fields.textarea
- fobi.contrib.plugins.form_elements.fields.time
- fobi.contrib.plugins.form_elements.fields.url
- fobi.contrib.plugins.form_elements.content.content_image
- fobi.contrib.plugins.form_elements.content.content_image_url
- fobi.contrib.plugins.form_elements.content.content_richtext
- fobi.contrib.plugins.form_elements.content.content_text
- fobi.contrib.plugins.form_elements.content.content_video
- fobi.contrib.plugins.form_handlers.db_store
- fobi.contrib.plugins.form_handlers.http_repost
- fobi.contrib.plugins.form_handlers.mail

You should include their correspondent Django REST framework implementations
in the ``INSTALLED_APPS`` as well:

- fobi.contrib.apps.drf_integration.form_elements.fields.boolean
- fobi.contrib.apps.drf_integration.form_elements.fields.checkbox_select_multiple
- fobi.contrib.apps.drf_integration.form_elements.fields.date
- fobi.contrib.apps.drf_integration.form_elements.fields.date_drop_down
- fobi.contrib.apps.drf_integration.form_elements.fields.datetime
- fobi.contrib.apps.drf_integration.form_elements.fields.decimal
- fobi.contrib.apps.drf_integration.form_elements.fields.duration
- fobi.contrib.apps.drf_integration.form_elements.fields.email
- fobi.contrib.apps.drf_integration.form_elements.fields.file
- fobi.contrib.apps.drf_integration.form_elements.fields.float
- fobi.contrib.apps.drf_integration.form_elements.fields.hidden
- fobi.contrib.apps.drf_integration.form_elements.fields.input
- fobi.contrib.apps.drf_integration.form_elements.fields.integer
- fobi.contrib.apps.drf_integration.form_elements.fields.ip_address
- fobi.contrib.apps.drf_integration.form_elements.fields.null_boolean
- fobi.contrib.apps.drf_integration.form_elements.fields.password
- fobi.contrib.apps.drf_integration.form_elements.fields.radio
- fobi.contrib.apps.drf_integration.form_elements.fields.range_select
- fobi.contrib.apps.drf_integration.form_elements.fields.regex
- fobi.contrib.apps.drf_integration.form_elements.fields.select
- fobi.contrib.apps.drf_integration.form_elements.fields.select_multiple
- fobi.contrib.apps.drf_integration.form_elements.fields.select_multiple_with_max
- fobi.contrib.apps.drf_integration.form_elements.fields.slider
- fobi.contrib.apps.drf_integration.form_elements.fields.slug
- fobi.contrib.apps.drf_integration.form_elements.fields.text
- fobi.contrib.apps.drf_integration.form_elements.fields.textarea
- fobi.contrib.apps.drf_integration.form_elements.fields.time
- fobi.contrib.apps.drf_integration.form_elements.fields.url
- fobi.contrib.apps.drf_integration.form_elements.content.content_image
- fobi.contrib.apps.drf_integration.form_elements.content.content_image_url
- fobi.contrib.apps.drf_integration.form_elements.content.content_richtext
- fobi.contrib.apps.drf_integration.form_elements.content.content_text
- fobi.contrib.apps.drf_integration.form_elements.content.content_video
- fobi.contrib.apps.drf_integration.form_handlers.db_store
- fobi.contrib.apps.drf_integration.form_handlers.http_repost
- fobi.contrib.apps.drf_integration.form_handlers.mail

Installation
~~~~~~~~~~~~
Versions
########
Was made with ``djangorestframework`` 3.6.2. May work on earlier versions,
although not guaranteed.

See the `requirements file
<https://github.com/barseghyanartur/django-fobi/blob/stable/examples/requirements/djangorestframework.txt>`_.

your_project/settings.py
########################
See the `example settings file
<https://github.com/barseghyanartur/django-fobi/blob/stable/examples/simple/settings_bootstrap3_theme_drf_integration.py>`_.

.. code-block:: python

    INSTALLED_APPS = list(INSTALLED_APPS)
    INSTALLED_APPS += [
        # ...
        # Here should come a list of form element plugins of the core
        # package, followed by the list of form handler plugins of the core
        # package, followed by the list of themes of the core package and
        # all other apps that do matter.
        # ...
        'rest_framework',  # Django REST framework
        'fobi.contrib.apps.drf_integration',  # DRF integration app

        # DRF integration form element plugins - fields
        'fobi.contrib.apps.drf_integration.form_elements.fields.boolean',
        'fobi.contrib.apps.drf_integration.form_elements.fields.checkbox_select_multiple',
        'fobi.contrib.apps.drf_integration.form_elements.fields.date',
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
        'fobi.contrib.apps.drf_integration.form_elements.fields.select_multiple',
        'fobi.contrib.apps.drf_integration.form_elements.fields.select_multiple_with_max',
        'fobi.contrib.apps.drf_integration.form_elements.fields.slider',
        'fobi.contrib.apps.drf_integration.form_elements.fields.slug',
        'fobi.contrib.apps.drf_integration.form_elements.fields.text',
        'fobi.contrib.apps.drf_integration.form_elements.fields.textarea',
        'fobi.contrib.apps.drf_integration.form_elements.fields.time',
        'fobi.contrib.apps.drf_integration.form_elements.fields.url',

        # DRF integration form element plugins - presentational
        'fobi.contrib.apps.drf_integration.form_elements.content.content_image',
        'fobi.contrib.apps.drf_integration.form_elements.content.content_image_url',
        'fobi.contrib.apps.drf_integration.form_elements.content.content_richtext',
        'fobi.contrib.apps.drf_integration.form_elements.content.content_text',
        'fobi.contrib.apps.drf_integration.form_elements.content.content_video',

        # DRF integration form handler plugins
        'fobi.contrib.apps.drf_integration.form_handlers.db_store',
        'fobi.contrib.apps.drf_integration.form_handlers.mail',
        'fobi.contrib.apps.drf_integration.form_handlers.http_repost',
        # ...
    ]

your_project/urls.py
####################
Add the following code to the main ``urls.py`` of your project:

.. code-block:: python

    # Conditionally including django-rest-framework integration app
    if 'fobi.contrib.apps.drf_integration' in settings.INSTALLED_APPS:
        from fobi.contrib.apps.drf_integration.urls import fobi_router
        urlpatterns += [
            url(r'^api/', include(fobi_router.urls))
        ]

Usage
~~~~~
If you have followed the steps above precisely, you would be able to access
the API using ``http://localhost:8000/api/fobi-form-entry/``.

Actions/methods supported:

LIST
####
.. code-block:: text

    GET /api/fobi-form-entry/

Lists all the forms available. Anonymous users would see the list of all
public forms. Authenticated users would see their own forms in addition
to the public forms.

OPTIONS
#######
.. code-block:: text

    OPTIONS /api/fobi-form-entry/{FORM_SLUG}/

Lists all field options for the selected form.

See the `test DRF form
<https://django-fobi.herokuapp.com/en/fobi/view/test-drf-form/>`_ and
`same form in DRF integration app
<https://django-fobi.herokuapp.com/api/fobi-form-entry/test-drf-form/>`_ with
most of the fields that do have rich additional metadata.

OPTIONS call produces the following response:

.. code-block:: text

    OPTIONS /api/fobi-form-entry/test-drf-form/
    HTTP 200 OK
    Allow: GET, PUT, PATCH, OPTIONS
    Content-Type: application/json
    Vary: Accept


.. code-block:: python

    {
        "name": "Fobi Form Entry Instance",
        "description": "FormEntry view set.",
        "renders": [
            "application/json",
            "text/html"
        ],
        "parses": [
            "application/json",
            "application/x-www-form-urlencoded",
            "multipart/form-data"
        ],
        "actions": {
            "PUT": {
                "test_integer": {
                    "type": "integer",
                    "required": false,
                    "read_only": false,
                    "label": "Test integer",
                    "min_value": 1,
                    "max_value": 20,
                    "initial": 10
                },
                "test_email": {
                    "type": "email",
                    "required": true,
                    "read_only": false,
                    "label": "Test email",
                    "help_text": "Donec mollis hendrerit risus. Phasellus a "
                                 "est. Nam ipsum risus, rutrum vitae, "
                                 "vestibulum eu, molestie vel, lacus. "
                                 "Praesent nec nisl a purus blandit viverra. "
                                 "Cras id dui.",
                    "max_length": 255,
                    "placeholder": "john@doe.com"
                },
                "test_text": {
                    "type": "string",
                    "required": false,
                    "read_only": false,
                    "label": "Test text",
                    "help_text": "Sed lectus. Phasellus gravida semper "
                                 "nisi. Curabitur at lacus ac velit ornare "
                                 "lobortis. Mauris turpis nunc, blandit et, "
                                 "volutpat molestie, porta ut, ligula. Lorem "
                                 "ipsum dolor sit amet, consectetuer "
                                 "adipiscing elit.",
                    "max_length": 255,
                    "placeholder": "Lorem ipsum dolor sit amet"
                },
                "test_url": {
                    "type": "url",
                    "required": false,
                    "read_only": false,
                    "label": "Test URL",
                    "max_length": 255,
                    "initial": "http://github.com"
                },
                "test_decimal_field": {
                    "type": "decimal",
                    "required": false,
                    "read_only": false,
                    "label": "Test decimal field",
                    "min_value": 1.0,
                    "max_value": 25.0,
                    "initial": 10.0,
                    "placeholder": "3.14",
                    "max_digits": 5,
                    "decimal_places": 2
                },
                "test_float_field": {
                    "type": "float",
                    "required": false,
                    "read_only": false,
                    "label": "Test float field",
                    "min_value": 1.0,
                    "max_value": 10.0,
                    "initial": 3.14
                },
                "test_ip_address": {
                    "type": "string",
                    "required": false,
                    "read_only": false,
                    "label": "Test IP address",
                    "max_length": 255,
                    "placeholder": "127,0.0.1"
                },
                "test_password_field": {
                    "type": "string",
                    "required": false,
                    "read_only": false,
                    "label": "Test password field",
                    "max_length": 255,
                    "placeholder": "your-secret-password"
                },
                "test_regex_field": {
                    "type": "regex",
                    "required": false,
                    "read_only": false,
                    "label": "Test regex field",
                    "max_length": 255,
                    "regex": "^([a-zA-Z])+$"
                },
                "test_slug_field": {
                    "type": "slug",
                    "required": false,
                    "read_only": false,
                    "label": "Test slug field",
                    "max_length": 255,
                    "placeholder": "lorem-ipsum-dolor-sit-amet"
                },
                "test_textarea_field": {
                    "type": "string",
                    "required": false,
                    "read_only": false,
                    "label": "Test textarea field",
                    "placeholder": "Pellentesque habitant morbi tristique."
                },
                "test_input_field": {
                    "type": "string",
                    "required": false,
                    "read_only": true,
                    "label": "Test input field",
                    "max_length": 255,
                    "autofocus": "autofocus",
                    "autocomplete": "on",
                    "disabled": "disabled"
                },
                "content_image_url_b0996b16-9f1c-430d-a6c7-0a722f4c2177": {
                    "type": "content",
                    "required": false,
                    "read_only": true,
                    "initial": "<p><img src=\"http://example.com/image.jpg\" alt=\"n.n.\" width=\"600\"/></p>",
                    "contenttype": "image",
                    "raw_data": {
                        "url": "http://example.com/image.jpg",
                        "alt": "n.n.",
                        "fit_method": "fit_width",
                        "size": "600x600"
                    },
                    "content": "<p><img src=\"http://example.com/image.jpg\" alt=\"n.n.\" width=\"600\"/></p>"
                },
                "content_text_de4d69b2-99e1-479d-8c61-1534dea7c981": {
                    "type": "content",
                    "required": false,
                    "read_only": true,
                    "initial": "<p>Pellentesque posuere. Quisque id mi. "
                               "Duis arcu tortor, suscipit eget, imperdiet "
                               "nec, imperdiet iaculis, ipsum. Phasellus a "
                               "est. In turpis.</p>",
                    "contenttype": "text",
                    "raw_data": {
                        "text": "Pellentesque posuere. Quisque id mi. Duis "
                                "arcu tortor, suscipit eget, imperdiet nec, "
                                "imperdiet iaculis, ipsum. Phasellus a est. "
                                "In turpis."
                    },
                    "content": "<p>Pellentesque posuere. Quisque id mi. Duis "
                               "arcu tortor, suscipit eget, imperdiet nec, "
                               "imperdiet iaculis, ipsum. Phasellus a est. "
                               "In turpis.</p>"
                },
                "content_video_f4799aca-9a0b-4f1a-8069-dda611858ef4": {
                    "type": "content",
                    "required": false,
                    "read_only": true,
                    "initial": "<iframe src=\"//www.youtube.com/embed/8GVIui0JK0M\" width=\"500\" height=\"400\" frameborder=\"0\" allowfullscreen></iframe>",
                    "contenttype": "video",
                    "raw_data": {
                        "title": "Delusional Insanity - To far beyond...",
                        "url": "https://www.youtube.com/watch?v=8GVIui0JK0M&t=1s",
                        "size": "500x400"
                    },
                    "content": "<iframe src=\"//www.youtube.com/embed/8GVIui0JK0M\" width=\"500\" height=\"400\" frameborder=\"0\" allowfullscreen></iframe>"
                }
            }
        }
    }

**Some insights:**

Meta-data is passed to the ``DRFIntegrationFormElementPluginProcessor`` as
``field_metadata`` argument, which is supposed to be a dict.

- `Example 1: content_image plugin
  <https://github.com/barseghyanartur/django-fobi/blob/master/src/fobi/contrib/apps/drf_integration/form_elements/content/content_image/base.py#L54>`_

- `Example 2: decimal plugin
  <https://github.com/barseghyanartur/django-fobi/blob/master/src/fobi/contrib/apps/drf_integration/form_elements/fields/decimal/base.py#L86>`_

- `Example 3: text plugin
  <https://github.com/barseghyanartur/django-fobi/blob/master/src/fobi/contrib/apps/drf_integration/form_elements/fields/text/base.py#L55>`_

Private forms would be only visible to authenticated users.

PUT
###
.. code-block:: text

    PUT /api/fobi-form-entry/{FORM_SLUG}/

    {DATA}

Callbacks
~~~~~~~~~
Callbacks work just the same way the core callbacks work.

fobi_form_callbacks.py
######################
.. code-block:: python

    from fobi.base import (
        integration_form_callback_registry,
        IntegrationFormCallback,
    )

    from fobi.constants import (
        CALLBACK_BEFORE_FORM_VALIDATION,
        CALLBACK_FORM_INVALID,
        CALLBACK_FORM_VALID,
        CALLBACK_FORM_VALID_AFTER_FORM_HANDLERS,
        CALLBACK_FORM_VALID_BEFORE_SUBMIT_PLUGIN_FORM_DATA,
    )

    from fobi.contrib.apps.drf_integration import UID as INTEGRATE_WITH


    class DRFSaveAsFooItem(IntegrationFormCallback):
        """Save the form as a foo item, if certain conditions are met."""

        stage = CALLBACK_FORM_VALID
        integrate_with = INTEGRATE_WITH

        def callback(self, form_entry, request, **kwargs):
            """Custom callback login comes here."""
            logger.debug("Great! Your form is valid!")


    class DRFDummyInvalidCallback(IntegrationFormCallback):
        """Saves the form as a foo item, if certain conditions are met."""

        stage = CALLBACK_FORM_INVALID
        integrate_with = INTEGRATE_WITH

        def callback(self, form_entry, request, **kwargs):
            """Custom callback login comes here."""
            logger.debug("Damn! You've made a mistake, boy!")

Testing
~~~~~~~
To test Django REST framework integration package only, run the following
command:

.. code-block:: sh

    ./runtests.py src/fobi/tests/test_drf_integration.py

or use plain Django tests:

.. code-block:: sh

    ./manage.py test fobi.tests.test_drf_integration --settings=settings.test

Limitations
~~~~~~~~~~~
Certain fields are not available yet (relational fields).


Form elements
-------------


Content form element
~~~~~~~~~~~~~~~~~~~~
Presentational form elements for ``drf_integration``.


fobi.contrib.apps.drf_integration.form_elements.content.content_image
#####################################################################
A ``django-fobi`` ContentImage plugin for integration with
``Django REST framework``. Makes use of the
``fobi.contrib.apps.drf_integration.fields.ContentImage``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.content.content_image``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.content.content_image',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

Usage
^^^^^
Unlike standard fields, ``ContentImage`` field is purely presentational.
You're not supposed to make write actions on it (it won't work). Neither
will it be displayed in the browsable API (list/retrieve actions). However,
it will be listed in the options action call.

**Sample JSON response fragment**

.. code-block:: javascript

    "actions": {
        "PUT": {
            // ...
            "content_image_89c8c319-195b-487a-a44d-f59ef14a5d44": {
                "type": "content",
                "required": false,
                "read_only": true,
                "contenttype": "image",
                "content": "\n<p>\n\n\n\n\n<img src=\"/media/fobi_plugins/content_image/test-image-thumbnail.jpg\" alt=\"Lorem ipsum\"/>\n\n\n</p>\n",
                "raw": {
                    "file": "/media/fobi_plugins/content_image/test-image.jpg",
                    "alt": "Lorem ipsum",
                    "fit_method": "center",
                    "size": "500x500"
                }
            },
            // ...
        }
    }

**JSON response fragment explained**

- ``type`` (str): Set to "content" for all presentational form elements.
- ``contenttype`` (str): Set to "image" for ``ContentImage`` field.
- ``content`` (str): Representation of the content. Rendered partial HTML.
- ``raw`` (json dict): Raw attributes of the ``ContentImage`` plugin. Contains
  "file", "alt", "fit_method" and "size" attributes.


fobi.contrib.apps.drf_integration.form_elements.content.content_image_url
#########################################################################
A ``django-fobi`` ContentImageURL plugin for integration with
``Django REST framework``. Makes use of the
``fobi.contrib.apps.drf_integration.fields.ContentImage``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.content.content_image_url``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.content.content_image_url',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

Usage
^^^^^
Unlike standard fields, ``ContentImageURL`` field is purely presentational.
You're not supposed to make write actions on it (it won't work). Neither
will it be displayed in the browsable API (list/retrieve actions). However,
it will be listed in the options action call.

**Sample JSON response fragment**

.. code-block:: javascript

    "actions": {
        "PUT": {
            // ...
            "content_image_89c8c319-195b-487a-a44d-f59ef14a5d44": {
                "type": "content",
                "required": false,
                "read_only": true,
                "contenttype": "image",
                "content": "\n<p>\n\n\n\n\n<img src=\"http://example.com/media/test-image.jpg\" alt=\"Lorem ipsum\"/>\n\n\n</p>\n",
                "raw": {
                    "url": "http://example.com/media/test-image.jpg",
                    "alt": "Lorem ipsum",
                    "fit_method": "fit_width",
                    "size": "500x500"
                }
            },
            // ...
        }
    }

**JSON response fragment explained**

- ``type`` (str): Set to "content" for all presentational form elements.
- ``contenttype`` (str): Set to "image" for ``ContentImageURL`` field.
- ``content`` (str): Representation of the content. Rendered partial HTML.
- ``raw`` (json dict): Raw attributes of the ``ContentImageURL`` plugin.
  Contains "url", "alt", "fit_method" and "size" attributes.


fobi.contrib.apps.drf_integration.form_elements.content.content_richtext
########################################################################
A ``django-fobi`` ContentRichText plugin for integration with
``Django REST framework``. Makes use of the
``fobi.contrib.apps.drf_integration.fields.ContentRichText``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.content.content_richtext``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.content.content_richtext',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

Usage
^^^^^
Unlike standard fields, ``ContentText`` field is purely presentational.
You're not supposed to make write actions on it (it won't work). Neither
will it be displayed in the browsable API (list/retrieve actions). However,
it will be listed in the options action call.

**Sample JSON response fragment**

.. code-block:: javascript

    "actions": {
        "PUT": {
            // ...
            "content_text_89c8c319-195b-487a-a44d-f59ef14a5d44": {
                "type": "content",
                "required": false,
                "read_only": true,
                "contenttype": "text",
                "content": "\n<p>\n\nLorem ipsum dolor sit amet.\n\n\n</p>\n",
                "raw": {
                    "text": "Lorem ipsum dolor sit amet."
                }
            },
            // ...
        }
    }

**JSON response fragment explained**

- ``type`` (str): Set to "content" for all presentational form elements.
- ``contenttype`` (str): Set to "text" for ``ContentText`` field.
- ``content`` (str): Representation of the content. Rendered partial HTML.
- ``raw`` (json dict): Raw attributes of the ``ContentText`` plugin. Contains
  "text" attribute.


fobi.contrib.apps.drf_integration.form_elements.content.content_text
####################################################################
A ``django-fobi`` ContentText plugin for integration with
``Django REST framework``. Makes use of the
``fobi.contrib.apps.drf_integration.fields.ContentText``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.content.content_text``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.content.content_text',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

Usage
^^^^^
Unlike standard fields, ``ContentText`` field is purely presentational.
You're not supposed to make write actions on it (it won't work). Neither
will it be displayed in the browsable API (list/retrieve actions). However,
it will be listed in the options action call.

**Sample JSON response fragment**

.. code-block:: javascript

    "actions": {
        "PUT": {
            // ...
            "content_text_89c8c319-195b-487a-a44d-f59ef14a5d44": {
                "type": "content",
                "required": false,
                "read_only": true,
                "contenttype": "text",
                "content": "\n<p>\n\nLorem ipsum dolor sit amet.\n\n\n</p>\n",
                "raw": {
                    "text": "Lorem ipsum dolor sit amet."
                }
            },
            // ...
        }
    }

**JSON response fragment explained**

- ``type`` (str): Set to "content" for all presentational form elements.
- ``contenttype`` (str): Set to "text" for ``ContentText`` field.
- ``content`` (str): Representation of the content. Rendered partial HTML.
- ``raw`` (json dict): Raw attributes of the ``ContentText`` plugin. Contains
  "text" attribute.


fobi.contrib.apps.drf_integration.form_elements.content.content_video
#####################################################################
A ``django-fobi`` ContentVideo plugin for integration with
``Django REST framework``. Makes use of the
``fobi.contrib.apps.drf_integration.fields.ContentVideo``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.content.content_video``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.content.content_video',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

Usage
^^^^^
Unlike standard fields, ``ContentVideo`` field is purely presentational.
You're not supposed to make write actions on it (it won't work). Neither
will it be displayed in the browsable API (list/retrieve actions). However,
it will be listed in the options action call.

**Sample JSON response fragment**

.. code-block:: javascript

    "actions": {
        "PUT": {
            // ...
            "content_video_41a6b951-e6f9-4f08-ada6-3b109aa9a72f": {
                "type": "content",
                "required": false,
                "read_only": true,
                "contenttype": "video",
                "content": "\n<iframe src=\"//www.youtube.com/embed/3P1qcVcs4Ik\" width=\"500\" height=\"400\" frameborder=\"0\" allowfullscreen></iframe>\n",
                "raw": {
                    "title": "Cras risus ipsum faucibus",
                    "url": "https://www.youtube.com/watch?v=3P1qcVcs4Ik",
                    "size": "500x400"
                }
            },
            // ...
        }
    }

**JSON response fragment explained**

- ``type`` (str): Set to "content" for all presentational form elements.
- ``contenttype`` (str): Set to "video" for ``ContentVideo`` field.
- ``content`` (str): Representation of the content. Rendered partial HTML.
- ``raw`` (json dict): Raw attributes of the ``ContentVideo`` plugin. Contains
  "title", "url" and "size" attributes.


Fields
~~~~~~
Form fields for ``drf_integration``.


fobi.contrib.apps.drf_integration.form_elements.fields.boolean
##############################################################
A ``django-fobi`` BooleanField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.BooleanField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.boolean`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.boolean',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.checkbox_select_multiple
###############################################################################
A ``django-fobi`` CharField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.MultipleChoiceField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.checkbox_select_multiple``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.checkbox_select_multiple',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.date
###########################################################
A ``django-fobi`` DateField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.DateField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.date`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.date',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.date_drop_down
#####################################################################
A ``django-fobi`` DateField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.DateField``.

This plugin has been made primarily for compatibility with ``date_drop_down``
plugin of the core package.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.date_drop_down``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.date_drop_down',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.datetime
###############################################################
A ``django-fobi`` DateField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.DateTimeField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.datetime`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.datetime',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.decimal
##############################################################
A ``django-fobi`` DecimalField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.DecimalField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.decimal`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.decimal',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.email
############################################################
A ``django-fobi`` EmailField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.EmailField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.email`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.email',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.file
###########################################################
A ``django-fobi`` FileField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.FileField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.file`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.file',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.float
############################################################
A ``django-fobi`` FloatField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.FloatField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.float`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.float',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.hidden
#############################################################
A ``django-fobi`` HiddenField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.HiddenField``.

Note, that in terms of the Django REST framework it is a read-only field.
Any values posted along won't be saved. Initial value would.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.hidden`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.hidden',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.input
############################################################
A ``django-fobi`` CharField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.CharField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.input`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.input',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.integer
##############################################################
A ``django-fobi`` IntegerField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.IntegerField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.integer`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.integer',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.ip_address
#################################################################
A ``django-fobi`` IPAddressField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.IPAddressField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.ip_address`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.ip_address',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.null_boolean
###################################################################
A ``django-fobi`` NullBooleanField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.NullBooleanField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.null_boolean``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.null_boolean',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.password
###############################################################
A ``django-fobi`` CharField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.CharField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.password`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.password',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.radio
############################################################
A ``django-fobi`` CharField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.ChoiceField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.radio`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.radio',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.range_select
###################################################################
A ``django-fobi`` ChoiceField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.ChoiceField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.range_select``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.range_select',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.regex
############################################################
A ``django-fobi`` RegexField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.RegexField``.

Installation
^^^^^^^^^^^^
1. Add ``fobi.contrib.apps.drf_integration.form_elements.fields.regex`` to
   the ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi.contrib.apps.drf_integration.form_elements.fields.regex',
        # ...
    )

2. In the terminal type:

.. code-block:: sh

    ./manage.py fobi_sync_plugins

3. Assign appropriate permissions to the target users/groups to be using
   the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.select
#############################################################
A ``django-fobi`` ChoiceField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.ChoiceField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.select``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.select',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.select_multiple
######################################################################
A ``django-fobi`` CharField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.MultipleChoiceField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.select_multiple``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.select_multiple',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.select_multiple
######################################################################
A ``django-fobi`` CharField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.MultipleChoiceField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.select_multiple``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.select_multiple',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.slider
#############################################################
A ``django-fobi`` ChoiceField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.ChoiceField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.slider``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.slider',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.slug
###########################################################
A ``django-fobi`` SlugField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.SlugField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.slug`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.slug',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.text
###########################################################
A ``django-fobi`` CharField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.CharField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.text`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.text',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.textarea
###############################################################
A ``django-fobi`` CharField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.CharField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.textarea`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.textarea',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.time
###########################################################
A ``django-fobi`` TimeField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.TimeField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.time`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.time',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_elements.fields.url
##########################################################
A ``django-fobi`` URLField plugin for integration with
``Django REST framework``. Makes use of the
``rest_framework.fields.URLField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.time`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.url',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


Form handlers
-------------
Form handlers for ``drf_integration``.


fobi.contrib.apps.drf_integration.form_handlers.db_store
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A ``django-fobi`` Mail form handler plugin for integration
with ``Django REST framework``. Saves submitted form data into the
``SavedFormDataEntry`` model.

Installation
############
(1) Add ``fobi.contrib.apps.drf_integration.form_handlers.db_store`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_handlers.db_store',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py migrate

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_handlers.http_repost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A ``django-fobi`` HTTP repost form handler plugin for integration
with ``Django REST framework``. Submits the form to another endpoint specified.

Installation
############
(1) Add ``fobi.contrib.apps.drf_integration.form_handlers.http_respost`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_handlers.http_repost',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.drf_integration.form_handlers.mail
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A ``django-fobi`` Mail form handler plugin for integration
with ``Django REST framework``. Submits the form data by email to the
specified email address.

Installation
############
(1) Add ``fobi.contrib.apps.drf_integration.form_handlers.mail`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_handlers.mail',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py migrate

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.apps.feincms_integration
-------------------------------------
A ``django-fobi`` integration with FeinCMS.

Prerequisites
~~~~~~~~~~~~~
Tested with FeinCMS 1.10, 1.12 and 1.13 only. Might work on earlier (or
later) versions as well.

Installation
~~~~~~~~~~~~
Versions
########
See the requirements files:

- `FeinCMS 1.10 requirements
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/requirements/feincms_1_10.txt>`_.
- `FeinCMS 1.12 requirements
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/requirements/feincms_1_12.txt>`_.
- `FeinCMS 1.13 requirements
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/requirements/feincms_1_13.txt>`_.

your_project/settings.py
########################
See the `example settings file
<https://github.com/barseghyanartur/django-fobi/blob/stable/examples/simple/settings/bootstrap3_theme_feincms.py>`_.

.. code-block:: python

    INSTALLED_APPS = list(INSTALLED_APPS)
    INSTALLED_APPS += [
        'feincms',  # FeinCMS

        'fobi.contrib.apps.feincms_integration',  # Fobi FeinCMS app

        'page',  # Example
    ]

    FEINCMS_RICHTEXT_INIT_CONTEXT = {
        'TINYMCE_JS_URL': STATIC_URL + 'tiny_mce/tiny_mce.js',
    }

your_project/page/models.py
###########################
.. code-block:: python

    from django.utils.translation import ugettext_lazy as _

    from feincms.module.page.models import Page
    from feincms.content.raw.models import RawContent
    from feincms.content.richtext.models import RichTextContent
    # Import the ``django-fobi`` widget.
    from fobi.contrib.apps.feincms_integration.widgets import FobiFormWidget

    Page.register_extensions('feincms.module.extensions.translations',)

    # Register basic template.
    Page.register_templates(
        {
            'title': _(u"Base template"),
            'path': 'page/base.html',
            'key': 'page_base',
            'regions': (
                ('main', _(u"Main")),
                ('sidebar', _(u"Sidebar")),
            )
        },
        )

    # Standard content types
    Page.create_content_type(RawContent)
    Page.create_content_type(RichTextContent)

    # Register the ``django-fobi`` widget.
    Page.create_content_type(FobiFormWidget)

your_project/admin.py
#####################
.. code-block:: python

    from django.contrib import admin

    from feincms.module.page.modeladmins import PageAdmin

    from page.models import Page

    admin.site.register(Page, PageAdmin)

Information for developers
##########################
Template rendering
^^^^^^^^^^^^^^^^^^
The embed FeinCMS widget is rendered with use of two theme templates:

- ``view_embed_form_entry_ajax_template``: Used for rendering the form.
- ``embed_form_entry_submitted_ajax_template``: Used for rendering the form
  sent event.

Using custom templates for rendering the widget
###############################################
In the widget, you can specify a template which you want to be used for
rendering the form or the form-sent event.

Example:

.. code-block:: python

    FOBI_FEINCMS_INTEGRATION_FORM_TEMPLATE_CHOICES = (
        ("yourapp/custom_view_embed_form_v1.html",
         "Custom embed form view template #1"),
        ("yourapp/custom_view_embed_form_v2.html",
         "Custom embed form view template #2"),
    )

Same goes for form-sent templates.

.. code-block:: python

    FOBI_FEINCMS_INTEGRATION_SUCCESS_PAGE_TEMPLATE_CHOICES = (
        ("yourapp/custom_embed_form_submitted_v1.html",
         "Custom form-sent template #1"),
        ("yourapp/custom_embed_form_submitted_v2.html",
         "Custom form-sent template #2"),
    )

Registering a template in the ``FORM_TEMPLATE_CHOICES`` makes it available
for all the themes. If you rather want to use different custom templates
for different themes, use the ``FOBI_CUSTOM_THEME_DATA`` as shown in the
example below.

.. code-block:: python

    FOBI_CUSTOM_THEME_DATA = {
        'bootstrap3': {
            'feincms_integration': {
                'form_template_choices': [
                    ('fobi/bootstrap3_extras/view_embed_form.html',
                     "Custom bootstrap3 embed form view template"),
                ],
                'success_page_template_choices': [
                    ('fobi/bootstrap3_extras/embed_form_submitted.html',
                     "Custom bootstrap3 embed form entry submitted template"),
                ],
            },
        },
        'foundation5': {
            'feincms_integration': {
                'form_template_choices': [
                    ('fobi/foundation5_extras/view_embed_form.html',
                     "Custom foundation5 embed form view template"),
                ],
                'success_page_template_choices': [
                    ('fobi/foundation5_extras/embed_form_submitted.html',
                     "Custom foundation5 embed form entry submitted template"),
                ],
            },
        },
    }

Usage
~~~~~
The ``fobi.contrib.apps.feincms_integration.widgets.FobiFormWidget`` consists
of the following fields:

- Form: The form to be used.
- Form template name: Template to be used to render the embed form.
- Hide form title: If checked, no form title would be shown.
- Form title: Overrides the standard form title.
- Submit button text: Overrides the default submit button text.
- Success page template name: Template to be used to render the embed form-sent
  event.
- Hide success page title: If checked, no form-sent title would be shown.
- Success page title: Overrides the form-sent title.
- Success page text: Overrides the form-sent text.


fobi.contrib.apps.mezzanine_integration
---------------------------------------
A ``django-fobi`` integration with Mezzanine.

Prerequisites
~~~~~~~~~~~~~
Tested with Mezzanine 3.1.10 and 4.2.3 only. Might work on earlier (or
later) versions as well.

Installation
~~~~~~~~~~~~
Versions
########
See the requirements files:

- `Mezzanine 4.2.3 requirements
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/mezzanine_example/requirements.txt>`_.

your_project/settings.py
########################
See the `example settings file
<https://github.com/barseghyanartur/django-fobi/blob/stable/examples/mezzanine_example/settings.py>`_.

.. code-block:: python

    INSTALLED_APPS = list(INSTALLED_APPS)
    INSTALLED_APPS += [
        # Standard mezzanine apps

        'fobi.contrib.apps.mezzanine_integration',  # Fobi Mezzanine app
    ]

Information for developers
~~~~~~~~~~~~~~~~~~~~~~~~~~
Template rendering
##################
The form embed into Mezzanine page is rendered with use of two theme templates:

- ``view_embed_form_entry_ajax_template``: Used for rendering the form.
- ``embed_form_entry_submitted_ajax_template``: Used for rendering the form
  sent event.

Using custom templates for rendering the form
#############################################
In the widget, you can specify a template which you want to be used for
rendering the form or the form-sent event.

Example:

.. code-block:: python

    FOBI_MEZZANINE_INTEGRATION_FORM_TEMPLATE_CHOICES = (
        ("yourapp/custom_view_embed_form_v1.html",
         "Custom embed form view template #1"),
        ("yourapp/custom_view_embed_form_v2.html",
         "Custom embed form view template #2"),
    )

Same goes for form-sent templates.

.. code-block:: python

    FOBI_MEZZANINE_INTEGRATION_SUCCESS_PAGE_TEMPLATE_CHOICES = (
        ("yourapp/custom_embed_form_submitted_v1.html",
         "Custom form-sent template #1"),
        ("yourapp/custom_embed_form_submitted_v2.html",
         "Custom form-sent template #2"),
    )

Registering a template in the ``FORM_TEMPLATE_CHOICES`` makes it available
for all the themes. If you rather want to use different custom templates
for different themes, use the ``FOBI_CUSTOM_THEME_DATA`` as shown in the
example below.

.. code-block:: python

    FOBI_CUSTOM_THEME_DATA = {
        'bootstrap3': {
            'mezzanine_integration': {
                'form_template_choices': [
                    ('fobi/bootstrap3_extras/view_embed_form.html',
                     "Custom bootstrap3 embed form view template"),
                ],
                'success_page_template_choices': [
                    ('fobi/bootstrap3_extras/embed_form_submitted.html',
                     "Custom bootstrap3 embed form entry submitted template"),
                ],
            },
        },
        'foundation5': {
            'mezzanine_integration': {
                'form_template_choices': [
                    ('fobi/foundation5_extras/view_embed_form.html',
                     "Custom foundation5 embed form view template"),
                ],
                'success_page_template_choices': [
                    ('fobi/foundation5_extras/embed_form_submitted.html',
                     "Custom foundation5 embed form entry submitted template"),
                ],
            },
        },
    }

Usage
~~~~~
The ``fobi`` page model
#######################
The ``fobi.contrib.apps.mezzanine_integration.models.FobiFormPage`` consists
of the following fields:

- Form: The form to be used.
- Form template name: Template to be used to render the embed form.
- Hide form title: If checked, no form title would be shown.
- Form title: Overrides the standard form title.
- Submit button text: Overrides the default submit button text.
- Success page template name: Template to be used to render the embed form-sent
  event.
- Hide success page title: If checked, no form-sent title would be shown.
- Success page title: Overrides the form-sent title.
- Success page text: Overrides the form-sent text.

Steps described
###############
1. If you use the mezzanine `example
   <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/mezzanine_example/>`_
   project, to start go to the http://localhost:8003/fobi/ URL and create a
   form.
2. Then go to http://localhost:8003/admin/pages/page/ and add a new `Fobi form`
   page.
3. Choose the form and optionally - override the form settings and then
   save the page.
4. See the page in the front-end.


fobi.contrib.plugins.form_elements.content.content_image
--------------------------------------------------------
A ``Fobi`` Image form element plugin.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.content.content_image`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'easy_thumbnails',
            'fobi.contrib.plugins.form_elements.content.content_image',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) Additionally, for the fine tuning, see the
    ``fobi.contrib.plugins.form_elements.content.content_image.defaults``
    module. If necessary, override the settings by prepending
    ``FOBI_PLUGIN_CONTENT_IMAGE_`` to the desired variable name from the
    above mentioned ``defaults`` module.


fobi.contrib.plugins.form_elements.content.content_image_url
------------------------------------------------------------
A ``Fobi`` ImageURL form element plugin.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.content.content_image_url`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.content.content_image_url',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) Additionally, for the fine tuning, see the
    ``fobi.contrib.plugins.form_elements.content.content_image_url.defaults``
    module. If necessary, override the settings by prepending
    ``FOBI_PLUGIN_CONTENT_IMAGE_URL_`` to the desired variable name from the
    above mentioned ``defaults`` module.


fobi.contrib.plugins.form_elements.content.content_text
-------------------------------------------------------
A ``Fobi`` Text form element plugin.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.content.content_text`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.content.content_text',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) Additionally, for the fine tuning, see the
    ``fobi.contrib.plugins.form_elements.content.content_text.defaults``
    module. If necessary, override the settings by prepending
    ``FOBI_PLUGIN_CONTENT_TEXT_`` to the desired variable name from the
    above mentioned ``defaults`` module.

    By default the content of the text field is stripped using either the
    awesome `bleach <https://bleach.readthedocs.io/>`_ library or if bleach
    is not installed just Django's own `strip_tags` function. To configure
    the strip (bleach only) behaviour, two settings are introduced:

    .. code-block:: text

       - ALLOWED_TAGS:
       - ALLOWED_ATTRIBUTES:

    The default values are:

    .. code-block:: python

        ALLOWED_TAGS = [
            'a',
            'abbr',
            'acronym',
            'b',
            'blockquote',
            'code',
            'em',
            'i',
            'li',
            'ol',
            'strong',
            'ul',
        ]

        ALLOWED_ATTRIBUTES = {
            'a': ['href', 'title'],
            'abbr': ['title'],
            'acronym': ['title'],
        }


fobi.contrib.plugins.form_elements.content.content_richtext
-----------------------------------------------------------

A ``Fobi`` Rich text form element plugin based on
`CKEditor <https://ckeditor.com/>`_ and
`django-ckeditor <https://github.com/django-ckeditor/django-ckeditor>`_.

Installation
~~~~~~~~~~~~

(1) Install ``django-ckeditor``.

    .. code-block:: sh

        pip install django-ckeditor

(2) Add ``ckeditor`` to ``INSTALLED_APPS`` in ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            ...
            'ckeditor',
            ...
        )

(3) Add ``fobi.contrib.plugins.form_elements.content.content_richtext`` to
    ``INSTALLED_APPS`` in ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            ...
            'fobi.contrib.plugins.form_elements.content.content_richtext',
            ...
        )

(4) Add ``fobi.contrib.themes.bootstrap3.widgets.form_elements.content_richtext_bootstrap3_widget`` to
    ``INSTALLED_APPS`` in ``settings.py`` (if you're using ``bootstrap3`` theme).
    If you're using another theme, add correspondent widget specific to the
    active theme.

    .. code-block:: python

        INSTALLED_APPS = (
            ...
            'fobi.contrib.themes.bootstrap3.widgets.form_elements.content_richtext_bootstrap3_widget',
            ...
        )

(5) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(6) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to ``True``.

Controlling HTML tags and attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(1) Install ``bleach``.

    .. code-block:: sh

        pip install bleach

(2) Specify ``FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_TAGS``,
    ``FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_ATTRIBUTES`` and
    ``FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_STYLES`` in
    ``settings.py``. The default values come from bleach:

    .. code-block:: python

        FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_TAGS = [
            'a',
            'abbr',
            'acronym',
            'b',
            'blockquote',
            'code',
            'em',
            'i',
            'li',
            'ol',
            'strong',
            'ul',
        ]

        FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_ATTRIBUTES = {
            'a': ['href', 'title'],
            'abbr': ['title'],
            'acronym': ['title'],
        }

        FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_STYLES = []


fobi.contrib.plugins.form_elements.content.content_video
--------------------------------------------------------
A ``Fobi`` Video form element plugin.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.content.content_video`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.content.content_video',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) Additionally, for the fine tuning, see the
    ``fobi.contrib.plugins.form_elements.content.content_video.defaults``
    module. If necessary, override the settings by prepending
    ``FOBI_PLUGIN_CONTENT_VIDEO_`` to the desired variable name from the
    above mentioned ``defaults`` module.


fobi.contrib.plugins.form_elements.fields.boolean
-------------------------------------------------
A ``Fobi`` Boolean form field plugin. Makes use of the
``django.forms.fields.BooleanField``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.boolean`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.boolean',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.fields.checkbox_select_multiple
------------------------------------------------------------------
A ``Fobi`` Select Multiple form field plugin. Makes use of the
``django.forms.fields.MultipleChoiceField`` and
``django.forms.widgets.CheckboxSelectMultiple``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.checkbox_select_multiple``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.checkbox_select_multiple',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) By default, the submitted form value of `checkbox_select_multiple`
    elements is label (human readable representation of the value chosen).
    However, that part of the behaviour has been made configurable. You can
    choose between the following options:

    Consider the following list of (value, label) choices (the first element in
    the tuple is value, the second element is label):

    .. code-block:: python

        [
            ('alpha', 'Alpha'),
            ('beta', 'Beta'),
            ('gamma', 'Gamma'),
        ]

    - "val": `value` (example: "alpha").
    - "repr" (default): `label` (example: "Alpha").
    - "mix": `value (label)` (example: "Alpha (alpha)").

    Simply set the
    ``FOBI_FORM_ELEMENT_CHECKBOX_SELECT_MULTIPLE_SUBMIT_VALUE_AS`` assign one
    of the following values: "val", "repr" or "mix" to get the desired
    behaviour.

Usage
~~~~~
You should be entering a single choice per line. Choice might
consist of just a single value or value/label pair.

For example:

.. code-block:: text

    1
    2
    alpha, Alpha
    beta, Beta
    omega

The following HTML would be made of:

.. code-block:: html
      
    <ul id="id_NAME_OF_THE_ELEMENT">
      <li>
        <label for="id_NAME_OF_THE_ELEMENT_0">
          <input class="form-control" id="id_NAME_OF_THE_ELEMENT_0" name="NAME_OF_THE_ELEMENT" type="checkbox" value="1" /> 1
        </label>
      </li>
      <li>
        <label for="id_NAME_OF_THE_ELEMENT_1">
          <input class="form-control" id="id_NAME_OF_THE_ELEMENT_1" name="NAME_OF_THE_ELEMENT" type="checkbox" value="2" /> 2
        </label>
      </li>
      <li>
        <label for="id_NAME_OF_THE_ELEMENT_2">
          <input class="form-control" id="id_NAME_OF_THE_ELEMENT_2" name="NAME_OF_THE_ELEMENT" type="checkbox" value="alpha" /> Alpha
        </label>
      </li>
      <li>
        <label for="id_NAME_OF_THE_ELEMENT_3">
          <input class="form-control" id="id_NAME_OF_THE_ELEMENT_3" name="NAME_OF_THE_ELEMENT" type="checkbox" value="beta" /> Beta
        </label>
      </li>
      <li>
        <label for="id_NAME_OF_THE_ELEMENT_4">
          <input class="form-control" id="id_NAME_OF_THE_ELEMENT_4" name="NAME_OF_THE_ELEMENT" type="checkbox" value="omega" /> omega
        </label>
      </li>
    </ul>


fobi.contrib.plugins.form_elements.fields.date
----------------------------------------------
A ``Fobi`` Date form field plugin. Makes use of the
``django.forms.fields.DateField`` and ``django.forms.widgets.DateInput``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.date`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.date',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.fields.date_drop_down
--------------------------------------------------------
A ``Fobi`` Birthday form field plugin. Makes use of the
``django.forms.fields.DateField`` and
``django.forms.extras.widgets.SelectDateWidget``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.date_drop_down`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.date_drop_down',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.fields.datetime
--------------------------------------------------
A ``Fobi`` DateTime form field plugin. Makes use of the
``django.forms.fields.DateTimeField`` and
``django.forms.widgets.DateTimeInput``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.datetime`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.datetime',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.fields.decimal
-------------------------------------------------
A ``Fobi`` Decimal form field plugin. Makes use of the
``django.forms.fields.DecimalField`` and ``django.forms.widgets.NumberInput``
(falling back to ``django.forms.widgets.TextInput`` for older Django
versions).

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.decimal`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.decimal',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.fields.email
-----------------------------------------------
A ``Fobi`` Email form field plugin. Makes use of the
``django.forms.fields.EmailField`` and ``django.forms.widgets.TextInput``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.email`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.email',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.fields.file
----------------------------------------------
A ``Fobi`` File form field plugin. Makes use of the
``django.forms.fields.FileField`` and
``django.forms.widgets.ClearableFileInput``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.file`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.file',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) By default uploaded files are stored in the "fobi_plugins/file" directory
    of the media root. If you want to change the directory location,
    set the ``FOBI_PLUGIN_FIELDS_FILE_FILES_UPLOAD_DIR`` value to the desired
    (relative) path.

(5) You may optionally restrict uploaded files extensions by specifying the
    ``allowed_extensions`` field in the plugin.


fobi.contrib.plugins.form_elements.fields.float
-----------------------------------------------
A ``Fobi`` Integer form field plugin. Makes use of the
``django.forms.fields.FloatField`` and ``django.forms.widgets.NumberInput``
(falling back to ``django.forms.widgets.TextInput`` for older Django
versions).

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.float`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.float',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.fields.hidden
------------------------------------------------
A ``Fobi`` Hidden form field plugin. Makes use of the
``django.forms.fields.CharField`` and ``django.forms.widgets.HiddenInput``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.hidden`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.hidden',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.fields.input
-----------------------------------------------
A generic input form field plugin. Makes use of the
``django.forms.fields.Field`` and ``django.forms.widgets.Input``.
Comes with a lot of options you likely won't use every day.

The full list of supported HTML properties is listed below:

- autocomplete
- autofocus
- disabled
- list
- max
- min
- multiple
- pattern
- placeholder
- readonly
- step
- type

See `w3schools.com <http://www.w3schools.com/tags/tag_input.asp>`_ for further
explanations.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.input`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.input',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.fields.integer
-------------------------------------------------
A ``Fobi`` Integer form field plugin. Makes use of the
``django.forms.fields.IntegerField`` and ``django.forms.widgets.NumberInput``
(falling back to ``django.forms.widgets.TextInput`` for older Django
versions).

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.integer`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.integer',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.fields.ip_address
----------------------------------------------------
A ``Fobi`` Text form field plugin. Makes use of the
``django.forms.fields.GenericIPAddressField`` and
``django.forms.widgets.TextInput``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.ip_address`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.ip_address',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.fields.null_boolean
------------------------------------------------------
A ``Fobi`` NullBoolean form field plugin. Makes use of the
``django.forms.fields.NullBooleanField`` and
``django.forms.widgets.NullBooleanSelect``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.null_boolean`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.null_boolean',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.fields.password
--------------------------------------------------
A ``Fobi`` Password form field plugin. Makes use of the
``django.forms.fields.CharField`` and ``django.forms.widgets.PasswordInput``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.password`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.password',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.fields.radio
-----------------------------------------------
A ``Fobi`` Radio form field plugin. Makes use of the
``django.forms.fields.ChoiceField`` and ``django.forms.widgets.RadioSelect``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.radio`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.radio',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) By default, the submitted form value of `radio`
    elements is label (human readable representation of the value chosen).
    However, that part of the behaviour has been made configurable. You can
    choose between the following options:

    Consider the following list of (value, label) choices (the first element in
    the tuple is value, the second element is label):

    .. code-block:: python

        [
            ('alpha', 'Alpha'),
            ('beta', 'Beta'),
            ('gamma', 'Gamma'),
        ]

    .. code-block:: text

        - "val": `value` (example: "alpha").
        - "repr" (default): `label` (example: "Alpha").
        - "mix": `value (label)` (example: "Alpha (alpha)").

    Simply set the
    ``FOBI_FORM_ELEMENT_RADIO_SUBMIT_VALUE_AS`` assign one of the following
    values: "val", "repr" or "mix" to get the desired behaviour.

Usage
-----
You should be entering a single choice per line. Choice might
consist of just a single value or value/label pair.

For example:

.. code-block:: text

    1
    2
    alpha, Alpha
    beta, Beta
    omega

The following HTML would be made of:

.. code-block:: html

    <select id="id_NAME_OF_THE_ELEMENT" name="NAME_OF_THE_ELEMENT">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="alpha">Alpha</option>
      <option value="beta">Beta</option>
      <option value="omega">omega</option>
    </select>


fobi.contrib.plugins.form_elements.fields.range_select
------------------------------------------------------
A ``Fobi`` RangeSelect form field plugin. Makes use of the
``django.forms.fields.ChoiceField`` and ``django.forms.widgets.Select``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.range_select`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.range_select',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) Ranges are specified within the given min/max values. The default values
    are:

    .. code-block:: text

        - INITIAL: 50
        - INITIAL_MAX_VALUE: 100
        - INITIAL_MIN_VALUE: 0
        - MIN_VALUE: 0
        - MAX_VALUE: 100
        - STEP: 1

    However, you can override each of them in the settings of your project by
    prefixing correspondent names with `FOBI_FORM_ELEMENT_RANGE_SELECT_`:

    .. code-block:: text

        - FOBI_FORM_ELEMENT_RANGE_SELECT_INITIAL
        - FOBI_FORM_ELEMENT_RANGE_SELECT_INITIAL_MAX_VALUE
        - FOBI_FORM_ELEMENT_RANGE_SELECT_INITIAL_MIN_VALUE
        - FOBI_FORM_ELEMENT_RANGE_SELECT_MIN_VALUE
        - FOBI_FORM_ELEMENT_RANGE_SELECT_MAX_VALUE
        - FOBI_FORM_ELEMENT_RANGE_SELECT_STEP

(5) By default, the submitted form value of `range_select`
    elements is label (human readable representation of the value chosen).
    However, that part of the behaviour has been made configurable. You can
    choose between the following options:

    Consider the following list of (value, label) choices (the first element in
    the tuple is value, the second element is label):

    .. code-block:: python

        [
            ('alpha', 'Alpha'),
            ('beta', 'Beta'),
            ('gamma', 'Gamma'),
        ]

    .. code-block:: text

        - "val": `value` (example: "alpha").
        - "repr" (default): `label` (example: "Alpha").
        - "mix": `value (label)` (example: "Alpha (alpha)").

    Simply set the
    ``FOBI_FORM_ELEMENT_RANGE_SELECT_SUBMIT_VALUE_AS`` assign one of the
    following values: "val", "repr" or "mix" to get the desired behaviour.

fobi.contrib.plugins.form_elements.fields.regex
-----------------------------------------------
A ``Fobi`` Text form field plugin. Makes use of the
``django.forms.fields.RegexField`` and ``django.forms.widgets.TextInput``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.regex`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.regex',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.fields.select
------------------------------------------------
A ``Fobi`` Select form field plugin. Makes use of the
``django.forms.fields.ChoiceField`` and ``django.forms.widgets.Select``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.select`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.select',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) By default, the submitted form value of `select`
    elements is label (human readable representation of the value chosen).
    However, that part of the behaviour has been made configurable. You can
    choose between the following options:

    Consider the following list of (value, label) choices (the first element in
    the tuple is value, the second element is label):

    .. code-block:: python

        [
            ('alpha', 'Alpha'),
            ('beta', 'Beta'),
            ('gamma', 'Gamma'),
        ]

    .. code-block:: text

        - "val": `value` (example: "alpha").
        - "repr" (default): `label` (example: "Alpha").
        - "mix": `value (label)` (example: "Alpha (alpha)").

    Simply set the
    ``FOBI_FORM_ELEMENT_SELECT_SUBMIT_VALUE_AS`` assign one of the following
    values: "val", "repr" or "mix" to get the desired behaviour.

Usage
~~~~~
You should be entering a single choice per line. Choice might
consist of just a single value or value/label pair.

For example:

.. code-block:: text

    1
    2
    alpha, Alpha
    beta, Beta
    omega

The following HTML would be made of:

.. code-block:: html

    <select id="id_NAME_OF_THE_ELEMENT" name="NAME_OF_THE_ELEMENT">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="alpha">Alpha</option>
      <option value="beta">Beta</option>
      <option value="omega">omega</option>
    </select>


fobi.contrib.plugins.form_elements.fields.select_model_object
-------------------------------------------------------------
A ``Fobi`` Select Model Object form field plugin. Makes use of the
``django.forms.models.ModelChoiceField`` and ``django.forms.widgets.Select``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.select_model_object`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.select_model_object',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) Make sure to take a look at
    ``fobi.contrib.plugins.form_elements.fields.select_model_object.defaults.IGNORED_MODELS``.
    If necessary, override it in your `settings` as shown in the example below:

    .. code-block:: python

        FOBI_FORM_ELEMENT_SELECT_MODEL_OBJECT_IGNORED_MODELS = [
            'auth.User',
            'auth.Group',
        ]

(5) By default, the submitted form value of `select_model_object` elements is
    `app_label.model_name.object_pk.object_repr`. However, that part of the
    behaviour has been made configurable. You can choose between the following
    options:

    .. code-block:: text

        - "val": `app_label.model_name.object_pk.object_repr`.
        - "repr": `object_repr` (uses the ``__unicode__`` method of the model).
        - "mix" (default): `app_label.model_name.object_pk.object_repr`.

    Simply set the ``FOBI_FORM_ELEMENT_SELECT_MODEL_OBJECT_SUBMIT_VALUE_AS``
    assign one of the following values: "val", "repr" or "mix" to get the
    desired behaviour.


fobi.contrib.plugins.form_elements.fields.select_mptt_model_object
------------------------------------------------------------------
A ``Fobi`` Select MPTT Model Object form field plugin. Makes use of the
``mptt.fields.TreeNodeChoiceField`` and ``django.forms.widgets.Select``.

Installation
~~~~~~~~~~~~
Install `django-mptt`
#####################
Taken from django-mptt `Getting started
<http://django-mptt.github.io/django-mptt/tutorial.html#getting-started>`_.

1. Download ``django-mptt`` using pip by running:

.. code-block:: sh

    pip install django-mptt

2. Add ``mptt`` to the ``INSTALLED_APPS`` in your ``settings.py``.

Install `select_mptt_model_object` plugin
#########################################
(1) Add ``mptt`` and
    ``fobi.contrib.plugins.form_elements.fields.select_mptt_model_object``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'mptt',
            'fobi.contrib.plugins.form_elements.fields.select_mptt_model_object',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) Make sure to take a look at
    ``fobi.contrib.plugins.form_elements.fields.select_mptt_model_object.defaults.IGNORED_MODELS``.
    If necessary, override it in your `settings` as shown in the example below:

    .. code-block:: python

        FOBI_FORM_ELEMENT_SELECT_MPTT_MODEL_OBJECT_IGNORED_MODELS = [
            'auth.User',
            'auth.Group',
        ]

(5) By default, the submitted form value of `select_mptt_model_object` elements
    is `app_label.model_name.object_pk.object_repr`. However, that part of the
    behaviour has been made configurable. You can choose between the following
    options:

    .. code-block:: text

        - "val": `app_label.model_name.object_pk.object_repr`.
        - "repr": `object_repr` (uses the ``__unicode__`` method of the model).
        - "mix" (default): `app_label.model_name.object_pk.object_repr`.

    Simply set the ``FOBI_FORM_ELEMENT_SELECT_MPTT_MODEL_OBJECT_SUBMIT_VALUE_AS``
    assign one of the following values: "val", "repr" or "mix" to get the
    desired behaviour.


fobi.contrib.plugins.form_elements.fields.select_multiple
---------------------------------------------------------
A ``Fobi`` Select Multiple form field plugin. Makes use of the
``django.forms.fields.MultipleChoiceField`` and
``django.forms.widgets.SelectMultiple``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.select_multiple`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.select_multiple',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) By default, the submitted form value of `select_multiple`
    elements is label (human readable representation of the value chosen).
    However, that part of the behaviour has been made configurable. You can
    choose between the following options:

    Consider the following list of (value, label) choices (the first element in
    the tuple is value, the second element is label):

    .. code-block:: python

        [
            ('alpha', 'Alpha'),
            ('beta', 'Beta'),
            ('gamma', 'Gamma'),
        ]

    .. code-block:: text

        - "val": `value` (example: "alpha").
        - "repr" (default): `label` (example: "Alpha").
        - "mix": `value (label)` (example: "Alpha (alpha)").

    Simply set the
    ``FOBI_FORM_ELEMENT_SELECT_MULTIPLE_SUBMIT_VALUE_AS`` assign one of the
    following values: "val", "repr" or "mix" to get the desired behaviour.

Usage
~~~~~
You should be entering a single choice per line. Choice might
consist of just a single value or value/label pair.

For example:

.. code-block:: text

    1
    2
    alpha, Alpha
    beta, Beta
    omega

The following HTML would be made of:

.. code-block:: html

    <select id="id_NAME_OF_THE_ELEMENT" name="NAME_OF_THE_ELEMENT">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="alpha">Alpha</option>
      <option value="beta">Beta</option>
      <option value="omega">omega</option>
    </select>


fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects
-----------------------------------------------------------------------
A ``Fobi`` Select Multiple Model Objects form field plugin. Makes use of the
``django.forms.models.ModelMultipleChoiceField`` and
``django.forms.widgets.SelectMultiple``.

Installation
~~~~~~~~~~~~
(1) Add
    ``fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) Make sure to take a look at
    ``fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects.defaults.IGNORED_MODELS``.
    If necessary, override it in your `settings` as shown in the example below:

    .. code-block:: python

        FOBI_FORM_ELEMENT_SELECT_MULTIPLE_MODEL_OBJECTS_IGNORED_MODELS = [
            'auth.User',
            'auth.Group',
        ]

(5) By default, the submitted form value of `select_multiple_model_objects`
    elements is `app_label.model_name.object_pk.object_repr`. However, that
    part of the behaviour has been made configurable. You can choose between
    the following options:

    .. code-block:: text

        - "val": `app_label.model_name.object_pk.object_repr`.
        - "repr": `object_repr` (uses the ``__unicode__`` method of the model).
        - "mix" (default): `app_label.model_name.object_pk.object_repr`.

    Simply set the
    ``FOBI_FORM_ELEMENT_SELECT_MULTIPLE_MODEL_OBJECTS_SUBMIT_VALUE_AS`` assign
    one of the following values: "val", "repr" or "mix" to get the desired
    behaviour.


fobi.contrib.plugins.form_elements.fields.select_multiple_mptt_model_objects
----------------------------------------------------------------------------
A ``Fobi`` Select Multiple MPTT Model Objects form field plugin. Makes use of
the ``mptt.forms.TreeNodeMultipleChoiceField`` and
``django.forms.widgets.SelectMultiple``.

Installation
~~~~~~~~~~~~
Install `django-mptt`
#####################
Taken from django-mptt `Getting started
<http://django-mptt.github.io/django-mptt/tutorial.html#getting-started>`_.

1. Download ``django-mptt`` using pip by running:

.. code-block:: sh

    pip install django-mptt

2. Add ``mptt`` to the ``INSTALLED_APPS`` in your ``settings.py``.

Install `select_multiple_mptt_model_objects` plugin
###################################################
(1) Add
    ``fobi.contrib.plugins.form_elements.fields.select_multiple_mptt_model_objects``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'mptt',
            'fobi.contrib.plugins.form_elements.fields.select_multiple_mptt_model_objects',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) Make sure to take a look at
    ``fobi.contrib.plugins.form_elements.fields.select_multiple_mptt_model_objects.defaults.IGNORED_MODELS``.
    If necessary, override it in your `settings` as shown in the example below:

    .. code-block:: python

        FOBI_FORM_ELEMENT_SELECT_MULTIPLE_MPTT_MODEL_OBJECTS_IGNORED_MODELS = [
            'auth.User',
            'auth.Group',
        ]

(5) By default, the submitted form value of `select_multiple_mptt_model_objects`
    elements is `app_label.model_name.object_pk.object_repr`. However, that part
    of the behaviour has been made configurable. You can choose between the
    following options:

    .. code-block:: text

        - "val": `app_label.model_name.object_pk.object_repr`.
        - "repr": `object_repr` (uses the ``__unicode__`` method of the model).
        - "mix" (default): `app_label.model_name.object_pk.object_repr`.

    Simply set the
    ``FOBI_FORM_ELEMENT_SELECT_MULTIPLE_MPTT_MODEL_OBJECTS_SUBMIT_VALUE_AS``
    assign one of the following values: "val", "repr" or "mix" to get the
    desired behaviour.


fobi.contrib.plugins.form_elements.fields.select_multiple_with_max
------------------------------------------------------------------
A ``Fobi`` Select Multiple form field plugin with max choices. Makes use of
the ``django.forms.widgets.SelectMultiple``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.select_multiple_with_max``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.select_multiple_with_max',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) By default, the submitted form value of `select_multiple_with_max`
    elements is label (human readable representation of the value chosen).
    However, that part of the behaviour has been made configurable. You can
    choose between the following options:

    Consider the following list of (value, label) choices (the first element in
    the tuple is value, the second element is label):

    .. code-block:: python

        [
            ('alpha', 'Alpha'),
            ('beta', 'Beta'),
           ('gamma', 'Gamma'),
        ]

    .. code-block:: text

        - "val": `value` (example: "alpha").
        - "repr" (default): `label` (example: "Alpha").
        - "mix": `value (label)` (example: "Alpha (alpha)").

    Simply set the
    ``FOBI_FORM_ELEMENT_SELECT_MULTIPLE_WITH_MAX_SUBMIT_VALUE_AS`` assign one of the
    following values: "val", "repr" or "mix" to get the desired behaviour.

Usage
-----
You should be entering a single choice per line. Choice might
consist of just a single value or value/label pair. If you enter an integer in
the 'max_choices' field, the user can choose only <max_choices> or less choices.

For example:

.. code-block:: text

    1
    2
    alpha, Alpha
    beta, Beta
    omega

The following HTML would be made of:

.. code-block:: html

    <select id="id_NAME_OF_THE_ELEMENT" name="NAME_OF_THE_ELEMENT">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="alpha">Alpha</option>
      <option value="beta">Beta</option>
      <option value="omega">omega</option>
    </select>


fobi.contrib.plugins.form_elements.fields.slider
------------------------------------------------
A ``Fobi`` Percentage form field plugin. Makes use of the
``django.forms.fields.ChoiceField`` and ``django.forms.widgets.Select``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.slider`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.slider',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) Ranges are specified within the given min/max values. The default values
    are:

    .. code-block:: text

       - INITIAL: 50
       - INITIAL_MAX_VALUE: 100
       - INITIAL_MIN_VALUE: 0
       - MIN_VALUE: 0
       - MAX_VALUE: 100
       - STEP: 1

    However, you can override each of them in the settings of your project by
    prefixing correspondent names with `FOBI_FORM_ELEMENT_SLIDER_`:

    .. code-block:: text

       - FOBI_FORM_ELEMENT_SLIDER_INITIAL
       - FOBI_FORM_ELEMENT_SLIDER_INITIAL_MAX_VALUE
       - FOBI_FORM_ELEMENT_SLIDER_INITIAL_MIN_VALUE
       - FOBI_FORM_ELEMENT_SLIDER_MIN_VALUE
       - FOBI_FORM_ELEMENT_SLIDER_MAX_VALUE
       - FOBI_FORM_ELEMENT_SLIDER_STEP

(5) By default, the submitted form value of `slider`
    elements is label (human readable representation of the value chosen).
    However, that part of the behaviour has been made configurable. You can
    choose between the following options:

    Consider the following list of (value, label) choices (the first element in
    the tuple is value, the second element is label):

    .. code-block:: python

        [
            ('alpha', 'Alpha'),
            ('beta', 'Beta'),
            ('gamma', 'Gamma'),
        ]

    .. code-block:: text

        - "val": `value` (example: "alpha").
        - "repr" (default): `label` (example: "Alpha").
        - "mix": `value (label)` (example: "Alpha (alpha)").

    Simply set the
    ``FOBI_FORM_ELEMENT_SLIDER_SUBMIT_VALUE_AS`` assign one of the following
    values: "val", "repr" or "mix" to get the desired behaviour.

fobi.contrib.plugins.form_elements.fields.text
----------------------------------------------
A ``Fobi`` Text form field plugin. Makes use of the
``django.forms.fields.CharField`` and ``django.forms.widgets.TextInput``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.text`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.text',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.fields.textarea
--------------------------------------------------
A ``Fobi`` Textarea form field plugin. Makes use of the
``django.forms.fields.CharField`` and ``django.forms.widgets.Textarea``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.textarea`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.textarea',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.fields.time
----------------------------------------------
A ``Fobi`` DateTime form field plugin. Makes use of the
``django.forms.fields.TimeField`` and
``django.forms.widgets.TextInput``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.time`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.time',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.fields.url
---------------------------------------------
A ``Fobi`` URL form field plugin. Makes use of the
``django.forms.fields.URLField`` and ``django.forms.widgets.URLInput`` falling
back to ``django.forms.widgets.TextInput`` for older Django versions.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.url`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.url',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.security.captcha
---------------------------------------------------
A `CAPTCHA <http://en.wikipedia.org/wiki/CAPTCHA>`_ form field plugin. Makes
use of the `django-simple-captcha
<http://django-simple-captcha.readthedocs.io/en/latest/>`_.

Prerequisites
~~~~~~~~~~~~~
You will need ``libfreetype6``, otherwise ``django-simple-captcha`` won't work.

.. code-block:: sh

    sudo apt-get install libfreetype6-dev

Installation
~~~~~~~~~~~~
Install `django-simple-captcha`
###############################
Taken from django-simple-captcha `installation instructions
<http://django-simple-captcha.readthedocs.org/en/latest/usage.html#installation>`_.

(1) Download ``django-simple-captcha`` using pip by running:

    .. code-block:: sh

        pip install django-simple-captcha

(2) Add ``captcha`` to the ``INSTALLED_APPS`` in your ``settings.py``.

(3) Run ``python manage.py migrate``.

(4) Add an entry to your ``urls.py``:

    .. code-block:: python

        urlpatterns += [
            url(r'^captcha/', include('captcha.urls')),
        ]

Install `fobi` Captcha plugin
#############################
(1) Add ``fobi.contrib.plugins.form_elements.security.captcha`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.security.captcha',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) In order to have nicer text input widget, add the following line
    to your settings (if you're using bootstrap3 theme):

    .. code-block:: python

        CAPTCHA_TEXT_FIELD_TEMPLATE = 'bootstrap3/captcha/text_field.html'

    For foundation5 theme add the following line:

    .. code-block:: python

        CAPTCHA_TEXT_FIELD_TEMPLATE = 'foundation5/captcha/text_field.html'

Troubleshooting and usage limitations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In combination with other captcha solutions
###########################################
At the moment, you can't use both ``CAPTCHA``
(fobi.contrib.plugins.form_elements.security.captcha) and ``ReCAPTCHA``
(fobi.contrib.plugins.form_elements.security.recaptcha) plugins alongside due
to app name collision of the ``django-simple-captcha`` and ``django-recaptcha``
packages.

Usage
~~~~~
Note, that unlike most of the other form element plugins, default
value for the ``required`` attribute is True, which makes the Captcha
obligatory. Although you could still set it to False, it does not make
much sense to do so.


fobi.contrib.plugins.form_elements.security.honeypot
----------------------------------------------------
A `Honeypot <http://en.wikipedia.org/wiki/Honeypot_%28computing%29>`_
form field plugin. Just another anti-spam technique.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.security.honeypot`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.security.honeypot',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_elements.security.recaptcha
-----------------------------------------------------
A `ReCAPTCHA <http://en.wikipedia.org/wiki/ReCAPTCHA>`_ form field plugin.
Makes use of the `django-recaptcha
<https://github.com/praekelt/django-recaptcha>`_.

Installation
~~~~~~~~~~~~
Install `django-recaptcha`
##########################
(1) Download ``django-recaptcha`` using pip by running:

    .. code-block:: sh

        pip install django-recaptcha

(2) Add ``captcha`` to the ``INSTALLED_APPS`` in your ``settings.py``.

(3) Run ``python manage.py migrate``.

Install `fobi` ReCAPTCHA plugin
###############################
(1) Add ``fobi.contrib.plugins.form_elements.security.recaptcha`` to the
   ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.security.recaptcha',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
   the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) Specify the following ReCAPTCHA credentials in your settings:

    .. code-block:: text

       - ``RECAPTCHA_PUBLIC_KEY``
       - ``RECAPTCHA_PRIVATE_KEY``

Troubleshooting and usage limitations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In combination with other captcha solutions
###########################################
At the moment, you can't use both ``CAPTCHA``
(fobi.contrib.plugins.form_elements.security.captcha) and ``ReCAPTCHA``
(fobi.contrib.plugins.form_elements.security.recaptcha) plugins alongside due
to app name collision of the ``django-simple-captcha`` and ``django-recaptcha``
packages.

If you happen to see errors like "Input error: k: Format of site key was
invalid", make sure to have defined (and filled in properly) the
``RECAPTCHA_PUBLIC_KEY`` and ``RECAPTCHA_PRIVATE_KEY`` in your settings.py.
See the `following <https://github.com/praekelt/django-recaptcha/issues/32>`_
thread for more information.

Usage
~~~~~
Note, that unlike most of the other form element plugins, default
value for the ``required`` attribute is True, which makes the ReCaptcha
obligatory. Although you could still set it to False, it does not make
much sense to do so.


fobi.contrib.plugins.form_elements.test.dummy
---------------------------------------------
A ``Fobi`` Dummy form element plugin. Created for testing purposes.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.test.dummy`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.test.dummy',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_handlers.db_store
-------------------------------------------
A ``Fobi`` Database Store form-/wizard- handler plugin. Saves submitted form
data into the ``SavedFormDataEntry``/``SavedFormWizardDataEntry`` models.

Dependencies
~~~~~~~~~~~~
The `xlwt <https://pypi.python.org/pypi/xlwt>`_ package is required
(optional) for XLS export. If not present, export format falls back
to CSV.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_handlers.db_store`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_handlers.db_store',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py migrate

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) Add db_store form handler plugin URLs to the urls.py of your project.

    .. code-block:: python

        urlpatterns = [
            # DB Store plugin URLs
            url(r'^fobi/plugins/form-handlers/db-store/',
                include('fobi.contrib.plugins.form_handlers.db_store.urls')),
        ]

    For form wizards do:

    .. code-block:: python

        urlpatterns = [
            # DB Store plugin URLs
            url(r'^fobi/plugins/form-wizard-handlers/db-store/',
                include('fobi.contrib.plugins.form_handlers.db_store.urls.'
                        'form_wizard_handlers')),
        ]


fobi.contrib.plugins.form_handlers.http_repost
----------------------------------------------
A ``Fobi`` HTTP Repost form handler plugin. Submits the form
data as is to the given endpoint.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_handlers.http_repost`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_handlers.http_repost',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


fobi.contrib.plugins.form_handlers.mail
---------------------------------------
A ``Fobi`` Mail form handler plugin. Submits the form
data by email to the specified email address.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_handlers.mail`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_handlers.mail',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.


mailchimp_importer
------------------
A ``django-fobi`` integration with MailChimp.

This plugin makes it possible to import a form from a MailChimp list. A typical
list URL would be `this <https://us5.admin.mailchimp.com/lists/>`_. In the
listing you would see list names and `Stats` at the right corner. If you click
on it you would see the `Settings` link. Follow it and scroll to the bottom for
the unique id for your list. Now, if you have been successfully authenticated
to the MailChimp API using your API_KEY, you could call the `lists.merge_vars`
method for getting the form. API_KEY could be obtained from the MailChimp
in the `Account API <https://us5.admin.mailchimp.com/account/api/>`_.

For additional information on MailChimp import see the following `article
<http://kb.mailchimp.com/lists/managing-subscribers/manage-list-and-signup-form-fields>`_.

Prerequisites
~~~~~~~~~~~~~
Python wrapper for the Mailchimp:

.. code-block:: sh

   pip install mailchimp

If you are using Django 1.8 or greater, you would need `django-formtools`
package as well:

.. code-block:: sh

   pip install django-formtools

Installation
~~~~~~~~~~~~
your_project/settings.py
########################
.. code-block:: python

    INSTALLED_APPS = list(INSTALLED_APPS)
    INSTALLED_APPS += [
        'fobi.contrib.plugins.form_importers.mailchimp_importer',
    ]

How it works
~~~~~~~~~~~~
Assuming that you have configured the `mailchimp_importer` plugin properly and
have the Django running locally on port 8000, accessing the following URL would
bring you to the MailChimp form import wizard.

- http://localhost:8000/en/fobi/forms/importer/mailchimp/

On the first step you would be asked to provide your API_KEY, which is used
to authenticate to the MailChimp in order to fetch your list- and form-
information. The key isn't stored/saved/remembered. Next time you want to
import a form from the same account, you would have to provide it again.

Development status
~~~~~~~~~~~~~~~~~~
This part of code is alpha, which means it experimental and needs improvements.

See the `TODOS <https://raw.githubusercontent.com/barseghyanartur/django-fobi/master/TODOS.rst>`_
for the full list of planned-, pending- in-development- or to-be-implemented
features.

If you want to improve it or did make it working, please, make a pull request.


fobi.contrib.themes.bootstrap3
------------------------------
A ``django-fobi`` Bootstrap 3 theme. Based on the ??? template.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.themes.bootstrap3`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.themes.bootstrap3',
            # ...
        )

(2) Specify ``bootstrap3`` as a default theme in your ``settings.py``:

    .. code-block:: python

        FOBI_DEFAULT_THEME = 'bootstrap3'


fobi.contrib.themes.djangocms_admin_style_theme
-----------------------------------------------
A ``django-fobi`` theme in a style of ``djangocms-admin-style`` admin.
Relies on ``djangocms-admin-style`` package and some jQuery UI only.

jQuery UI "Smoothness" theme comes from `here <http://jqueryui.com/>`_.

Installation
~~~~~~~~~~~~
Install `djangocms-admin-style`
###############################
See the original `installation instructions
<https://pypi.python.org/pypi/djangocms-admin-style#installation>`_.

(1) Install the ``djangocms-admin-style`` package.

    .. code-block:: sh

        pip install djangocms-admin-style

(2) Add ``djangocms_admin_style`` to your ``INSTALLED_APPS`` just before
    ``django.contrib.admin``.

Install `fobi.contrib.themes.djangocms_admin_style_theme` theme
###############################################################
(1) Add ``fobi.contrib.themes.djangocms_admin_style_theme`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.themes.djangocms_admin_style_theme',
            # ...
        )

(2) Specify ``djangocms_admin_style_theme`` as a default theme in your
    ``settings.py``:

    .. code-block:: python

        FOBI_DEFAULT_THEME = 'djangocms_admin_style_theme'


fobi.contrib.themes.foundation5
-------------------------------
A ``django-fobi`` Foundation 5 theme. Based on the ??? template, but
entire JS and CSS are taken from Foundation 5 version 5.4.0. The
`following <http://zurb.com/playground/foundation-icon-fonts-3>`_ icon set
was used.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.themes.foundation5`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.themes.foundation5',
            # ...
        )

(2) Specify ``foundation5`` as a default theme in your ``settings.py``:

    .. code-block:: python

        FOBI_DEFAULT_THEME = 'foundation5'


fobi.contrib.themes.simple
--------------------------
A ``django-fobi`` theme in a style of Django admin. Relies on Django-admin
and some jQuery UI only.

jQuery UI "Django" theme comes from `here
<http://jqueryui.com/themeroller/#!zThemeParams=5d000001004406000000000000003d8888d844329a8dfe02723de3e5702531794cd29e6ed19a93500bec10499630a65410e41ead4c600a0cf20b340bb5e2f7caf959ed396c92b6035d90d24df6690df466ac448d4e1c19e7fa7c9a0839be4194bf063920ea1af50a8118ad9351aef9ad563b3a37cd36e7495624fe90fc1dea5e04da5c3bc1b05fbaabd52118818b56bf553915a91d00d5f3e6d7170d10432c322c435542e105860d86f5aff187d2c5fd576473852b0a11341f0f25f44acc20995011eacc757f738992c953dbc7a1465ffdb121cb5442e4eab396fc706de223fe0fc9c95a7d117899db8aa67ebf8d5b547778d8301f54035188d6f909c525eba7227394e77fa275211eca51b9a828c4266d31e94e9ad9d094e2d5313fc059abfb69532833a14287184b79fd3e769e36246d5f0b3f8fb23a589e0ce916bb6b074faf8dbac4a8f379a481f14755e3043f7a684ccde3630e138ed0ed7e0e4af40517ffcf11fd3581d7da611c79f6481f3e02d2d1645c776ada5da686c7e62ad51e829cf9ba6ec42e0a7afa3dcaed299f70bd4a28055aa8c0f6d9d1d5f362280aff2c9be5d5355c0e15c5145565ac449331112dd272ba1c7f326f3502465763e229cdc80dec6054935a2c4ef8b62e3f00a7bee54e59377abda70f8f3fbd15004573b3372aaddd79545e195b14abddcb8dc730dc65504265aece22ee6158670dbc2d11f314ffebbc5e3d>`_.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.themes.simple`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.themes.simple',
            # ...
        )

(2) Specify ``simple`` as a default theme in your ``settings.py``:

    .. code-block:: python

        FOBI_DEFAULT_THEME = 'simple'


