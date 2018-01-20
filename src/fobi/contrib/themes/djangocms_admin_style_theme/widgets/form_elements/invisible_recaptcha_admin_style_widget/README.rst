==================================================================================
fobi.contrib.themes.djangocms_admin_style_theme.widgets.form_elements.invisible_recaptcha_admin_style_widget
==================================================================================
An Invisible reCAPTCHA widget for the ``invisible_recaptcha`` plugin (for
Simple theme).

Installation
============
1. Add ``fobi.contrib.themes.simple.widgets.form_elements.invisible_recaptcha_admin_style_widget``
   to the ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi.contrib.themes.djangocms_admin_style_theme',
        'fobi.contrib.themes.djangocms_admin_style_theme.widgets.form_elements.invisible_recaptcha_admin_style_widget',
        'fobi.contrib.plugins.form_elements.security.invisible_recaptcha_admin_style_widget',
        # ...
    )

2. Specify ``bootstrap3`` as a default theme in your ``settings.py``:

.. code-block:: python

    FOBI_DEFAULT_THEME = 'djangocms_admin_style_theme'
