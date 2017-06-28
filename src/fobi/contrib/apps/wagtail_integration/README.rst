fobi.contrib.apps.wagtail_integration
-------------------------------------
A ``django-fobi`` integration with Wagtail.

Prerequisites
~~~~~~~~~~~~~
Tested with Wagtail 1.10.1 only. Might work on earlier (or
later) versions as well.

Installation
~~~~~~~~~~~~
Versions
########
See the requirements files:

- `Wagtail 1.10 requirements
  <https://github.com/barseghyanartur/django-fobi/blob/stable/examples/wagtaildemo/requirements.txt>`_.

your_project/settings.py
########################
See the `example settings file
<https://github.com/barseghyanartur/django-fobi/blob/stable/examples/wagtaildemo/settings/fobi_integration.py>`_.

.. code-block:: python

    INSTALLED_APPS = list(INSTALLED_APPS)
    INSTALLED_APPS += [
        # ... standard wagtail apps

        # ... standard django-fobi apps

        'fobi.contrib.apps.wagtail_integration',  # Wagtail integration app
    ]

your_project/your_app/models.py
###############################
If existing ``fobi.contrib.apps.wagtail_integration.models.FobiFormPage``
model does not fit your needs and you want to extend, there's a
``fobi.contrib.apps.wagtail_integration.abstract.AbstractFobiFormPage``
abstract model which you can extend. If so, remove the
``fobi.contrib.apps.wagtail_integration`` from ``INSTALLED_APPS`` and add
path to the app with your customised ``FobiFormPage`` model.

.. code-block:: python

    from fobi.contrib.apps.wagtail_integration.models import AbstractFobiFormPage

    class FobiFormPage(AbstractFobiFormPage):
        """Fobi form page."""

        # ... customise your form page further

And then:

.. code-block:: python

    INSTALLED_APPS = [
        # ... standard wagtail apps

        # ... standard django-fobi apps

        'your_app',  # Customised `FobiFormPage` model app
    ]

Information for developers
##########################
Template rendering
^^^^^^^^^^^^^^^^^^
The embed Wagtail page is rendered with use of two theme templates:

- ``view_embed_form_entry_ajax_template``: Used for rendering the form.
- ``embed_form_entry_submitted_ajax_template``: Used for rendering the form
  sent event.

Using custom templates for rendering the widget
###############################################
In the widget, you can specify a template which you want to be used for
rendering the form or the form-sent event.

Example:

.. code-block:: python

    FOBI_WAGTAIL_INTEGRATION_FORM_TEMPLATE_CHOICES = (
        ("yourapp/custom_view_embed_form_v1.html",
         "Custom embed form view template #1"),
        ("yourapp/custom_view_embed_form_v2.html",
         "Custom embed form view template #2"),
    )

Same goes for form-sent templates.

.. code-block:: python

    FOBI_WAGTAIL_INTEGRATION_SUCCESS_PAGE_TEMPLATE_CHOICES = (
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
            'wagtail_integration': {
                'form_template_choices': [
                    ('fobi/bootstrap3_extras/view_embed_form.html',
                     "Custom form view (non-partial) template"),
                ],
                'success_page_template_choices': [
                    ('fobi/bootstrap3_extras/embed_form_submitted.html',
                     "Custom form entry submitted (non-partial) template"),
                ],
            },
        },
        'foundation5': {
            'wagtail_integration': {
                'form_template_choices': [
                    ('fobi/foundation5_extras/view_embed_form.html',
                     "Custom form view (non-partial) template"),
                ],
                'success_page_template_choices': [
                    ('fobi/foundation5_extras/embed_form_submitted.html',
                     "Custom form entry submitted (non-partial) template"),
                ],
            },
        },
    }

Disregard the name, both ``view_embed_form.html`` and
``embed_form_submitted.html`` files should be full (non-partial) HTML
templates.

Usage
~~~~~
The ``fobi.contrib.apps.wagtail_integration.models.FobiFormPage`` consists
of the following django-fobi specific fields (as well as of other Wagtail
Page related fields):

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
