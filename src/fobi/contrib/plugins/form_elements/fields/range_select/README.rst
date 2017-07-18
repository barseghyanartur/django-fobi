fobi.contrib.plugins.form_elements.fields.range_select
------------------------------------------------------
A ``Fobi`` RangeSelect form field plugin. Makes use of the
``django.forms.fields.ChoiceField`` and ``django.forms.widgets.Select``.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.range_select`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.range_select',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

(4) Ranges are specified within the given min/max values. The default values
    are:

    .. code-block:: text

        - INITIAL: 50
        - INITIAL_MAX_VALUE: 100
        - INITIAL_MIN_VALUE: 0
        - MIN_VALUE: 0
        - MAX_VALUE: 100
        - STEP: 1

    However, you can override each of them in the settings of your project by
    prefixing correspondent names with `FOBI_FORM_ELEMENT_RANGE_SELECT_`:

    .. code-block:: text

        - FOBI_FORM_ELEMENT_RANGE_SELECT_INITIAL
        - FOBI_FORM_ELEMENT_RANGE_SELECT_INITIAL_MAX_VALUE
        - FOBI_FORM_ELEMENT_RANGE_SELECT_INITIAL_MIN_VALUE
        - FOBI_FORM_ELEMENT_RANGE_SELECT_MIN_VALUE
        - FOBI_FORM_ELEMENT_RANGE_SELECT_MAX_VALUE
        - FOBI_FORM_ELEMENT_RANGE_SELECT_STEP

(5) By default, the submitted form value of `range_select`
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
    ``FOBI_FORM_ELEMENT_RANGE_SELECT_SUBMIT_VALUE_AS`` assign one of the
    following values: "val", "repr" or "mix" to get the desired behaviour.