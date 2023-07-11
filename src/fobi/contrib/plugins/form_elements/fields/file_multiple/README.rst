fobi.contrib.plugins.form_elements.fields.file
----------------------------------------------
A ``Fobi`` File form field plugin. Makes use of the
``django.forms.fields.FileField`` and
``django.forms.widgets.ClearableFileInput``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.file`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.file',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) By default uploaded files are stored in the "fobi_plugins/file" directory
    of the media root. If you want to change the directory location,
    set the ``FOBI_PLUGIN_FIELDS_FILE_FILES_UPLOAD_DIR`` value to the desired
    (relative) path.

(5) You may optionally restrict uploaded files extensions by specifying the
    ``allowed_extensions`` field in the plugin.
