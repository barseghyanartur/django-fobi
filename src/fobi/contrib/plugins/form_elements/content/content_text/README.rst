=======================================================
fobi.contrib.plugins.form_elements.content.content_text
=======================================================
A ``Fobi`` Text form element plugin.

Installation
===============================================
1. Add ``fobi.contrib.plugins.form_elements.content.content_text`` to the
   ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi.contrib.plugins.form_elements.content.content_text',
        # ...
    )

2. In the terminal type:

.. code-block:: none

    $ ./manage.py fobi_sync_plugins

3. Assign appropriate permissions to the target users/groups to be using
   the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.
