===========================================================================
fobi.contrib.themes.bootstrap3.widgets.form_elements.date_bootstrap3_widget
===========================================================================
A fancy date picker widget for the ``date`` plugin (for Bootstrap 3
theme).

Installation
============
1. Add ``fobi.contrib.themes.bootstrap3.widgets.form_elements.date_bootstrap3_widget``
   to the ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi.contrib.themes.bootstrap3',
        'fobi.contrib.themes.bootstrap3.widgets.form_elements.date_bootstrap3_widget',
        'fobi.contrib.plugins.form_elements.fields.date',
        # ...
    )

2. Specify ``bootstrap3`` as a default theme in your ``settings.py``:

.. code-block:: python

    FOBI_DEFAULT_THEME = 'bootstrap3'
