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
