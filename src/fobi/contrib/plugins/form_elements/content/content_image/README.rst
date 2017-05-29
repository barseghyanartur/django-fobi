fobi.contrib.plugins.form_elements.content.content_image
--------------------------------------------------------
A ``Fobi`` Image form element plugin.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.content.content_image`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'easy_thumbnails',
            'fobi.contrib.plugins.form_elements.content.content_image',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) Additionally, for the fine tuning, see the
    ``fobi.contrib.plugins.form_elements.content.content_image.defaults``
    module. If necessary, override the settings by prepending
    ``FOBI_PLUGIN_CONTENT_IMAGE_`` to the desired variable name from the
    above mentioned ``defaults`` module.
