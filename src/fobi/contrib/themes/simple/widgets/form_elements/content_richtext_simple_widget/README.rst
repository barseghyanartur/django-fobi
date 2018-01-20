===============================================================================
fobi.contrib.themes.simple.widgets.form_elements.content_richtext_simple_widget
===============================================================================
A rich-text widget for the ``content_richtext`` plugin (for Simple theme).

Installation
============
1. Add ``fobi.contrib.themes.simple.widgets.form_elements.content_richtext_simple_widget``
   to the ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi.contrib.themes.simple',
        'fobi.contrib.themes.simple.widgets.form_elements.content_richtext_simple_widget',
        'fobi.contrib.plugins.form_elements.content.content_richtext',
        # ...
    )

2. Specify ``simple`` as a default theme in your ``settings.py``:

.. code-block:: python

    FOBI_DEFAULT_THEME = 'simple'
