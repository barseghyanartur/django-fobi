from collections import OrderedDict

from django.forms.forms import BaseForm
from django.forms.widgets import media_property
from django.http import HttpResponseRedirect
from django.urls import reverse

from formtools.wizard.views import (
    CookieWizardView,
    SessionWizardView,
    WizardView,
)

from six import with_metaclass

from .constants import WIZARD_TYPE_COOKIE, WIZARD_TYPE_SESSION

__title__ = 'fobi.dynamic'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'assemble_form_class',
    'assemble_form_wizard_class',
)

# ****************************************************************************
# ****************************************************************************
# **************************** Form generator ********************************
# ****************************************************************************
# ****************************************************************************


def assemble_form_class(form_entry,
                        base_class=BaseForm,
                        request=None,
                        origin=None,
                        origin_kwargs_update_func=None,
                        origin_return_func=None,
                        form_element_entries=None,
                        get_form_field_instances_kwargs={}):
    """Assemble a form class by given entry.

    :param form_entry:
    :param base_class:
    :param django.http.HttpRequest request:
    :param string origin:
    :param callable origin_kwargs_update_func:
    :param callable origin_return_func:
    :param iterable form_element_entries: If given, used instead of
        ``form_entry.formelemententry_set.all`` (no additional database hit).
    :param dict get_form_field_instances_kwargs: To be passed as **kwargs to
        the :method:`get_form_field_instances_kwargs`.
    """
    if form_element_entries is None:
        form_element_entries = form_entry.formelemententry_set.all()

    # DeclarativeFieldsMetaclass
    class DeclarativeFieldsMetaclass(type):
        """Declarative fields meta class.

        Copied from ``django.forms.forms.DeclarativeFieldsMetaclass``.

        Metaclass that converts Field attributes to a dictionary called
        `base_fields`, taking into account parent class 'base_fields' as well.
        """

        def __new__(cls, name, bases, attrs):
            """New."""
            base_fields = []

            for creation_counter, form_element_entry \
                    in enumerate(form_element_entries):
                plugin = form_element_entry.get_plugin(request=request)

                # We simply make sure the plugin exists. We don't handle
                # exceptions relate to the non-existent plugins here. They
                # are instead handled in registry.
                if plugin:
                    plugin_form_field_instances = \
                        plugin._get_form_field_instances(
                            form_element_entry=form_element_entry,
                            origin=origin,
                            kwargs_update_func=origin_kwargs_update_func,
                            return_func=origin_return_func,
                            extra={'counter': creation_counter},
                            request=request,
                            form_entry=form_entry,
                            form_element_entries=form_element_entries,
                            **get_form_field_instances_kwargs
                        )
                    for form_field_name, form_field_instance \
                            in plugin_form_field_instances:
                        base_fields.append(
                            (form_field_name, form_field_instance)
                        )

            attrs['base_fields'] = OrderedDict(base_fields)
            new_class = super(DeclarativeFieldsMetaclass, cls).__new__(
                cls, name, bases, attrs
            )

            if 'media' not in attrs:
                new_class.media = media_property(new_class)

            return new_class

    # DynamicForm
    class DynamicForm(with_metaclass(DeclarativeFieldsMetaclass, base_class)):
        """Dynamically created form element plugin class."""

    # Finally, return the DynamicForm
    return DynamicForm


def assemble_form_wizard_class(form_wizard_entry,
                               base_class=SessionWizardView,
                               request=None,
                               origin=None,
                               origin_kwargs_update_func=None,
                               origin_return_func=None,
                               form_wizard_form_entries=None,
                               template_name=None):
    """Assemble form wizard class.

    :param form_wizard_entry:
    :param base_class:
    :param request:
    :param origin:
    :param origin_kwargs_update_func:
    :param origin_return_func:
    :param form_wizard_form_entries:
    :param template_name:
    :return:
    """

    if form_wizard_entry.wizard_type == WIZARD_TYPE_SESSION:
        base_class = SessionWizardView
    elif form_wizard_entry.wizard_type == WIZARD_TYPE_COOKIE:
        base_class = CookieWizardView
    elif not issubclass(base_class, WizardView):
        base_class = SessionWizardView

    if form_wizard_form_entries is None:
        form_entries = [
            form_wizard_form_entry.form_entry
            for form_wizard_form_entry
            in form_wizard_entry.formwizardformentry_set.all()
        ]
    else:
        form_entries = [
            form_wizard_form_entry.form_entry
            for form_wizard_form_entry
            in form_wizard_form_entries
        ]

    # DeclarativeFormsMetaclass
    class DeclarativeFormsMetaclass(type):
        """Declarative forms meta class.

        Copied from ``django.forms.forms.DeclarativeFieldsMetaclass``.

        Metaclass that converts Forms attributes to a dictionary called
        `form_list`, taking into account parent class 'form_list' as well.
        """

        def __new__(cls, name, bases, attrs):
            """New.

            Form list should be presented in the following way:

            ..code-block: python

                named_contact_forms = (
                    ('contactdata', ContactForm1),
                    ('leavemessage', ContactForm2),
                )

            In the example above, the fist item of the tuple would be
            the slug of the form included. The second one would be the
            form class.
            """
            form_list = []

            for creation_counter, form_entry \
                    in enumerate(form_entries):

                form_cls = assemble_form_class(
                    form_entry,
                    request=request
                )

                form_list.append(
                    (form_entry.slug, form_cls)
                )

            attrs['form_list'] = form_list
            attrs['template_name'] = template_name
            new_class = super(DeclarativeFormsMetaclass, cls).__new__(
                cls, name, bases, attrs
            )

            # if 'media' not in attrs:
            #     new_class.media = media_property(new_class)

            return new_class

    # DynamicFormWizard
    class DynamicFormWizard(with_metaclass(
            DeclarativeFormsMetaclass, base_class)):
        """Dynamically created form wizard class."""

        def done(self, form_list, **kwargs):
            """Done."""
            # do_something_with_the_form_data(form_list)
            redirect_url = reverse('fobi.form_wizard_entry_submitted',
                                   [form_wizard_entry.slug])
            return HttpResponseRedirect(redirect_url)

    # Finally, return the dynamic wizard
    return DynamicFormWizard
