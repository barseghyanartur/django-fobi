==============================================================================
fobi.contrib.themes.djangocms_admin_style_theme.widgets.form_handlers.db_store
==============================================================================
A ``db_store`` form handler plugin widget for Simple theme.

Installation
============
1. Add ``fobi.contrib.themes.djangocms_admin_style_theme.widgets.form_handlers.db_store`` 
   to the ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi.contrib.themes.djangocms_admin_style_theme',
        'fobi.contrib.themes.djangocms_admin_style_theme.widgets.form_handlers.db_store',
        'fobi.contrib.plugins.form_handlers.db_store',
        # ...
    )

2. Specify ``djangocms_admin_style_theme`` as a default theme in your ``settings.py``:

.. code-block:: python

    FOBI_DEFAULT_THEME = 'djangocms_admin_style_theme'
