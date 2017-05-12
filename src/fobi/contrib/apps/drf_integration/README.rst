fobi.contrib.apps.drf_integration
=================================
A ``django-fobi`` integration with ``Django REST framework``.

Supported actions are:

- `LIST`_: List all the forms.
- `OPTIONS`_: Describe the given form.
- `PUT`_: Submit form data.

Live demo
---------
Live demo is available on Heroku.

- `The core <https://django-fobi.herokuapp.com/>`_
- `Django REST framework integration <https://django-fobi.herokuapp.com/api/>`_

Supported fields
----------------
The following fields are supported.

Content (presentational form elements)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- content_image
- content_text
- content_video

Fields
~~~~~~
- boolean
- checkbox_select_multiple
- date
- datetime
- decimal
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
--------------------------
The following fields are not supported. Those marked with asterisk are planned
to be supported in the upcoming releases.

- date_drop_down
- select_model_object
- select_mptt_model_object
- select_multiple_model_objects
- select_multiple_mptt_model_objects

Implementation details
----------------------
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
- fobi.contrib.plugins.form_elements.fields.datetime
- fobi.contrib.plugins.form_elements.fields.decimal
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
- fobi.contrib.apps.drf_integration.form_elements.fields.datetime
- fobi.contrib.apps.drf_integration.form_elements.fields.decimal
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
- fobi.contrib.apps.drf_integration.form_elements.content.content_text
- fobi.contrib.apps.drf_integration.form_elements.content.content_video
- fobi.contrib.apps.drf_integration.form_handlers.db_store
- fobi.contrib.apps.drf_integration.form_handlers.http_repost
- fobi.contrib.apps.drf_integration.form_handlers.mail

Installation
------------
Versions
~~~~~~~~
Was made with ``djangorestframework`` 3.6.2. May work on earlier versions,
although not guaranteed.

See the `requirements file
<https://github.com/barseghyanartur/django-fobi/blob/stable/examples/requirements/djangorestframework.txt>`_.

your_project/settings.py
~~~~~~~~~~~~~~~~~~~~~~~~
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
        'fobi.contrib.apps.drf_integration.form_elements.content.content_text',
        'fobi.contrib.apps.drf_integration.form_elements.content.content_video',

        # DRF integration form handler plugins
        'fobi.contrib.apps.drf_integration.form_handlers.db_store',
        'fobi.contrib.apps.drf_integration.form_handlers.mail',
        'fobi.contrib.apps.drf_integration.form_handlers.http_repost',
        # ...
    ]

your_project/urls.py
~~~~~~~~~~~~~~~~~~~~
Add the following code to the main ``urls.py`` of your project:

.. code-block:: python

    # Conditionally including django-rest-framework integration app
    if 'fobi.contrib.apps.drf_integration' in settings.INSTALLED_APPS:
        from fobi.contrib.apps.drf_integration.urls import fobi_router
        urlpatterns += [
            url(r'^api/', include(fobi_router.urls))
        ]

Usage
-----
If you have followed the steps above precisely, you would be able to access
the API using ``http://localhost:8000/api/fobi-form-entry/``.

Actions/methods supported:

LIST
~~~~
.. code-block:: text

    GET /api/fobi-form-entry/

Lists all the forms available. Anonymous users would see the list of all
public forms. Authenticated users would see their own forms in addition
to the public forms.

OPTIONS
~~~~~~~
.. code-block:: text

    OPTIONS /api/fobi-form-entry/{FORM_SLUG}/

Lists all field options for the selected form. Private forms would be only
visible to authenticated users.

PUT
~~~
.. code-block:: text

    PUT /api/fobi-form-entry/{FORM_SLUG}/

    {DATA}

Callbacks
---------
Callbacks work just the same way the core callbacks work.

fobi_form_callbacks.py
~~~~~~~~~~~~~~~~~~~~~~
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
-------
To test Django REST framework integration package only, run the following
command:

.. code-block:: sh

    ./runtests.py src/fobi/tests/test_drf_integration.py

or use plain Django tests:

.. code-block:: sh

    ./manage.py test fobi.tests.test_drf_integration --settings=settings.test

Limitations
-----------
Certain fields are not available yet (relational fields).
