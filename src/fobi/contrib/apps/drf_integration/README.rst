fobi.contrib.apps.drf_integration
=================================
A ``django-fobi`` integration with ``Django REST framework``.

Due to limits of the API interface, certain fields are not available
yet (presentational fields).

Some of the plugins may seam to have zero-added-value and in fact they are.
For instance, DRF integration `slider` plugin is just an exact copy of the
`range_select` plugin, created in order to provide exactly the same form
fields generated in the API.

Supported fields
----------------
The following fields are suppored.

- boolean
- checkbox_select_multiple
- date
- *date_drop_down
- datetime
- decimal
- email
- file
- float
- hidden (in terms of the Django REST framework - a read-only field)
- input (some sort of a copy of `text` plugin)
- integer
- ip_address
- null_boolean
- password (some sort of a copy of `text` plugin)
- radio
- range_select
- regex
- select
- select_multiple
- select_multiple_with_max
- slider (just a copy of range_select, for compatibility with main package)
- slug
- text
- textarea (some sort of a copy of `text` plugin)
- time
- url

Not supported fields
--------------------
The following fields are not supported. Those marked with asterisk are planned
to be supported in the upcoming releases.

- content_image
- content_text
- content_video
- select_model_object
- select_mptt_model_object
- select_multiple_model_objects
- select_multiple_mptt_model_objects

Installation
------------
Versions
~~~~~~~~
See the `requirements file
<https://github.com/barseghyanartur/django-fobi/blob/stable/examples/requirements_djangorestframework.txt>`_.

your_project/settings.py
~~~~~~~~~~~~~~~~~~~~~~~~
See the `example settings file
<https://github.com/barseghyanartur/django-fobi/blob/stable/examples/simple/settings_bootstrap3_theme_drf_integration.py>`_.

.. code-block:: python

    INSTALLED_APPS = list(INSTALLED_APPS)
    INSTALLED_APPS += [
        'rest_framework',  # Django REST framework

        'fobi.contrib.apps.drf_integration',  # DRF integration app
    ]

your_project/urls.py
~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    # TODO

your_project/routers.py
~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    # TODO

Information for developers
--------------------------

# TODO

Usage
-----

# TODO
