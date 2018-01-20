fobi.contrib.plugins.form_elements.security.invisible_recaptcha
---------------------------------------------------------------
A `Invisible reCAPTCHA
<https://developers.google.com/recaptcha/docs/invisible>`_
form field plugin. Just another anti-spam technique.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.security.invisible_recaptcha`` to
    the ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.security.invisible_recaptcha',
            'fobi.contrib.themes.bootstrap3.widgets.form_elements.invisible_recaptcha_bootstrap3_widget',
            # ...
        )

(2) Enable Invisible reCAPTCHA for your site and put the site key and site
    secret keys in the settings:

    .. code-block:: python

        FOBI_PLUGIN_INVISIBLE_RECAPTCHA_SITE_KEY = 'your-site-key'
        FOBI_PLUGIN_INVISIBLE_RECAPTCHA_SITE_SECRET = 'your-site-secret'

(3) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(4) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.
