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
