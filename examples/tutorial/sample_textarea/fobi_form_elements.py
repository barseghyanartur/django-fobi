from django import forms

from fobi.base import FormFieldPlugin, form_element_plugin_registry

from .forms import SampleTextareaForm


class SampleTextareaPlugin(FormFieldPlugin):
    """SampleTextareaPlugin."""

    uid = "sample_textarea"
    name = "Sample Textarea"
    form = SampleTextareaForm
    group = "Samples"  # Group to which the plugin belongs to

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        field_kwargs = {
            'required': self.data.required,
            'label': self.data.label,
            'initial': self.data.initial,
            'widget': forms.widgets.Textarea(attrs={})
        }

        return [(self.data.name, forms.CharField, field_kwargs)]


form_element_plugin_registry.register(SampleTextareaPlugin)
