from six import text_type

from django.forms.fields import ChoiceField
from django.forms.utils import flatatt
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme
from fobi.widgets import RichSelect

from . import UID
from .constants import (
    SLIDER_DEFAULT_TOOLTIP,
    SLIDER_DEFAULT_HANDLE,
    SLIDER_SHOW_ENDPOINTS_AS_LABELED_TICKS,
    SLIDER_SHOW_ENDPOINTS_AS_TICKS,
    SLIDER_DEFAULT_SHOW_ENDPOINTS_AS
)
from .forms import SliderInputForm
from .settings import INITIAL, MAX_VALUE, MIN_VALUE, STEP

__title__ = 'fobi.contrib.plugins.form_elements.fields.slider.' \
            'fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('SliderInputPlugin',)

theme = get_theme(request=None, as_instance=True)


class SliderInputPlugin(FormFieldPlugin):
    """Slider field plugin."""

    uid = UID
    name = _("Slider")
    group = _("Fields")
    form = SliderInputForm
    html_classes = ['slider']

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        initial = self.data.initial if self.data.initial else INITIAL
        max_value = self.data.max_value if self.data.max_value else MAX_VALUE
        min_value = self.data.min_value if self.data.min_value else MIN_VALUE
        step = self.data.step if self.data.step else STEP
        tooltip = self.data.tooltip \
            if self.data.tooltip \
            else SLIDER_DEFAULT_TOOLTIP
        handle = self.data.handle \
            if self.data.handle \
            else SLIDER_DEFAULT_HANDLE

        # custom_ticks = get_select_field_choices(self.data.custom_ticks) \
        #     if self.data.custom_ticks \
        #     else []

        _choices = range(min_value, max_value+1, step)
        choices = zip(_choices, _choices)

        # slider_html_class = "slider-no-background" \
        #     if self.data.disable_slider_background \
        #     else "slider"
        slider_html_class = "slider"

        widget_attrs = {
            'class': "{0} {1}".format(
                slider_html_class,
                theme.form_element_html_class
            ),
            'data-slider-min': min_value,
            'data-slider-max': max_value,
            'data-slider-step': step,
            'data-slider-value': initial,
            'data-slider-tooltip': tooltip,
            'data-slider-handle': handle,
        }

        show_endpoints_as = self.data.show_endpoints_as \
            if self.data.show_endpoints_as \
            else SLIDER_DEFAULT_SHOW_ENDPOINTS_AS

        prepend_html_list = []
        append_html_list = []

        # Show endpoints as labeled ticks
        if SLIDER_SHOW_ENDPOINTS_AS_LABELED_TICKS == show_endpoints_as:

            label_start = self.data.label_start \
                if self.data.label_start \
                else text_type(min_value)

            label_end = self.data.label_end \
                if self.data.label_end \
                else text_type(max_value)

            widget_attrs.update({
                'data-slider-ticks': "[{0}, {1}]".format(
                    min_value, max_value
                ),
                'data-slider-ticks-labels': '["{0!s}", "{1!s}"]'.format(
                    label_start.encode('utf8'), label_end.encode('utf8')
                ),
            })

        # Show endpoints as ticks
        elif SLIDER_SHOW_ENDPOINTS_AS_TICKS == show_endpoints_as:

            widget_attrs.update({
                'data-slider-ticks': "[{0}, {1}]".format(
                    min_value, max_value
                ),
                'data-slider-ticks-labels': '["{0}", "{1}"]'.format(
                    "", ""
                ),
            })

        # Show endpoints as labels
        else:

            if self.data.label_start:
                prepend_html_list.append(
                    format_html(
                        " <span {}>",
                        flatatt({'class': "slider-endpoint-label-start"})
                    )
                )
                prepend_html_list.append(format_html(self.data.label_start))
                prepend_html_list.append(format_html(" </span>"))

            if self.data.label_end:
                append_html_list.append(
                    format_html(
                        " <span {}>",
                        flatatt({'class': "slider-endpoint-label-end"})
                    )
                )
                append_html_list.append(format_html(self.data.label_end))
                append_html_list.append(format_html(" </span>"))

        widget_kwargs = {'attrs': widget_attrs}

        # For showing endpoints as labels
        if prepend_html_list:
            widget_kwargs.update({
                'prepend_html': mark_safe(''.join(prepend_html_list)),
            })

        if append_html_list:
            widget_kwargs.update({
                'append_html': mark_safe(''.join(append_html_list)),
            })

        field_kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': initial,
            'required': self.data.required,
            'choices': choices,
            'widget': RichSelect(**widget_kwargs),
        }

        return [(self.data.name, ChoiceField, field_kwargs)]


form_element_plugin_registry.register(SliderInputPlugin)
