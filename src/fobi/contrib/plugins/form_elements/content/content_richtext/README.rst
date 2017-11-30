fobi.contrib.plugins.form_elements.content.content_richtext
-----------------------------------------------------------

A ``Fobi`` Rich text form element plugin based on
`Summernote <https://summernote.org/>`_.

Installation
~~~~~~~~~~~~

(1) Install ``django-summernote``.

    .. code-block:: sh

        pip install django-summernote

(2) Add ``django_summernote`` to ``INSTALLED_APPS`` in ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            ...
            'django_summernote',
            ...
        )

(3) Add ``django_summernote.urls`` to ``urls.py``.

    .. code-block:: python

        urlpatterns = [
            ...
            url(r'^summernote/', include('django_summernote.urls')),
            ...
        ]

(4) Add ``fobi.contrib.plugins.form_elements.content.content_richtext`` to
    ``INSTALLED_APPS`` in ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            ...
            'fobi.contrib.plugins.form_elements.content.content_richtext',
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

(2) Specify ``FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_TAGS`` and
    ``FOBI_PLUGIN_CONTENT_RICHTEXT_ALLOWED_ATTRIBUTES`` in
    ``settings.py``. The default values are:

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

For frontend-only control one could alternatively use
a ``summernote`` plugin like ``summernote-cleaner``.
