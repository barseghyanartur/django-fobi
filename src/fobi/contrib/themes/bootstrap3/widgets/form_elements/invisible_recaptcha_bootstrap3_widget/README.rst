==========================================================================================
fobi.contrib.themes.bootstrap3.widgets.form_elements.invisible_recaptcha_bootstrap3_widget
==========================================================================================
An Invisible reCAPTCHA widget for the ``invisible_recaptcha`` plugin (for
Bootstrap 3 theme).

Installation
============
1. Add ``fobi.contrib.themes.bootstrap3.widgets.form_elements.invisible_recaptcha_bootstrap3_widget``
   to the ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi.contrib.themes.bootstrap3',
        'fobi.contrib.themes.bootstrap3.widgets.form_elements.invisible_recaptcha_bootstrap3_widget',
        'fobi.contrib.plugins.form_elements.security.invisible_recaptcha_bootstrap3_widget',
        # ...
    )

2. Specify ``bootstrap3`` as a default theme in your ``settings.py``:

.. code-block:: python

    FOBI_DEFAULT_THEME = 'bootstrap3'
