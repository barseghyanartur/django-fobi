fobi.contrib.themes.bootstrap5
------------------------------
A ``django-fobi`` Bootstrap 5 theme.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.themes.bootstrap5`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.themes.bootstrap5',
            # ...
        )

(2) Specify ``bootstrap5`` as a default theme in your ``settings.py``:

    .. code-block:: python

        FOBI_DEFAULT_THEME = 'bootstrap5'
