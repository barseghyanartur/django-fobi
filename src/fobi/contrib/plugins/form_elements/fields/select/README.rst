================================================
fobi.contrib.plugins.form_elements.fields.select
================================================
A ``Fobi`` Select form field plugin. Makes use of the
``django.forms.fields.ChoiceField`` and ``django.forms.widgets.Select``.

Installation
===============================================
1. Add ``fobi.contrib.plugins.form_elements.fields.select`` to the
   ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi.contrib.plugins.form_elements.fields.select',
        # ...
    )

2. In the terminal type:

.. code-block:: none

    $ ./manage.py fobi_sync_plugins

3. Assign appropriate permissions to the target users/groups to be using
   the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.

Usage
===============================================
You should be entering a single choice per line. Choice might
consist of just a single value or value/label pair.

For example:

.. code-block:: none

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
