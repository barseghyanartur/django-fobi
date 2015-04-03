===============================================
django-fobi
===============================================
`django-fobi` (later on named just `fobi`) is a customisable, modular,
user- and developer- friendly form generator/builder application for Django. 
With `fobi` you can build Django forms using an intiutive GUI, save or
mail posted form data. API allows you to build your own form elements and
form handlers (mechanisms for handling the submitted form data).

Prerequisites
===============================================
- Django 1.5, 1.6, 1.7, 1.8
- Python >= 2.6.8, >= 2.7, >= 3.3

Note, that Django 1.8 is not yet proclaimed to be flawlessly supported. The
core and contrib packages (with no additional dependencies) have been tested
against the latest stable Django 1.8 release. All tests have successfully
passed, although it's yet too early to claim that Django 1.8 is fully
supported.

Key concepts
===============================================
- Each form consists of elements. Form elements are divided
  into two groups:

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

Note, that Fobi does not require django-admin and administrative rights/
permissions to access the UI, although almost seamless integration with
django-admin is implemented through the ``simple`` theme.

Main features and highlights
===============================================
- User-friendly GUI to quickly build forms.
- Large variety of `Bundled form element plugins`_. Most of the Django fields
  are supported. `HTML5 fields`_ are supported as well.
- Anti-spam solutions like `CAPTCHA
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/security/captcha>`_,
  `ReCAPTCHA
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/security/recaptcha>`_
  or `Honeypot
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/security/honeypot>`_
  come out of the box (CAPTCHA and ReCAPTCHA do require additional third-party
  apps to be installed).
- In addition to standard form elements, there are cosmetic (presentational)
  form elements (for adding a piece of text, image or a embed video)
  alongside standard form elements.
- Data handling in plugins (form handlers). Save the data, mail it to some
  address or repost it to some other endpoint. See the
  `Bundled form handler plugins`_ for more information.
- Developer-friendly API, which allows to edit existing or build new form 
  fields and handlers without touching the core.
- Support for custom user model.
- `Theming`_. There are 4 ready to use `Bundled themes`_: "Bootstrap 3",
  "Foundation 5", "Simple" (with editing interface in style of Django admin)
  and "DjangoCMS admin style" theme (which is another simple theme with editing
  interface in style of `djangocms-admin-style
  <https://github.com/divio/djangocms-admin-style>`_).
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
- Data export (`db_store 
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_handlers/db_store>`_
  form handler plugin) into XLS/CSV format.

Roadmap
===============================================
Some of the upcoming/in-development features/improvements are:

- Form importers (and as a part of it - MailChimp integration,
  which would allow to import forms from MailChimp into Fobi using
  a user-friendly wizard).
- Fieldsets.

See the `TODOS <https://raw.githubusercontent.com/barseghyanartur/django-fobi/master/TODOS.rst>`_
for the full list of planned-, pending- in-development- or to-be-implemented
features.

Some screenshots
===============================================
See the documentation for some screen shots:

- `PythonHosted <http://pythonhosted.org/django-fobi/#screenshots>`_
- `ReadTheDocs <http://django-fobi.readthedocs.org/en/latest/#screenshots>`_

Demo
===============================================
Live demo
-----------------------------------------------
See the `live demo app <https://django-fobi.herokuapp.com/>`_ on Heroku.

Credentials:

- username: test_user
- password: test_user

Run demo locally
-----------------------------------------------
In order to be able to quickly evaluate the `Fobi`, a demo app (with a quick
installer) has been created (works on Ubuntu/Debian, may work on other Linux
systems as well, although not guaranteed). Follow the instructions below for
having the demo running within a minute.

Grab the latest `django_fobi_example_app_installer.sh`:

.. code-block:: none

    $ wget https://raw.github.com/barseghyanartur/django-fobi/stable/examples/django_fobi_example_app_installer.sh

Assign execute rights to the installer and run the
`django_fobi_example_app_installer.sh`:

