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
