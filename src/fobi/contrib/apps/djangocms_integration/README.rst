fobi.contrib.apps.djangocms_integration
---------------------------------------
A ``django-fobi`` integration with DjangoCMS.

Prerequisites
~~~~~~~~~~~~~
Tested with DjangoCMS 2.4.3, 3.0.6 and 3.4.3 only. Might work on earlier (or
later) versions as well.

Installation
~~~~~~~~~~~~
Versions
########
See the requirements files:

- `DjangoCMS 2.4.3 requirements
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/requirements/djangocms_2.txt>`_.
- `DjangoCMS 3.0.6 requirements
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/requirements/djangocms_3_0_6.txt>`_.
- `DjangoCMS 3.4.3 requirements
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/requirements/djangocms_3_4_3.txt>`_.

your_project/settings.py
########################
See the example settings files:

- `DjangoCMS 2.4.3 settings
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/simple/settings/bootstrap3_theme_djangocms_2.py>`_.
- `DjangoCMS 3.0.6/3.4.3. settings
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/simple/settings/bootstrap3_theme_djangocms.py>`_.

.. code-block:: python

    INSTALLED_APPS = list(INSTALLED_APPS)
    INSTALLED_APPS += [
        'cms',  # DjangoCMS

        'fobi.contrib.apps.djangocms_integration',  # Fobi DjangoCMS app
    ]

Information for developers
~~~~~~~~~~~~~~~~~~~~~~~~~~
Templates for DjangoCMS
#######################
Django-CMS templates are quite specific and in some aspects are not 100%
compatible with built-in themes (due to the fact that DjangoCMS intensively 
makes use of ``django-sekizai`` which isn't used in the generic templates).

That does not anyhow affect the core ``fobi`` and the built-in themes,
although you can't magically reuse built-in ``fobi`` themes with Django-CMS
(as it's done for `FeinCMS page templates
<https://github.com/barseghyanartur/django-fobi/blob/stable/examples/simple/templates/page/base.html>`_).

You would have to make custom page templates from scratch (or based on a
copy of the desired bundled template). See how I did it for all bundled themes
`here
<https://github.com/barseghyanartur/django-fobi/tree/stable/examples/simple/templates/cms_page>`_:

- `Bootstrap 3
  <https://github.com/barseghyanartur/django-fobi/tree/stable/examples/simple/templates/cms_page/bootstrap3>`_
- `Foundation 5
  <https://github.com/barseghyanartur/django-fobi/tree/stable/examples/simple/templates/cms_page/foundation5>`_
- `Simple
  <https://github.com/barseghyanartur/django-fobi/tree/stable/examples/simple/templates/cms_page/simple>`_

Template rendering
##################
The embed DjangoCMS widget is rendered with use of two theme templates:

- ``view_embed_form_entry_ajax_template``: Used for rendering the form.
- ``embed_form_entry_submitted_ajax_template``: Used for rendering the form
  sent event.

Using custom templates for rendering the widget
###############################################
In the widget, you can specify a template which you want to be used for
rendering the form or the form-sent event.

Example:

.. code-block:: python

    FOBI_DJANGOCMS_INTEGRATION_FORM_TEMPLATE_CHOICES = (
        ("yourapp/custom_view_embed_form_v1.html",
         "Custom embed form view template #1"),
        ("yourapp/custom_view_embed_form_v2.html",
         "Custom embed form view template #2"),
    )

Same goes for form-sent templates.

.. code-block:: python

    FOBI_DJANGOCMS_INTEGRATION_SUCCESS_PAGE_TEMPLATE_CHOICES = (
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
            'djangocms_integration': {
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
            'djangocms_integration': {
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
The ``fobi.contrib.apps.djangocms_integration.models.FobiFormWidget`` consists
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
