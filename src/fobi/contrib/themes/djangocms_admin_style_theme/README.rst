fobi.contrib.themes.djangocms_admin_style_theme
-----------------------------------------------
A ``django-fobi`` theme in a style of ``djangocms-admin-style`` admin.
Relies on ``djangocms-admin-style`` package and some jQuery UI only.

jQuery UI "Smoothness" theme comes from `here <http://jqueryui.com/>`_.

Installation
~~~~~~~~~~~~
Install `djangocms-admin-style`
###############################
See the original `installation instructions
<https://pypi.python.org/pypi/djangocms-admin-style#installation>`_.

(1) Install the ``djangocms-admin-style`` package.

    .. code-block:: sh

        pip install djangocms-admin-style

(2) Add ``djangocms_admin_style`` to your ``INSTALLED_APPS`` just before
    ``django.contrib.admin``.

Install `fobi.contrib.themes.djangocms_admin_style_theme` theme
###############################################################
(1) Add ``fobi.contrib.themes.djangocms_admin_style_theme`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.themes.djangocms_admin_style_theme',
            # ...
        )

(2) Specify ``djangocms_admin_style_theme`` as a default theme in your
    ``settings.py``:

    .. code-block:: python

        FOBI_DEFAULT_THEME = 'djangocms_admin_style_theme'
