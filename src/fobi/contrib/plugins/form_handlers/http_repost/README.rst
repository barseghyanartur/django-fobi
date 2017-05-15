fobi.contrib.plugins.form_handlers.http_repost
----------------------------------------------
A ``Fobi`` HTTP Repost form handler plugin. Submits the form
data as is to the given endpoint.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_handlers.http_repost`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_handlers.http_repost',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.
