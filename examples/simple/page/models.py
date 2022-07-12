from django.utils.translation import gettext_lazy as _
from feincms.content.raw.models import RawContent
from feincms.content.richtext.models import RichTextContent
from feincms.module.page.models import Page

# Import the ``django-fobi`` widget.
from fobi.contrib.apps.feincms_integration.widgets import FobiFormWidget

Page.register_extensions(
    "feincms.module.extensions.translations",
)

# Register basic template.
Page.register_templates(
    {
        "title": _("Base template"),
        "path": "page/base.html",
        "key": "page_base",
        "regions": (
            ("main", _("Main")),
            ("sidebar", _("Sidebar")),
        ),
    },
)

# Standard content types
Page.create_content_type(RawContent)
Page.create_content_type(RichTextContent)

# Register the ``django-fobi`` widget.
Page.create_content_type(FobiFormWidget)
