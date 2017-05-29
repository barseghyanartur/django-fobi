fobi.contrib.themes.bootstrap3
------------------------------
A ``django-fobi`` Bootstrap 3 theme. Based on the ??? template.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.themes.bootstrap3`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.themes.bootstrap3',
            # ...
        )

(2) Specify ``bootstrap3`` as a default theme in your ``settings.py``:

    .. code-block:: python

        FOBI_DEFAULT_THEME = 'bootstrap3'
