fobi.contrib.apps.feincms_integration
-------------------------------------
A ``django-fobi`` integration with FeinCMS.

Prerequisites
~~~~~~~~~~~~~
Tested with FeinCMS 1.10, 1.12 and 1.13 only. Might work on earlier (or
later) versions as well.

Installation
~~~~~~~~~~~~
Versions
########
See the requirements files:

- `FeinCMS 1.10 requirements
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/requirements/feincms_1_10.txt>`_.
- `FeinCMS 1.12 requirements
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/requirements/feincms_1_12.txt>`_.
- `FeinCMS 1.13 requirements
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/requirements/feincms_1_13.txt>`_.

your_project/settings.py
########################
See the `example settings file
<https://github.com/barseghyanartur/django-fobi/blob/stable/examples/simple/settings/bootstrap3_theme_feincms.py>`_.

.. code-block:: python

    INSTALLED_APPS = list(INSTALLED_APPS)
    INSTALLED_APPS += [
        'feincms',  # FeinCMS

        'fobi.contrib.apps.feincms_integration',  # Fobi FeinCMS app

        'page',  # Example
    ]

    FEINCMS_RICHTEXT_INIT_CONTEXT = {
        'TINYMCE_JS_URL': STATIC_URL + 'tiny_mce/tiny_mce.js',
    }

your_project/page/models.py
###########################
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
#####################
.. code-block:: python

    from django.contrib import admin

    from feincms.module.page.modeladmins import PageAdmin

    from page.models import Page

    admin.site.register(Page, PageAdmin)

Information for developers
##########################
Template rendering
^^^^^^^^^^^^^^^^^^
The embed FeinCMS widget is rendered with use of two theme templates:

- ``view_embed_form_entry_ajax_template``: Used for rendering the form.
- ``embed_form_entry_submitted_ajax_template``: Used for rendering the form
  sent event.

Using custom templates for rendering the widget
###############################################
In the widget, you can specify a template which you want to be used for
rendering the form or the form-sent event.

Example:

.. code-block:: python

    FOBI_FEINCMS_INTEGRATION_FORM_TEMPLATE_CHOICES = (
        ("yourapp/custom_view_embed_form_v1.html",
         "Custom embed form view template #1"),
        ("yourapp/custom_view_embed_form_v2.html",
         "Custom embed form view template #2"),
    )

Same goes for form-sent templates.

.. code-block:: python

    FOBI_FEINCMS_INTEGRATION_SUCCESS_PAGE_TEMPLATE_CHOICES = (
        ("yourapp/custom_embed_form_submitted_v1.html",
         "Custom form-sent template #1"),
        ("yourapp/custom_embed_form_submitted_v2.html",
         "Custom form-sent template #2"),
    )

Registering a template in the ``FORM_TEMPLATE_CHOICES`` makes it available
for all the themes. If you rather want to use different custom templates
for different themes, use the ``FOBI_CUSTOM_THEME_DATA`` as shown in the
example below.

.. code-block:: python

    FOBI_CUSTOM_THEME_DATA = {
        'bootstrap3': {
            'feincms_integration': {
                'form_template_choices': [
                    ('fobi/bootstrap3_extras/view_embed_form.html',
                     "Custom bootstrap3 embed form view template"),
                ],
                'success_page_template_choices': [
                    ('fobi/bootstrap3_extras/embed_form_submitted.html',
                     "Custom bootstrap3 embed form entry submitted template"),
                ],
            },
        },
        'foundation5': {
            'feincms_integration': {
                'form_template_choices': [
                    ('fobi/foundation5_extras/view_embed_form.html',
                     "Custom foundation5 embed form view template"),
                ],
                'success_page_template_choices': [
                    ('fobi/foundation5_extras/embed_form_submitted.html',
                     "Custom foundation5 embed form entry submitted template"),
                ],
            },
        },
    }

Usage
~~~~~
The ``fobi.contrib.apps.feincms_integration.widgets.FobiFormWidget`` consists
of the following fields:

- Form: The form to be used.
- Form template name: Template to be used to render the embed form.
- Hide form title: If checked, no form title would be shown.
- Form title: Overrides the standard form title.
- Submit button text: Overrides the default submit button text.
- Success page template name: Template to be used to render the embed form-sent
  event.
- Hide success page title: If checked, no form-sent title would be shown.
- Success page title: Overrides the form-sent title.
- Success page text: Overrides the form-sent text.