.. code-block:: none

    $ chmod +x django_fobi_example_app_installer.sh
    $ ./django_fobi_example_app_installer.sh

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
===============================================
See the `quick start <http://pythonhosted.org/django-fobi/quickstart.html>`_.

Installation
===============================================

(1) Install latest stable version from PyPI:

.. code-block:: none

    $ pip install django-fobi

Or latest stable version from GitHub:

.. code-block:: none

    $ pip install -e git+https://github.com/barseghyanartur/django-fobi@stable#egg=django-fobi

Or latest stable version from BitBucket:

.. code-block:: none

    $ pip install -e hg+https://bitbucket.org/barseghyanartur/django-fobi@stable#egg=django-fobi

(2) Add `fobi` to ``INSTALLED_APPS`` of the your projects' Django settings.
    Furthermore, all themes and plugins to be used, shall be added to the
    ``INSTALLED_APPS`` as well. Note, that if a plugin has additional
    dependencies, you should be mentioning those in the ``INSTALLED_APPS``
    as well.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        # Fobi core
        'fobi',

        # Fobi themes
        'fobi.contrib.themes.bootstrap3', # Bootstrap 3 theme
        'fobi.contrib.themes.foundation5', # Foundation 5 theme
        'fobi.contrib.themes.simple', # Simple theme

        # Fobi form elements - fields
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

        # Fobi form elements - content elements
        'fobi.contrib.plugins.form_elements.test.dummy',
        'easy_thumbnails', # Required by `content_image` plugin
        'fobi.contrib.plugins.form_elements.content.content_image',
        'fobi.contrib.plugins.form_elements.content.content_text',
        'fobi.contrib.plugins.form_elements.content.content_video',

        # Form handlers
        'fobi.contrib.plugins.form_handlers.db_store',
        'fobi.contrib.plugins.form_handlers.http_repost',
        'fobi.contrib.plugins.form_handlers.mail',

        # Other project specific apps
        'foo', # Test app
        # ...
    )


(3) Make appropriate changes to the ``TEMPLATE_CONTEXT_PROCESSORS`` of the your
    projects' Django settings.

And the following to the context processors.

.. code-block:: python

    TEMPLATE_CONTEXT_PROCESSORS = (
        # ...
        "fobi.context_processors.theme",
        # ...
    )

Make sure that ``django.core.context_processors.request`` is in
``TEMPLATE_CONTEXT_PROCESSORS`` too.

(4) Configure URLs

Add the following line to urlpatterns of your `urls` module.

.. code-block:: python

    # View URLs
    url(r'^fobi/', include('fobi.urls.view')),

    # Edit URLs
    url(r'^fobi/', include('fobi.urls.edit')),

Note, that some plugins require additional URL includes. For instance, if you
listed the `fobi.contrib.plugins.form_handlers.db_store` form handler plugin
in the ``INSTALLED_APPS``, you should mention the following in `urls` module.

.. code-block:: python

    # DB Store plugin URLs
    url(r'^fobi/plugins/form-handlers/db-store/',
        include('fobi.contrib.plugins.form_handlers.db_store.urls')),

View URLs are put separately from edit URLs in order to make it possible
to prefix the edit URLs differently. For example, if you're using the
"Simple" theme, you would likely want to prefix the edit URLs with "admin/"
so that it looks more like django-admin.

Creating a new form element plugin
===============================================
Form element plugins represent the elements of which the forms is made:
Inputs, checkboxes, textareas, files, hidden fields, as well as pure
presentational elements (text or image). Number of form elements in a form
is not limited.

Presentational form elements are inherited from ``fobi.base.FormElementPlugin``.

The rest (real form elements, that are supposed to have a value)
are inherited from ``fobi.base.FormFieldPlugin``.

You should see a form element plugin as a Django micro app, which could have
its' own models, admin interface, etc.

Fobi comes with several bundled form element plugins. Do check the source code
as example.

Let's say, you want to create a textarea form element plugin.

