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
