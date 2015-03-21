#import json

import simplejson as json

from fobi.base import BaseRegistry

class BaseFormImporter(object):
    """
    Base importer.
    """
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

    def __init__(self, form_properties, form_data):
        """
        :param django.contrib.auth.models.User user: User importing the form.
        :param dict form_properties: Properties of the form, that
            user provides (such as name, is_public, etc.)
        """
        assert self.uid
        assert self.name
        assert self.fields_mapping is not None
        assert self.field_properties_mapping is not None
        for prop in ('name', 'label', 'help_text', 'initial', 'required'):
            assert prop in self.field_properties_mapping

        self.form_data = form_data
        self.form_properties = form_properties

    def get_form_data(self):
        return self.form_data

    def extract_field_properties(self, field_data):
        field_properties = {}
        for prop, val in self.field_properties_mapping.items():
            if val in field_data:
                field_properties[prop] = field_data[val]
        return field_properties

    def import_data(self):
        """
        Imports data.
        """
        # TODO: Move this to top level and ensure it works!
        from fobi.models import FormEntry, FormElementEntry
        assert 'name' in self.form_properties
        form_entry = FormEntry()
        for prop, val in self.form_properties.items():
            setattr(form_entry, prop, val)

        form_entry.save()

        data = self.get_form_data()
        for field_data in data:
            # Skip non-existing
            if not field_data[self.field_type_prop_name] in self.fields_mapping:
                continue

            form_element_entry = FormElementEntry()
            form_element_entry.form_entry = form_entry
            form_element_entry.plugin_uid = self.fields_mapping[field_data[self.field_type_prop_name]]

            # Assign form data
            form_element_entry.plugin_data = json.dumps(
                self.extract_field_properties(field_data)
                )

            # Assign position in form
            if self.position_prop_name in field_data:
                form_element_entry.position = field_data[self.position_prop_name]

            form_element_entry.save()



class FormImporterPluginRegistry(BaseRegistry):
    """
    Form importer plugins registry.
    """
    type = BaseFormImporter


# Register form field plugins by calling form_field_plugin_registry.register()
form_importer_plugin_registry = FormImporterPluginRegistry()