There are several properties, each textarea should have. They are:

- `label` (string): HTML label of the textarea.
- `name` (string): HTML name of the textarea.
- `initial` (string): Initial value of the textarea.
- `required` (bool): Flag, which tells us whether the field is required or
  optional.

Let's name that plugin `sample_textarea`. The plugin directory should then have
the following structure.

.. code-block:: none

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
-----------------------------------------------
Step by step review of a how to create and register a plugin and plugin
widgets. Note, that Fobi autodiscovers your plugins if you place them into a
file named `fobi_form_elements.py` of any Django app listed in
``INSTALLED_APPS`` of your Django projects' settings module.

path/to/sample_textarea/fobi_form_elements.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A single form element plugin is registered by its' UID.

Required imports.

.. code-block:: python

    from django import forms
    from fobi.base import FormFieldPlugin, form_element_plugin_registry
    from path.to.sample_textarea.forms import SampleTextareaForm

Defining the Sample textarea plugin.

.. code-block:: python

    class SampleTextareaPlugin(FormFieldPlugin):
        uid = "sample_textarea"
        name = "Sample Textarea"
        form = SampleTextareaForm
        group = "Samples" # Group to which the plugin belongs to
        
        def get_form_field_instances(self):
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
the successful form submittion. In such cases, you will need to define a 
``submit_plugin_form_data`` method in the plugin, which accepts the 
following arguments:

- `form_entry` (fobi.models.FormEntry): Form entry, which is being submitted.
- `request` (django.http.HttpRequest): The Django HTTP request.
- `form` (django.forms.Form): Form object (a valid one, which contains 
  the ``cleaned_data`` attribute).
  
Example (taken from fobi.contrib.plugins.form_elements.fields.file):

.. code-block:: python

    def submit_plugin_form_data(self, form_entry, request, form):
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Why to have another file for defining forms? Just to keep the code clean and
less messy, although you could perfectly define all your plugin forms in the
module `fobi_form_elements.py`, it's recommended to keep it separate.

Take into consideration, that `forms.py` is not an autodiscovered file pattern.
All your form element plugins should be registered in modules named
`fobi_form_elements.py`.

Required imports.

.. code-block:: python

    from django import forms
    from fobi.base import BasePluginForm

Form for for ``SampleTextareaPlugin`` form element plugin.

.. code-block:: python

    class SampleTextareaForm(forms.Form, BasePluginForm):
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
<https://github.com/barseghyanartur/django-fobi/blob/stable/src/fobi/contrib/plugins/form_elements/content/image/forms.py>`_.

.. code-block:: python

    def save_plugin_data(self, request=None):
        """
        Saving the plugin data and moving the file.
        """
        file_path = self.cleaned_data.get('file', None)
        if file_path:
            saved_image = handle_uploaded_file(IMAGES_UPLOAD_DIR, file_path)
            self.cleaned_data['file'] = saved_image

path/to/sample_textarea/widgets.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Required imports.

.. code-block:: python

    from fobi.base import FormElementPluginWidget

Defining the base plugin widget.

.. code-block:: python

    class BaseSampleTextareaPluginWidget(FormElementPluginWidget):
        # Same as ``uid`` value of the ``SampleTextareaPlugin``.
        plugin_uid = "sample_textarea"

path/to/sample_layout/fobi_form_elements.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Register in the registry (in some module which is for sure to be loaded; it's
handy to do it in the theme module).

Required imports.

.. code-block:: python

    from fobi.base import form_element_plugin_widget_registry
    from path.to.sample_textarea.widgets import BaseSampleTextareaPluginWidget

Define the theme specific plugin.

.. code-block:: python

    class SampleTextareaPluginWidget(BaseSampleTextareaPluginWidget):
        theme_uid = 'bootstrap3' # Theme for which the widget is loaded
        media_js = ['sample_layout/js/fobi.plugins.form_elements.sample_textarea.js',]
        media_css = ['sample_layout/css/fobi.plugins.form_elements.sample_textarea.css',]

