====================================================
fobi.contrib.plugins.form_elements.security.honeypot
====================================================
A ``Fobi`` `Honeypot <http://en.wikipedia.org/wiki/Honeypot_%28computing%29>`_
form field plugin. Just another anti-spam technique.

Installation
===============================================
1. Add ``fobi.contrib.plugins.form_elements.security.honeypot`` to the
   ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi.contrib.plugins.form_elements.security.honeypot',
        # ...
    )

2. In the terminal type:

.. code-block:: none

    $ ./manage.py fobi_sync_plugins

3. Assign appropriate permissions to the target users/groups to be using
   the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

Usage
===============================================
Note, that unlike most of the other form element plugins, default
value for the ``required`` attribute is True, which makes the Captcha
obligatory. Although you could still set it to False, it does not make
much sense to do so.
