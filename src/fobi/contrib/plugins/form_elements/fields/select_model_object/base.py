from __future__ import absolute_import

from django.apps import apps
from django.forms.models import ModelChoiceField
from django.forms.widgets import Select
from django.utils.translation import gettext_lazy as _

from fobi.base import FormFieldPlugin, get_theme
from fobi.constants import (
    SUBMIT_VALUE_AS_VAL,
    SUBMIT_VALUE_AS_REPR
)
from fobi.helpers import (
    safe_text,
    get_app_label_and_model_name,
    get_model_name_for_object
)

from . import UID
from .forms import SelectModelObjectInputForm
from .settings import SUBMIT_VALUE_AS

__title__ = 'fobi.contrib.plugins.form_elements.fields.' \
            'select_model_object.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('SelectModelObjectInputPlugin',)

theme = get_theme(request=None, as_instance=True)


class SelectModelObjectInputPlugin(FormFieldPlugin):
    """Select model object field plugin."""

    uid = UID
    name = _("Select model object")
    group = _("Fields")
    form = SelectModelObjectInputForm

    def get_queryset(self):
        """Get queryset.

        Might be used in integration packages.
        """
        app_label, model_name = get_app_label_and_model_name(self.data.model)
        model = apps.get_model(app_label, model_name)
        queryset = model._default_manager.all()
        return queryset

    def get_form_field_instances(self,
                                 request=None,
                                 form_entry=None,
                                 form_element_entries=None,
                                 **kwargs):
        """Get form field instances."""
        queryset = self.get_queryset()

        field_kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'queryset': queryset,
            'widget': Select(attrs={'class': theme.form_element_html_class}),
        }

        return [(self.data.name, ModelChoiceField, field_kwargs)]

    def prepare_plugin_form_data(self, cleaned_data):
        """Prepare plugin form data.

        Might be used in integration plugins.
        """
        # In case if we should submit value as is, we don't return anything.
        # In other cases, we proceed further.

        # Get the object
        obj = cleaned_data.get(self.data.name, None)
        if obj:
            value = None
            # Should be returned as repr
            if SUBMIT_VALUE_AS == SUBMIT_VALUE_AS_REPR:
                value = safe_text(obj)
            elif SUBMIT_VALUE_AS == SUBMIT_VALUE_AS_VAL:
                value = '{0}.{1}.{2}'.format(
                    obj._meta.app_label,
                    get_model_name_for_object(obj),
                    obj.pk
                )
            else:
                # Handle the submitted form value
                value = '{0}.{1}.{2}.{3}'.format(
                    obj._meta.app_label,
                    get_model_name_for_object(obj),
                    obj.pk,
                    safe_text(obj)
                )

            # Overwrite ``cleaned_data`` of the ``form`` with object
            # qualifier.
            cleaned_data[self.data.name] = value

            # It's critically important to return the ``form`` with updated
            # ``cleaned_data``
            return cleaned_data

    def submit_plugin_form_data(self,
                                form_entry,
                                request,
                                form,
                                form_element_entries=None,
                                **kwargs):
        """Submit plugin form data/process.

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        """
        # In case if we should submit value as is, we don't return anything.
        # In other cases, we proceed further.

        # Get the object
        obj = form.cleaned_data.get(self.data.name, None)
        if obj:
            value = None
            # Should be returned as repr
            if SUBMIT_VALUE_AS == SUBMIT_VALUE_AS_REPR:
                value = safe_text(obj)
            elif SUBMIT_VALUE_AS == SUBMIT_VALUE_AS_VAL:
                value = '{0}.{1}.{2}'.format(
                    obj._meta.app_label,
                    get_model_name_for_object(obj),
                    obj.pk
                )
            else:
                # Handle the submitted form value
                value = '{0}.{1}.{2}.{3}'.format(
                    obj._meta.app_label,
                    get_model_name_for_object(obj),
                    obj.pk,
                    safe_text(obj)
                )

            # Overwrite ``cleaned_data`` of the ``form`` with object
            # qualifier.
            form.cleaned_data[self.data.name] = value

        # It's critically important to return the ``form`` with updated
        # ``cleaned_data``
        return form
