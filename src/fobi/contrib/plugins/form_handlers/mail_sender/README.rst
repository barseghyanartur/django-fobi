fobi.contrib.plugins.form_handlers.mail_sender
----------------------------------------------
A ``Fobi`` Mail form handler plugin. Submits the form
data by email to the sender (submitter) of the form.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_handlers.mail_sender`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_handlers.mail_sender',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

Usage
~~~~~
(1) Add the `Mail the sender` form handler to the form.
(2) In the value for `Form field name to email` fill in the form field name
    which shall be used for sending an email to. For instance, if your
    original form consisted of `name`, `email`, `comment` fields, you should
    put `email` as a value for `Form field name to email` field.
