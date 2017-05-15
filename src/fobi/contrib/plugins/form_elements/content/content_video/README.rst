fobi.contrib.plugins.form_elements.content.content_video
--------------------------------------------------------
A ``Fobi`` Video form element plugin.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.content.content_video`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.content.content_video',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) Additionally, for the fine tuning, see the
    ``fobi.contrib.plugins.form_elements.content.content_video.defaults``
    module. If necessary, override the settings by prepending
    ``FOBI_PLUGIN_CONTENT_VIDEO_`` to the desired variable name from the
    above mentioned ``defaults`` module.
