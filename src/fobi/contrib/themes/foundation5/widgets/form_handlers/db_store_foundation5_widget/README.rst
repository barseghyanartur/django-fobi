==============================================================
fobi.contrib.themes.foundation5.widgets.form_handlers.db_store
==============================================================
A ``db_store`` form handler plugin widget for Foundation 5 theme.
was used.

Installation
============
1. Add ``fobi.contrib.themes.foundation5.widgets.form_handlers.db_store`` to 
   the ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi.contrib.themes.foundation5',
        'fobi.contrib.themes.foundation5.widgets.form_handlers.db_store',
        'fobi.contrib.plugins.form_handlers.db_store',
        # ...
    )

2. Specify ``foundation5`` as a default theme in your ``settings.py``:

.. code-block:: python

    FOBI_DEFAULT_THEME = 'foundation5'
