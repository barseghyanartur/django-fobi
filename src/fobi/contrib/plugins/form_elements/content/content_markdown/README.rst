fobi.contrib.plugins.form_elements.content.content_markdown
-----------------------------------------------------------

A ``Fobi`` Markdown form element plugin based on
`remarkable <https://github.com/jonschlinkert/remarkable/>`_ and
`markdown <https://github.com/Python-Markdown/markdown>`_.

Installation
~~~~~~~~~~~~

(1) Install ``markdown``.

    .. code-block:: sh

        pip install markdown

(2) Add ``fobi.reusable.markdown_widget`` to ``INSTALLED_APPS`` in
    ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            ...
            'fobi.reusable.markdown_widget',
            ...
        )

(3) Add ``fobi.contrib.plugins.form_elements.content.content_markdown`` to
    ``INSTALLED_APPS`` in ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            ...
            'fobi.contrib.plugins.form_elements.content.content_markdown',
            ...
        )

(4) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(5) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to ``True``.
