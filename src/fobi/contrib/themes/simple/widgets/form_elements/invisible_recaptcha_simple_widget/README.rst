==================================================================================
fobi.contrib.themes.simple.widgets.form_elements.invisible_recaptcha_simple_widget
==================================================================================
An Invisible reCAPTCHA widget for the ``invisible_recaptcha`` plugin (for
Simple theme).

Installation
============
1. Add ``fobi.contrib.themes.simple.widgets.form_elements.invisible_recaptcha_simple_widget``
   to the ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi.contrib.themes.simple',
        'fobi.contrib.themes.simple.widgets.form_elements.invisible_recaptcha_simple_widget',
        'fobi.contrib.plugins.form_elements.security.invisible_recaptcha_simple_widget',
        # ...
    )

2. Specify ``bootstrap3`` as a default theme in your ``settings.py``:

.. code-block:: python

    FOBI_DEFAULT_THEME = 'simple'
