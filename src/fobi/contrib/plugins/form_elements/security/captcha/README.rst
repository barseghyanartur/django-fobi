fobi.contrib.plugins.form_elements.security.captcha
---------------------------------------------------
A `CAPTCHA <http://en.wikipedia.org/wiki/CAPTCHA>`_ form field plugin. Makes
use of the `django-simple-captcha
<http://django-simple-captcha.readthedocs.io/en/latest/>`_.

Prerequisites
~~~~~~~~~~~~~
You will need ``libfreetype6``, otherwise ``django-simple-captcha`` won't work.

.. code-block:: sh

    sudo apt-get install libfreetype6-dev

Installation
~~~~~~~~~~~~
Install `django-simple-captcha`
###############################
Taken from django-simple-captcha `installation instructions
<http://django-simple-captcha.readthedocs.org/en/latest/usage.html#installation>`_.

(1) Download ``django-simple-captcha`` using pip by running:

    .. code-block:: sh

        pip install django-simple-captcha

(2) Add ``captcha`` to the ``INSTALLED_APPS`` in your ``settings.py``.

(3) Run ``python manage.py migrate``.

(4) Add an entry to your ``urls.py``:

    .. code-block:: python

        urlpatterns += [
            url(r'^captcha/', include('captcha.urls')),
        ]

Install `fobi` Captcha plugin
#############################
(1) Add ``fobi.contrib.plugins.form_elements.security.captcha`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.security.captcha',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) In order to have nicer text input widget, add the following line
    to your settings (if you're using bootstrap3 theme):

    .. code-block:: python

        CAPTCHA_TEXT_FIELD_TEMPLATE = 'bootstrap3/captcha/text_field.html'

    For foundation5 theme add the following line:

    .. code-block:: python

        CAPTCHA_TEXT_FIELD_TEMPLATE = 'foundation5/captcha/text_field.html'

Troubleshooting and usage limitations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In combination with other captcha solutions
###########################################
At the moment, you can't use both ``CAPTCHA``
(fobi.contrib.plugins.form_elements.security.captcha) and ``ReCAPTCHA``
(fobi.contrib.plugins.form_elements.security.recaptcha) plugins alongside due
to app name collision of the ``django-simple-captcha`` and ``django-recaptcha``
packages.

Usage
~~~~~
Note, that unlike most of the other form element plugins, default
value for the ``required`` attribute is True, which makes the Captcha
obligatory. Although you could still set it to False, it does not make
much sense to do so.
