fobi.contrib.plugins.form_elements.fields.email_repeat
------------------------------------------------------
A ``Fobi`` Email repeat form field plugin. Makes use of the
``fobi.reusable.email_repeat.fields.EmailRepeatField`` and
``fobi.reusable.email_repeat.widgets.EmailRepeatWidget``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.email_repeat`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            "fobi.contrib.plugins.form_elements.fields.email_repeat",
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.
