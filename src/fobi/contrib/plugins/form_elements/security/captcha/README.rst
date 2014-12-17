===================================================
fobi.contrib.plugins.form_elements.security.captcha
===================================================
A `CAPTCHA <http://en.wikipedia.org/wiki/CAPTCHA>`_ form field plugin. Makes
use of the `django-simple-captcha
<http://readthedocs.org/docs/django-simple-captcha>`_.

Installation
===============================================
Install `django-simple-captcha`
-----------------------------------------------
Taken from django-simple-captcha `installation instructions
<http://django-simple-captcha.readthedocs.org/en/latest/usage.html#installation>`_.

1. Download ``django-simple-captcha`` using pip by running:

.. code-block:: none

    $ pip install django-simple-captcha

2. Add ``captcha`` to the ``INSTALLED_APPS`` in your ``settings.py``.

3. Run ``python manage.py syncdb`` (or ``python manage.py migrate`` if you are
   managing database migrations via South) to create the required database
   tables.

4. Add an entry to your ``urls.py``:

.. code-block:: python

    urlpatterns += patterns('',
        url(r'^captcha/', include('captcha.urls')),
    )

Install `fobi` Captcha plugin
-----------------------------------------------
1. Add ``fobi.contrib.plugins.form_elements.security.captcha`` to the
   ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi.contrib.plugins.form_elements.security.captcha',
        # ...
    )

2. In the terminal type:

.. code-block:: none

    $ ./manage.py fobi_sync_plugins

3. Assign appropriate permissions to the target users/groups to be using
   the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

Troubleshooting and usage limitations
===============================================
At the moment, you can't use both ``CAPTCHA``
(fobi.contrib.plugins.form_elements.security.captcha) and ``ReCAPTCHA``
(fobi.contrib.plugins.form_elements.security.recaptcha) plugins alongside due
to app name collision of the ``django-simple-captcha`` and ``django-recaptcha``
packages. That limitation is likely to be solved in future in the
``django-recaptcha`` package. Until then, you should choose either one or
another, but not both on the same time.

Usage
===============================================
Note, that unlike most of the other form element plugins, default
value for the ``required`` attribute is True, which makes the Captcha
obligatory. Although you could still set it to False, it does not make
much sense to do so.
