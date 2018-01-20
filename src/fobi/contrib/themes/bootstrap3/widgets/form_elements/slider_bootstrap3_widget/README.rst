=============================================================================
fobi.contrib.themes.bootstrap3.widgets.form_elements.slider_bootstrap3_widget
=============================================================================
A fancy slider widget for the ``slider`` plugin (for Bootstrap 3 theme). Based
on `bootstrap-slider.js <http://seiyria.com/bootstrap-slider/>`_. See the
`github <https://github.com/seiyria/bootstrap-slider>`_ for more.

Installation
============
1. Add ``fobi.contrib.themes.bootstrap3.widgets.form_elements.slider_bootstrap3_widget``
   to the ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi.contrib.themes.bootstrap3',
        'fobi.contrib.themes.bootstrap3.widgets.form_elements.slider_bootstrap3_widget',
        'fobi.contrib.plugins.form_elements.fields.slider',
        # ...
    )

2. Specify ``bootstrap3`` as a default theme in your ``settings.py``:

.. code-block:: python

    FOBI_DEFAULT_THEME = 'bootstrap3'
