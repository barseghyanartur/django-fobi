from django.db import models
from django.forms.models import ModelChoiceField
from django.forms.widgets import Select
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme
from fobi.contrib.plugins.form_elements.fields.select_model_object import UID
from fobi.helpers import safe_text

from .forms import SelectModelObjectInputForm

theme = get_theme(request=None, as_instance=True)

__all__ = ('SelectModelObjectInputPlugin',)


class SelectModelObjectInputPlugin(FormFieldPlugin):
    """Select model object field plugin."""

    uid = UID
    name = _("Select model object")
    group = _("Fields")
    form = SelectModelObjectInputForm

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        app_label, model_name = self.data.model.split('.')
        model = models.get_model(app_label, model_name)
        queryset = model._default_manager.all()

        field_kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'queryset': queryset,
            'widget': Select(attrs={'class': theme.form_element_html_class}),
        }

        return [(self.data.name, ModelChoiceField, field_kwargs)]

    def submit_plugin_form_data(self, form_entry, request, form,
                                form_element_entries=None, **kwargs):
        """Submit plugin form data/process.

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        """
        # Get the object
        obj = form.cleaned_data.get(self.data.name, None)
        if obj:
            # Handle the submitted form value
            value = '{0}'.format(safe_text(obj))

            # Overwrite ``cleaned_data`` of the ``form`` with object qualifier.
            form.cleaned_data[self.data.name] = value

        # It's critically important to return the ``form`` with updated
        # ``cleaned_data``
        return form


form_element_plugin_registry.register(SelectModelObjectInputPlugin, force=True)
