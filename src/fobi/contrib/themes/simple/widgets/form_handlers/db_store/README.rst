=========================================================
fobi.contrib.themes.simple.widgets.form_handlers.db_store
=========================================================
A ``db_store`` form handler plugin widget for Simple theme.

Installation
============
1. Add ``fobi.contrib.themes.simple.widgets.form_handlers.db_store`` to
   the ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi.contrib.themes.simple',
        'fobi.contrib.themes.simple.widgets.form_handlers.db_store',
        'fobi.contrib.plugins.form_handlers.db_store',
        # ...
    )

2. Specify ``simple`` as a default theme in your ``settings.py``:

.. code-block:: python

    FOBI_DEFAULT_THEME = 'simple'
