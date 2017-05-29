fobi.contrib.plugins.form_elements.content.content_text
-------------------------------------------------------
A ``Fobi`` Text form element plugin.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.content.content_text`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.content.content_text',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) Additionally, for the fine tuning, see the
    ``fobi.contrib.plugins.form_elements.content.content_text.defaults``
    module. If necessary, override the settings by prepending
    ``FOBI_PLUGIN_CONTENT_TEXT_`` to the desired variable name from the
    above mentioned ``defaults`` module.

    By default the content of the text field is stripped using either the
    awesome `bleach <https://bleach.readthedocs.io/>`_ library or if bleach
    is not installed just Django's own `strip_tags` function. To configure
    the strip (bleach only) behaviour, two settings are introduced:

    .. code-block:: text

       - ALLOWED_TAGS:
       - ALLOWED_ATTRIBUTES:

    The default values are:

    .. code-block:: python

        ALLOWED_TAGS = [
            'a',
            'abbr',
            'acronym',
            'b',
            'blockquote',
            'code',
            'em',
            'i',
            'li',
            'ol',
            'strong',
            'ul',
        ]

        ALLOWED_ATTRIBUTES = {
            'a': ['href', 'title'],
            'abbr': ['title'],
            'acronym': ['title'],
        }