Register the widget.

.. code-block:: python

    form_element_plugin_widget_registry.register(SampleTextareaPluginWidget)

Form element plugin final steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now, that everything is ready, make sure your plugin module is added to
``INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'path.to.sample_textarea',
        # ...
    )

Afterwards, go to terminal and type the following command.

.. code-block:: none

    $ ./manage.py fobi_sync_plugins

If your HTTP server is running, you would then be able to see the new plugin
in the edit form interface.

Dashboard URL: http://127.0.0.1:8000/fobi/

Note, that you have to be logged in, in order to use the dashboard. If your
new plugin doesn't appear, set the ``FOBI_DEBUG`` to True in your Django's
local settings module, re-run your code and check console for error
notifications.

Creating a new form handler plugin
===============================================
Form handler plugins handle the form data. Fobi comes with several bundled
form handler plugins, among which is the ``db_store`` and ``mail`` plugins,
which are responsible for saving the submitted form data into the database
and mailing the data to recipients specified. Number of form handlers in a
form is not limited. Certain form handlers are not configurable (for
example the ``db_store`` form handler isn't), while others are (``mail``,
``http_repost``).

You should see a form handler as a Django micro app, which could have its' own
models, admin interface, etc.

By default, it's possible to use a form handler plugin multiple time per form.
If you wish to allow form handler plugin to be used only once in a form,
set the ``allow_multiple`` property of the plugin to False.

As said above, Fobi comes with several bundled form handler plugins. Do check
the source code as example.

Define and register the form handler plugin
-----------------------------------------------
Let's name that plugin `sample_mail`. The plugin directory should then have
the following structure.

.. code-block:: none

    path/to/sample_mail/
    ├── __init__.py
    ├── fobi_form_handlers.py # Where plugins are defined and registered
    └── forms.py # Plugin configuration form

Form handler plugins should be registered in "fobi_form_handlers.py" file.
Each plugin module should be put into the ``INSTALLED_APPS`` of your Django
projects' settings.

path/to/sample_mail/fobi_form_handlers.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
        uid = "sample_mail"
        name = _("Sample mail")
        form = SampleMailForm

        def run(self, form_entry, request, form):
            send_mail(
                self.data.subject,
                json.dumps(form.cleaned_data),
                self.data.from_email,
                [self.data.to_email],
                fail_silently = True
                )

Some form handlers are configurable, some others not. In order to
have a user friendly way of showing the form handler settings, what's
sometimes needed, a ``plugin_data_repr`` method has been introducd.
Simplest implementation of it would look as follows:

.. code-block:: python

    def plugin_data_repr(self):
        """
        Human readable representation of plugin data.

        :return string:
        """
        return self.data.__dict__

path/to/sample_mail/forms.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If plugin is configurable, it has configuration data. A single form may have
unlimited number of same plugins. Imagine, you want to have different subjects
and additional body texts for different user groups. You could then assign two
form handler ``mail`` plugins to the form. Of course, saving the posted form
data many times does not make sense, but it's up to the user. So, in case if
plugin is configurable, it should have a form.

Why to have another file for defining forms? Just to keep the code clean and
less messy, although you could perfectly define all your plugin forms in the
module `fobi_form_handlers.py`, it's recommended to keep it separate.

Take into consideration, that `forms.py` is not an autodiscovered file pattern.
All your form handler plugins should be registered in modules named
`fobi_form_handlers.py`.

Required imports.

.. code-block:: python

    from django import forms
    from django.utils.translation import ugettext_lazy as _
    from fobi.base import BasePluginForm

Defining the form for Sample mail handler plugin.

.. code-block:: python

    class MailForm(forms.Form, BasePluginForm):
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
        body = forms.CharField(label=_("Body"), required = False,
                               widget=forms.widgets.Textarea)

