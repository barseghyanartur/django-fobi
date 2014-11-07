__title__ = 'fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('SelectMultipleModelObjectsInputPlugin',)

from django.db import models
from django.forms.models import ModelChoiceField
from django.forms.widgets import SelectMultiple
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme
from fobi.helpers import admin_change_url
from fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects \
    import UID
from fobi.contrib.plugins.form_elements.fields.select_multiple_model_objects.forms import (
    SelectMultipleModelObjectsInputForm
    )

theme = get_theme(request=None, as_instance=True)

class SelectMultipleModelObjectsInputPlugin(FormFieldPlugin):
    """
    Select model object field plugin.
    """
    uid = UID
    name = _("Select multiple model objects")
    group = _("Fields")
    form = SelectMultipleModelObjectsInputForm

    def get_form_field_instances(self):
        """
        Get form field instances.
        """
        app_label, model_name = self.data.model.split('.')
        model = models.get_model(app_label, model_name)
        queryset = model._default_manager.all()

        kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'queryset': queryset,
            'widget': SelectMultiple(attrs={'class': theme.form_element_html_class}),
        }

        return [(self.data.name, ModelChoiceField, kwargs)]

    def __submit_plugin_form_data(self, form_entry, request, form):
        """
        Submit plugin form data/process.

        :param fobi.models.FormEntry form_entry: Instance of ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        """
        # Get the object
        obj = form.cleaned_data.get(self.data.name, None)

        if obj:
            # Handle the upload
            admin_url = admin_change_url(
                app_label = obj._meta.app_label,
                module_name = obj._meta.module_name,
                object_id = obj.pk
                )
            repr = '<a href="{0}">{1}</a>'.format(admin_url, str(obj))

            # Overwrite ``cleaned_data`` of the ``form`` with object qualifier.
            form.cleaned_data[self.data.name] = repr

        # It's critically important to return the ``form`` with updated ``cleaned_data``
        return form


form_element_plugin_registry.register(SelectMultipleModelObjectsInputPlugin)
