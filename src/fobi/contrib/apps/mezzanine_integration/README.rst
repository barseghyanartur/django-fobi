fobi.contrib.apps.mezzanine_integration
---------------------------------------
A ``django-fobi`` integration with Mezzanine.

Prerequisites
~~~~~~~~~~~~~
Tested with Mezzanine 3.1.10 and 4.2.3 only. Might work on earlier (or
later) versions as well.

Installation
~~~~~~~~~~~~
Versions
########
See the requirements files:

- `Mezzanine 4.2.3 requirements
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/mezzanine_example/requirements.txt>`_.

your_project/settings.py
########################
See the `example settings file
<https://github.com/barseghyanartur/django-fobi/blob/stable/examples/mezzanine_example/settings.py>`_.

.. code-block:: python

    INSTALLED_APPS = list(INSTALLED_APPS)
    INSTALLED_APPS += [
        # Standard mezzanine apps

        'fobi.contrib.apps.mezzanine_integration',  # Fobi Mezzanine app
    ]

Information for developers
~~~~~~~~~~~~~~~~~~~~~~~~~~
Template rendering
##################
The form embed into Mezzanine page is rendered with use of two theme templates:

- ``view_embed_form_entry_ajax_template``: Used for rendering the form.
- ``embed_form_entry_submitted_ajax_template``: Used for rendering the form
  sent event.

Using custom templates for rendering the form
#############################################
In the widget, you can specify a template which you want to be used for
rendering the form or the form-sent event.

Example:

.. code-block:: python

    FOBI_MEZZANINE_INTEGRATION_FORM_TEMPLATE_CHOICES = (
        ("yourapp/custom_view_embed_form_v1.html",
         "Custom embed form view template #1"),
        ("yourapp/custom_view_embed_form_v2.html",
         "Custom embed form view template #2"),
    )

Same goes for form-sent templates.

.. code-block:: python

    FOBI_MEZZANINE_INTEGRATION_SUCCESS_PAGE_TEMPLATE_CHOICES = (
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
            'mezzanine_integration': {
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
            'mezzanine_integration': {
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
The ``fobi`` page model
#######################
The ``fobi.contrib.apps.mezzanine_integration.models.FobiFormPage`` consists
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

Steps described
###############
1. If you use the mezzanine `example
   <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/mezzanine_example/>`_
   project, to start go to the http://localhost:8003/fobi/ URL and create a
   form.
2. Then go to http://localhost:8003/admin/pages/page/ and add a new `Fobi form`
   page.
3. Choose the form and optionally - override the form settings and then
   save the page.
4. See the page in the front-end.
