fobi.contrib.plugins.form_elements.fields.duration
--------------------------------------------------
A ``Fobi`` Select form field plugin. Makes use of the
``django.forms.fields.DurationField``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.duration`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.duration',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

Usage
~~~~~
Next to standard field attributes, duration plugin accepts the following
attributes (all integers):

.. code-block:: text

- weeks:
- days:
- hours
- minutes:
- seconds:

All being used to form a ``datetime.timedelta`` value with the arguments
mentioned above.

Initial value should be a properly formatted string.

.. code-block:: text

    3 days, 23:10:53
    09:30:00
