fobi.contrib.plugins.form_elements.fields.input
-----------------------------------------------
A generic input form field plugin. Makes use of the
``django.forms.fields.Field`` and ``django.forms.widgets.Input``.
Comes with a lot of options you likely won't use every day.

The full list of supported HTML properties is listed below:

- autocomplete
- autofocus
- disabled
- list
- max
- min
- multiple
- pattern
- placeholder
- readonly
- step
- type

See `w3schools.com <http://www.w3schools.com/tags/tag_input.asp>`_ for further
explanations.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.input`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.input',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.
