fobi.contrib.plugins.form_elements.fields.select
------------------------------------------------
A ``Fobi`` Select form field plugin. Makes use of the
``django.forms.fields.ChoiceField`` and ``django.forms.widgets.Select``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.select`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.select',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) By default, the submitted form value of `select`
    elements is label (human readable representation of the value chosen).
    However, that part of the behaviour has been made configurable. You can
    choose between the following options:

    Consider the following list of (value, label) choices (the first element in
    the tuple is value, the second element is label):

    .. code-block:: python

        [
            ('alpha', 'Alpha'),
            ('beta', 'Beta'),
            ('gamma', 'Gamma'),
        ]

    .. code-block:: text

        - "val": `value` (example: "alpha").
        - "repr" (default): `label` (example: "Alpha").
        - "mix": `value (label)` (example: "Alpha (alpha)").

    Simply set the
    ``FOBI_FORM_ELEMENT_SELECT_SUBMIT_VALUE_AS`` assign one of the following
    values: "val", "repr" or "mix" to get the desired behaviour.

Usage
~~~~~
You should be entering a single choice per line. Choice might
consist of just a single value or value/label pair.

For example:

.. code-block:: text

    1
    2
    alpha, Alpha
    beta, Beta
    omega

The following HTML would be made of:

.. code-block:: html

    <select id="id_NAME_OF_THE_ELEMENT" name="NAME_OF_THE_ELEMENT">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="alpha">Alpha</option>
      <option value="beta">Beta</option>
      <option value="omega">omega</option>
    </select>
