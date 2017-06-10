fobi.contrib.apps.drf_integration.form_elements.fields.select_multiple_model_objects
####################################################################################
A ``django-fobi`` MultipleModelChoiceField plugin for integration with
``Django REST framework``. Makes use of the
``fobi.contrib.apps.drf_integration.fields.py.MultipleModelChoiceField``.

Installation
^^^^^^^^^^^^
(1) Add ``fobi.contrib.apps.drf_integration.form_elements.fields.select_multiple_model_objects``
    to the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.apps.drf_integration.form_elements.fields.select_multiple_model_objects',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.
