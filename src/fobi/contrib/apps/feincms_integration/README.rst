===============================================
fobi.contrib.apps.feincms_integration
===============================================
A ``django-fobi`` integration with FeinCMS.

Installation
===============================================
your_project/settings.py
-----------------------------------------------
.. code-block:: python

    INSTALLED_APPS = list(INSTALLED_APPS)
    INSTALLED_APPS += [
        'feincms', # FeinCMS

        'fobi.contrib.apps.feincms_integration', # Fobi FeinCMS app

        'page', # Example
    ]

    FEINCMS_RICHTEXT_INIT_CONTEXT = {
        'TINYMCE_JS_URL': STATIC_URL + 'tiny_mce/tiny_mce.js',
    }

your_project/page/models.py
-----------------------------------------------
.. code-block:: python

    from django.utils.translation import ugettext_lazy as _

    from feincms.module.page.models import Page
    from feincms.content.raw.models import RawContent
    from feincms.content.richtext.models import RichTextContent
    # Import the ``django-fobi`` widget.
    from fobi.contrib.apps.feincms_integration.widgets import FobiFormWidget

    Page.register_extensions('feincms.module.extensions.translations',)

    # Register basic template.
    Page.register_templates(
        {
            'title': _(u"Base template"),
            'path': 'page/base.html',
            'key': 'page_base',
            'regions': (
                ('main', _(u"Main")),
                ('sidebar', _(u"Sidebar")),
            )
        },
        )

    # Standard content types
    Page.create_content_type(RawContent)
    Page.create_content_type(RichTextContent)

    # Register the ``django-fobi`` widget.
    Page.create_content_type(FobiFormWidget)

your_project/admin.py
-----------------------------------------------
.. code-block:: python

    from django.contrib import admin

    from feincms.module.page.modeladmins import PageAdmin

    from page.models import Page

    admin.site.register(Page, PageAdmin)

Usage
===============================================
Note, that rendering of the FeinCMS widget happens with help
theme template ``view_form_entry_ajax_template``.
