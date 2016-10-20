=====================================================
fobi.contrib.plugins.form_elements.security.recaptcha
=====================================================
A `ReCAPTCHA <http://en.wikipedia.org/wiki/ReCAPTCHA>`_ form field plugin.
Makes use of the `django-recaptcha
<https://github.com/praekelt/django-recaptcha>`_.

Installation
============
Install `django-recaptcha`
--------------------------
1. Download ``django-recaptcha`` using pip by running:

.. code-block:: none

    $ pip install django-recaptcha

2. Add ``captcha`` to the ``INSTALLED_APPS`` in your ``settings.py``.

3. Run ``python manage.py syncdb`` (or ``python manage.py migrate`` if you are
   managing database migrations via South) to create the required database
   tables.

Install `fobi` ReCAPTCHA plugin
-------------------------------
1. Add ``fobi.contrib.plugins.form_elements.security.recaptcha`` to the
   ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi.contrib.plugins.form_elements.security.recaptcha',
        # ...
    )

2. In the terminal type:

.. code-block:: none

    $ ./manage.py fobi_sync_plugins

3. Assign appropriate permissions to the target users/groups to be using
   the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

4. Specify the following ReCAPTCHA credentials in your settings.

   - ``RECAPTCHA_PUBLIC_KEY``
   - ``RECAPTCHA_PRIVATE_KEY``

Troubleshooting and usage limitations
=====================================
In combination with other captcha solutions
-------------------------------------------
At the moment, you can't use both ``CAPTCHA``
(fobi.contrib.plugins.form_elements.security.captcha) and ``ReCAPTCHA``
(fobi.contrib.plugins.form_elements.security.recaptcha) plugins alongside due
to app name collision of the ``django-simple-captcha`` and ``django-recaptcha``
packages. That limitation is likely to be solved in future in the
``django-recaptcha`` package. Until then, you should choose either one or
another, but not both on the same time.

If you happen to see errors like "Input error: k: Format of site key was
invalid", make sure to have defined (and filled in properly) the
``RECAPTCHA_PUBLIC_KEY`` and ``RECAPTCHA_PRIVATE_KEY`` in your settnings.py.
See the `following <https://github.com/praekelt/django-recaptcha/issues/32>`_
thread for more information.

In form wizards
---------------
At the moment, captcha fields do not work in form wizards, as they are
invalidated on the last step, which breaks the cycle. Therefore, it's not
recommended to use captcha plugins in form wizards.

Usage
=====
Note, that unlike most of the other form element plugins, default
value for the ``required`` attribute is True, which makes the ReCaptcha
obligatory. Although you could still set it to False, it does not make
much sense to do so.
