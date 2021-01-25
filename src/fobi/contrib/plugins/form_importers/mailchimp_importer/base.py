from django.utils.translation import gettext_lazy as _

from .....contrib.plugins.form_elements import fields
from .....form_importers import BaseFormImporter

from .views import MailchimpImporterWizardView

__title__ = 'fobi.contrib.plugins.form_importers.mailchimp_importer.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('MailChimpImporter',)


class MailChimpImporter(BaseFormImporter):
    """MailChimp data importer."""

    uid = 'mailchimp'
    name = _("MailChimp")
    wizard = MailchimpImporterWizardView
    templates = [
        'mailchimp_importer/0.html',
        'mailchimp_importer/1.html',
    ]

    # field_type (MailChimp): uid (django-fobi)
    fields_mapping = {
        # Implemented
        'email': fields.email.UID,
        'text': fields.text.UID,
        'number': fields.integer.UID,
        'dropdown': fields.select.UID,
        'date': fields.date.UID,
        'url': fields.url.UID,
        'radio': fields.radio.UID,

        # Transformed into something else
        'address': fields.text.UID,
        'zip': fields.text.UID,
        'phone': fields.text.UID,
        'imageurl': fields.url.UID,

        # Not implemented yet
        # 'birthday': '???',
    }

    # Django standard: remote
    field_properties_mapping = {
        'label': 'name',
        'name': 'tag',
        'help_text': 'helptext',
        'initial': 'default',
        'required': 'req',
        'choices': 'choices',
    }

    field_type_prop_name = 'field_type'
    position_prop_name = 'order'

    def extract_field_properties(self, field_data):
        """Extract field properties.

        Handle choices differently as we know what the mailchimp
        format is.
        """
        field_properties = {}
        for prop, val in self.field_properties_mapping.items():
            if val in field_data:
                if 'choices' == val:
                    field_properties[prop] = "\n".join(field_data[val])
                else:
                    field_properties[prop] = field_data[val]
        return field_properties
