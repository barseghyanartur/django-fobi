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
