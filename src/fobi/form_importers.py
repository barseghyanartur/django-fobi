from nine.versions import DJANGO_GTE_1_10

import simplejson as json

from six import text_type

from .base import BaseRegistry
from .discover import autodiscover

if DJANGO_GTE_1_10:
    from django.urls import reverse
else:
    from django.core.urlresolvers import reverse

__title__ = 'fobi.form_importers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'BaseFormImporter',
    'FormImporterPluginRegistry',
    'form_importer_plugin_registry',
    'ensure_autodiscover',
    'get_form_importer_plugin_uids',
    'get_form_importer_plugin_urls',
)


class BaseFormImporter(object):
    """Base importer."""

    uid = None
    name = None
    description = None

    # field_type (MailChimp): uid (Fobi)
    fields_mapping = None

    # Django standard: remote
    field_properties_mapping = None

    # Position is stored in a model (field)
    field_type_prop_name = None
    position_prop_name = None
    wizard = None
    templates = None

    def __init__(self, form_entry_cls, form_element_entry_cls,
                 form_properties=None, form_data=None):
        """Constructor.

        :param django.contrib.auth.models.User user: User importing the form.
        :param dict form_properties: Properties of the form, that
            user provides (such as name, is_public, etc.)
        """
        assert self.uid
        assert self.name
        assert self.fields_mapping is not None
        assert self.field_properties_mapping is not None
        assert self.wizard is not None
        assert self.templates is not None

        assert form_entry_cls is not None
        assert form_element_entry_cls is not None

        for prop in ('name', 'label', 'help_text', 'initial', 'required'):
            assert prop in self.field_properties_mapping

        self.form_data = form_data
        self.form_properties = form_properties
        self.form_entry_cls = form_entry_cls
        self.form_element_entry_cls = form_element_entry_cls

    def get_form_data(self):
        """Get form data."""
        return self.form_data

    def extract_field_properties(self, field_data):
        """Extract field properties."""
        field_properties = {}
        for prop, val in self.field_properties_mapping.items():
            if val in field_data:
                field_properties[prop] = field_data[val]
        return field_properties

    def import_data(self, form_properties, form_data):
        """Import data."""
        self.form_properties = form_properties
        self.form_data = form_data

        assert 'name' in self.form_properties
        form_entry = self.form_entry_cls()
        for prop, val in self.form_properties.items():
            setattr(form_entry, prop, val)

        form_entry.save()

        data = self.get_form_data()
        for field_data in data:
            # Skip non-existing
            if field_data[self.field_type_prop_name] \
                    not in self.fields_mapping:
                continue

            form_element_entry = self.form_element_entry_cls()
            form_element_entry.form_entry = form_entry
            form_element_entry.plugin_uid = self.fields_mapping[
                field_data[self.field_type_prop_name]]

            # Assign form data
            form_element_entry.plugin_data = json.dumps(
                self.extract_field_properties(field_data)
            )

            # Assign position in form
            if self.position_prop_name in field_data:
                form_element_entry.position = field_data[
                    self.position_prop_name
                ]

            form_element_entry.save()

        return form_entry

    def get_template_names(self):
        """Get template names."""
        return {text_type(idx): tpl for idx, tpl in enumerate(self.templates)}

    def get_wizard(self, request, *args, **kwargs):
        """Get wizard."""
        template_names = self.get_template_names()

        class FormImporterWizard(self.wizard):
            """Constructing the importer class dynamically."""

            _form_importer = self

            def get_template_names(self):
                """Get template names."""
                return [template_names[self.steps.current]]

        wizard = FormImporterWizard.as_view()
        return wizard(request, *args, **kwargs)


class FormImporterPluginRegistry(BaseRegistry):
    """Form importer plugins registry."""

    type = BaseFormImporter


# Register form field plugins by calling form_field_plugin_registry.register()
form_importer_plugin_registry = FormImporterPluginRegistry()


def ensure_autodiscover():
    """Ensure that form importer plugins are auto-discovered."""
    if not form_importer_plugin_registry._registry:
        autodiscover()


def get_form_importer_plugin_uids():
    """Get form importer plugin uids."""
    ensure_autodiscover()
    return list(form_importer_plugin_registry._registry.keys())


def get_form_importer_plugin_urls():
    """Gets the form importer plugin URLs as a list of tuples."""
    urls = []
    ensure_autodiscover()
    for uid, plugin in form_importer_plugin_registry._registry.items():
        urls.append(
            (
                uid,
                plugin.name,
                reverse('fobi.form_importer',
                        kwargs={'form_importer_plugin_uid': uid})
            )
        )
    return urls
