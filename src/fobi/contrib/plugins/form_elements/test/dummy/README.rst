fobi.contrib.plugins.form_elements.test.dummy
---------------------------------------------
A ``Fobi`` Dummy form element plugin. Created for testing purposes.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.test.dummy`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.test.dummy',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.
