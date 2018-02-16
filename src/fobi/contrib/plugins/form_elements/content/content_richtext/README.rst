fobi.contrib.plugins.form_elements.content.content_richtext
-----------------------------------------------------------

A ``Fobi`` Rich text form element plugin based on
`CKEditor <https://ckeditor.com/>`_ and
`django-ckeditor <https://github.com/django-ckeditor/django-ckeditor>`_.

Installation
~~~~~~~~~~~~

(1) Install ``django-ckeditor``.

    .. code-block:: sh

        pip install django-ckeditor

(2) Add ``ckeditor`` to ``INSTALLED_APPS`` in ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            ...
            'ckeditor',
            ...
        )

(3) Add ``fobi.contrib.plugins.form_elements.content.content_richtext`` to
    ``INSTALLED_APPS`` in ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            ...
            'fobi.contrib.plugins.form_elements.content.content_richtext',
            ...
        )

(4) Add ``fobi.contrib.themes.bootstrap3.widgets.form_elements.content_richtext_bootstrap3_widget`` to
    ``INSTALLED_APPS`` in ``settings.py`` (if you're using ``bootstrap3`` theme).
    If you're using another theme, add correspondent widget specific to the
    active theme.

    .. code-block:: python

        INSTALLED_APPS = (
            ...
            'fobi.contrib.themes.bootstrap3.widgets.form_elements.content_richtext_bootstrap3_widget',
            ...
        )

(5) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(6) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to ``True``.

Controlling HTML tags and attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(1) Install ``bleach``.

    .. code-block:: sh

        pip install bleach

(2) Specify ``FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_TAGS``,
    ``FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_ATTRIBUTES`` and
    ``FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_STYLES`` in
    ``settings.py``. The default values come from bleach:

    .. code-block:: python

        FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_TAGS = [
            'a',
            'abbr',
            'acronym',
            'b',
            'blockquote',
            'code',
            'em',
            'i',
            'li',
            'ol',
            'strong',
            'ul',
        ]

        FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_ATTRIBUTES = {
            'a': ['href', 'title'],
            'abbr': ['title'],
            'acronym': ['title'],
        }

        FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_STYLES = []
