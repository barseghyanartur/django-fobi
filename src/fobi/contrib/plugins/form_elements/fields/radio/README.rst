===============================================
fobi.contrib.plugins.form_elements.fields.radio
===============================================
A ``Fobi`` Radio form field plugin. Makes use of the
``django.forms.fields.ChoiceField`` and ``django.forms.widgets.RadioSelect``.

Installation
===============================================
1. Add ``fobi.contrib.plugins.form_elements.fields.radio`` to the
   ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi.contrib.plugins.form_elements.fields.radio',
        # ...
    )

2. In the terminal type:

.. code-block:: none

    $ ./manage.py fobi_sync_plugins

3. Assign appropriate permissions to the target users/groups to be using
   the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.
