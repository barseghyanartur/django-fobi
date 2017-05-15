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