After the plugin has been processed, all its' data is available in a
``plugin_instance.data`` container (for example,
``plugin_instance.data.subject`` or ``plugin_instance.data.from_name``).

Prioritise the excecution order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Some form handlers shall be executed prior others. A good example of such, is
a combination of "mail" and "db_save" form handlers for the form. In case of
large files posted, submittion of form data would fail if "mail" plugin would
be executed after "db_save" has been executed. That's why it's possible to
prioritise that ordering in a ``FOBI_FORM_HANDLER_PLUGINS_EXECUTION_ORDER``
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
        """
        Adding a link to view the saved form enties.

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Do not forget to add the form handler plugin module to ``INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'path.to.sample_mail',
        # ...
    )

Afterwards, go to terminal and type the following command.

.. code-block:: none

    $ ./manage.py fobi_sync_plugins

If your HTTP server is running, you would then be able to see the new plugin
in the edit form interface.

Creating a form callback
===============================================
Form callbacks are additional hooks, that are executed on various stages of
the form submission.

Let's place the callback in the `foo` module. The plugin directory should then
have the following
structure.

.. code-block:: none

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
        stage = CALLBACK_FORM_VALID

        def callback(self, form_entry, request, form):
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
===============================================
Custom action for the form
-----------------------------------------------
Sometimes, you would want to specify a different action for the form.
Although it's possible to define a custom form action (``action`` field
in the "Form properties" tab), you're advised to use the ``http_repost`` 
plugin instead, since then the form would be still validated locally
and only then the valid data, as is, would be sent to the desired
endpoint.

Take in mind, that if both cases, if CSRF protection is enabled on
the endpoint, your post request would result an error.

When you want to customise too many things
-----------------------------------------------
Fobi, with its' flexible form elements, form handlers and form callbacks
is very customisable. However, there might be cases when you need to
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
===============================================
`Fobi` comes with theming API. While there are several ready-to-use themes:

- "Bootstrap 3" theme
- "Foundation 5" theme
- "Simple" theme in (with editing interface in style of the Django admin)
- "DjangoCMS admin style" theme (which is another simple theme with editing
  interface in style of `djangocms-admin-style`)

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
-----------------------------------------------

Let's place the theme in the `sample_theme` module. The theme directory 
should then have the following structure.

.. code-block:: none

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
        """
        Sample theme.
        """
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
in order to use them later in templates (rememeber, current theme object
is always available in templates under name `fobi_theme`).

For such cases you would need to define a variable in your project's settings
module, called ``FOBI_CUSTOM_THEME_DATA``. See the following code as example:

.. code-block:: python

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
theme implemention are marked with three asterics (\*\*\*):

.. code-block:: none

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
-----------------------------------------------
As said above, making your own theme from scratch could be costy. Instead,
you can override/reuse an existing one and change it to your needs with
minimal efforts. See the `override simple theme
<https://github.com/barseghyanartur/django-fobi/tree/master/examples/simple/override_simple_theme/>`_
example. In order to see it in action, run the project with
`settings_override_simple_theme
<https://github.com/barseghyanartur/django-fobi/blob/master/examples/simple/settings_override_simple_theme.py>`_
option:

.. code-block:: none

    ./manage.py runserver --settings=settings_override_simple_theme

Details explained below.

Directory structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: none

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Overriding the "simple" theme.

.. code-block:: python

    __all__ = ('MySimpleTheme',)

    from fobi.base import theme_registry

    from fobi.contrib.themes.simple.fobi_themes import SimpleTheme

    class MySimpleTheme(SimpleTheme):
        html_classes = ['my-simple-theme',]
        base_view_template = 'override_simple_theme/base_view.html'
        form_ajax = 'override_simple_theme/snippets/form_ajax.html'

Register the overridden theme. Note, that it's important to set the `force`
argument to True, in order to override the original theme. Force can be
applied only once (for a overridden element).

.. code-block:: python

    theme_registry.register(MySimpleTheme, force=True)

templates/override_simple_theme/base_view.html
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

Permissions
===============================================
Plugin system allows administrators to specify the access rights to every
plugin. Fobi permissions are based on Django Users and User Groups. Access
rights are managable via Django admin ("/admin/fobi/formelement/",
"/admin/fobi/formhandler/"). If user doesn't have the rights to access plugin,
it doesn't appear on his form even if has been added to it (imagine, you have
once granted the right to use the news plugin to all users, but later on
decided to limit it to Staff members group only). Note, that superusers have
access to all plugins.

.. code-block:: none

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
===============================================
There are several management commands available.

- `fobi_find_broken_entries`. Find broken form element/handler entries that
  occur when some plugin which did exist in the system, no longer exists.
- `fobi_sync_plugins`. Should be ran each time a new plugin is being added to
  the Fobi.
- `fobi_update_plugin_data`. A mechanism to update existing plugin data in 
  case if it had become invalid after a change in a plugin. In order for it
  to work, each plugin should implement and ``update`` method, in which the
  data update happens.

Tuning
===============================================
There are number of Dash settings you can override in the settings module of
your Django project:

- `FOBI_RESTRICT_PLUGIN_ACCESS` (bool): If set to True, (Django) permission 
  system for dash plugins is enabled. Defaults to True. Setting this to False
  makes all plugins available for all users.
- `FOBI_DEFAULT_THEME` (str): Active (default) theme UID. Defaults to
  "bootstrap3".
- `FORM_HANDLER_PLUGINS_EXECUTION_ORDER` (list of tuples): Order in which the
  form handlers are executed. See the "Prioritise the excecution order"
  section for details.

For tuning of specific contrib plugin, see the docs in the plugin directory.

Bundled plugins and themes
===============================================
Fobi ships with number of bundled form element- and form handler- plugins, 
as well as themes which are ready to be used as is.

Bundled form element plugins
-----------------------------------------------
Below a short overview of the form element plugins. See the README.rst file
in directory of each plugin for details.

Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
- `Email
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/email/>`_
- `File
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/file/>`_
- `Float
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/float>`_
- `Hidden
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/hidden/>`_
- `Password
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/password/>`_
- `Radio select (radio button)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/radio/>`_
- `Input
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/input/>`_
- `IP address
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/ip_address>`_
- `Integer
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/integer/>`_
- `Null boolean
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/null_boolean>`_
- `Select (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select/>`_
- `Select model object (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select_model_object/>`_
- `Select multiple (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select_multiple/>`_
- `Slug
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/slug>`_
- `Select multiple model objects (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select_multiple_model_objects/>`_
- `Text
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/text/>`_
- `Textarea
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/textarea/>`_
- `Time
  <https://github.com/barseghyanartur/django-fobi/tree/master/src/fobi/contrib/plugins/form_elements/fields/time>`_
- `URL
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/url/>`_

Content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Content plugins are presentational plugins, that make your forms look more
complete and content rich.

- `Content image
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/content/content_image/>`_:
  Insert an image.
- `Content text
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/content/content_text/>`_:
  Add text.
- `Content video
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/content/content_video/>`_:
  Add an embed YouTube or Vimeo video.

Security
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- `CAPTCHA
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/security/captcha/>`__:
  Captcha integration. Requires ``django-simple-captcha`` package.
- `ReCAPTCHA
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/security/recaptcha/>`__:
  Captcha integration. Requires ``django-recaptcha`` package.
- `Honeypot
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/security/honeypot/>`__:
  `Anti-spam honeypot <http://en.wikipedia.org/wiki/Anti-spam_techniques#Honeypots>`_
  field.

Test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Test plugins are made for dev purposes only.

- `Dummy
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/test/dummy/>`_:
  Mainly for dev purposes.

Bundled form handler plugins
-----------------------------------------------
Below a short overview of the form handler plugins. See the README.rst file
in directory of each plugin for details.

- `DB store
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_handlers/db_store/>`_:
  Stores form data in a database.
- `HTTP repost
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_handlers/http_repost/>`_:
  Repost the POST request to another endpoint.
- `Mail
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_handlers/mail/>`_:
  Send the form data by email.

Bundled themes
-----------------------------------------------
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
  Basic theme. Form editing is in a style of Django admin.
- `DjangoCMS admin style
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/themes/djangocms_admin_style_theme/>`_:
  Basic theme. Form editing is in a style of `djangocms-admin-style
  <https://github.com/divio/djangocms-admin-style>`_.

HTML5 fields
===============================================
The following HTML5 fields are supported in appropriate bundled plugins:

- date
- datetime
- email
- max
- min
- number
- url
- placeholder
- type

With the `fobi.contrib.plugins.form_elements.fields.input` support for
HTML5 fields is extended to the following fields:

- autocomplete
- autofocus
- list
- multiple
- pattern
- step

Loading initial data using GET arguments
===============================================
It's possible to provide initial data for the form using the GET arguments.

In that case, along with the field values, you should be providing
an additional argument named "fobi_initial_data", which doesn't have to
hold a value. For example, if your form contains of fields named "email" and
"age" and you want to provide initial values for those using GET arguments, you
should be constructing your URL to the form as follows:

http://127.0.0.1:8001/fobi/view/test-form/?fobi_initial_data&email=test@example.com&age=19

Submitted form element plugins values
===============================================
While some values of form element plugins are submitted as is, some others
need additional processing. There are 3 behaviours taken into consideration:

- "val": value is being sent as is.
- "repr": (human readable) representatio of the value is used.
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
- `Select multiple (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select_multiple/>`__
- `Select multiple model objects (drop-down)
  <https://github.com/barseghyanartur/django-fobi/tree/stable/src/fobi/contrib/plugins/form_elements/fields/select_multiple_model_objects/>`__

Rendering forms using third-party libraries
===============================================
You might want to render your forms using third-party libraries such as
`django-crispy-forms <http://django-crispy-forms.readthedocs.org/>`_,
`django-floppyforms <http://django-floppyforms.readthedocs.org/>`_ or 
other alternatives.

For that purpose you should override the "snippets/form_snippet.html" used
by the theme you have chosen. Your template would then look similar to the
one below (make sure to setup/configure your third-party form rendering library
prior doing this).

Using `django-crispy-forms`
-----------------------------------------------

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
-----------------------------------------------

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

Available translations
===============================================
English is the primary language.

- `Dutch <https://django-fobi.herokuapp.com/nl/>`_ (core and plugins)
- `German <https://django-fobi.herokuapp.com/de/>`_ (core and plugins)
- `Russian <https://django-fobi.herokuapp.com/ru/>`_ (core and plugins)

Debugging
===============================================
By default debugging is turned off. It means that broken form entries, which
are entries with broken data, that are not possible to be shown, are just
skipped. That's safe in production. Although, you for sure would want to
see the broken entries in development. Set the ``FOBI_DEBUG`` to True
in the ``settings.py`` of your project in order to do so.

Most of the errors are logged (DEBUG). If you have written a plugin and it
somehow doesn't appear in the list of available plugins, do run the following
management command since it not only syncs your plugins into the database,
but also is a great way of checking for possible errors.

.. code-block:: none

    ./manage.py fobi_sync_plugins

Run the following command in order to identify the broken plugins.

.. code-block:: none

    ./manage.py fobi_find_broken_entries

If you have forms refering to form element- of form handler- plugins
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

Troubleshooting
===============================================
If you get a ``FormElementPluginDoesNotExist`` or a
``FormHandlerPluginDoesNotExist`` exception, make sure you have listed your
plugin in the `settings` module of your project.

License
===============================================
GPL 2.0/LGPL 2.1

Support
===============================================
For any issues contact me at the e-mail given in the `Author` section.

Author
===============================================
Artur Barseghyan <artur.barseghyan@gmail.com>
