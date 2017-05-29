fobi.contrib.themes.foundation5
-------------------------------
A ``django-fobi`` Foundation 5 theme. Based on the ??? template, but
entire JS and CSS are taken from Foundation 5 version 5.4.0. The
`following <http://zurb.com/playground/foundation-icon-fonts-3>`_ icon set
was used.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.themes.foundation5`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.themes.foundation5',
            # ...
        )

(2) Specify ``foundation5`` as a default theme in your ``settings.py``:

    .. code-block:: python

        FOBI_DEFAULT_THEME = 'foundation5'
