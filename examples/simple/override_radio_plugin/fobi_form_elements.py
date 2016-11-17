from django.forms.fields import ChoiceField
from django.forms.widgets import RadioSelect
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme
from fobi.contrib.plugins.form_elements.fields.radio import UID
from fobi.helpers import safe_text, get_select_field_choices

from .forms import RadioInputForm

theme = get_theme(request=None, as_instance=True)

__all__ = ('RadioInputPlugin',)


class RadioInputPlugin(FormFieldPlugin):
    """Radio field plugin."""

    uid = UID
    name = _("Radio")
    group = _("Fields")
    form = RadioInputForm

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        choices = get_select_field_choices(self.data.choices)

        widget_attrs = {'class': theme.form_radio_element_html_class}
        field_kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'choices': choices,
            'widget': RadioSelect(attrs=widget_attrs),
        }

        return [(self.data.name, ChoiceField, field_kwargs)]

    def submit_plugin_form_data(self, form_entry, request, form,
                                form_element_entries=None, **kwargs):
        """Submit plugin form data/process.

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        """
        # Get the object
        value = form.cleaned_data.get(self.data.name, None)

        if value:
            choices = dict(get_select_field_choices(self.data.choices))
            # Handle the submitted form value
            value = '{0}'.format(safe_text(choices.get(value)))

            # Overwrite ``cleaned_data`` of the ``form`` with object qualifier.
            form.cleaned_data[self.data.name] = value

        # It's critically important to return the ``form`` with updated
        # ``cleaned_data``
        return form


form_element_plugin_registry.register(RadioInputPlugin, force=True)
