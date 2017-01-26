from __future__ import absolute_import

import simplejson as json

from django.forms.widgets import SelectMultiple
from django.utils.translation import ugettext_lazy as _

from mptt.fields import TreeNodeMultipleChoiceField

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

from nine.versions import DJANGO_GTE_1_7

from . import UID
from .forms import SelectMultipleMPTTModelObjectsInputForm
from .settings import SUBMIT_VALUE_AS

if DJANGO_GTE_1_7:
    from django.apps import apps
    get_model = apps.get_model
else:
    from django.db.models import get_model

__title__ = 'fobi.contrib.plugins.form_elements.fields.' \
            'select_multiple_mptt_model_objects.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('SelectMultipleMPTTModelObjectsInputPlugin',)

theme = get_theme(request=None, as_instance=True)


class SelectMultipleMPTTModelObjectsInputPlugin(FormFieldPlugin):
    """Select multiple MPTT model object field plugin."""

    uid = UID
    name = _("Select multiple MPTT model objects")
    group = _("Fields")
    form = SelectMultipleMPTTModelObjectsInputForm

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        app_label, model_name = get_app_label_and_model_name(self.data.model)
        model = get_model(app_label, model_name)
        queryset = model._default_manager.all()

        field_kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'queryset': queryset,
            'widget': SelectMultiple(
                attrs={'class': theme.form_element_html_class}
            ),
        }

        return [(self.data.name, TreeNodeMultipleChoiceField, field_kwargs)]

    def submit_plugin_form_data(self, form_entry, request, form,
                                form_element_entries=None, **kwargs):
        """Submit plugin form data/process.

        :param fobi.models.FormEntry form_entry: Instance of
            ``fobi.models.FormEntry``.
        :param django.http.HttpRequest request:
        :param django.forms.Form form:
        """
        # In case if we should submit value as is, we don't return anything.
        # In other cases, we proceed further.

        # Get the object
        objs = form.cleaned_data.get(self.data.name, [])

        values = []

        for obj in objs:
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
                values.append(value)

        # Overwrite ``cleaned_data`` of the ``form`` with object qualifier.
        if values:
            form.cleaned_data[self.data.name] = json.dumps(values)
        else:
            del form.cleaned_data[self.data.name]

        # It's critically important to return the ``form`` with updated
        # ``cleaned_data``
        return form
