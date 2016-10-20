from django.forms.fields import ChoiceField
from django.forms.widgets import Select
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme
from fobi.helpers import get_select_field_choices

from . import UID
from .constants import SLIDER_DEFAULT_TOOLTIP, SLIDER_DEFAULT_HANDLE
from .forms import SliderInputForm
from .settings import INITIAL, MAX_VALUE, MIN_VALUE, STEP

__title__ = 'fobi.contrib.plugins.form_elements.fields.' \
            'slider_percentage.fobi_form_elements'
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

    def get_form_field_instances(self, request=None):
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

        _choices = range(min_value, max_value, step)
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
            'data-slider-tooltip': tooltip,
            'data-slider-handle': handle,
        }

        if self.data.enable_ticks:
            # if custom_ticks:
            #     pass
            # else:
                tick_label_start = self.data.tick_label_start \
                    if self.data.tick_label_start \
                    else min_value

                tick_label_end = self.data.tick_label_end \
                    if self.data.tick_label_end \
                    else max_value

                widget_attrs.update({
                    'data-slider-ticks': "[{0}, {1}]".format(
                        min_value, max_value
                    ),
                    'data-slider-ticks-labels': '["{0}", "{1}"]'.format(
                        tick_label_start, tick_label_end
                    ),
                })

        # I hate to do so, but it seems like a dirty workaround that works.
        if 'POST' == request.method:
            try:
                value = int(request.POST.get(self.data.name, initial))
            except (ValueError, TypeError) as err:
                value = initial

            if value < min_value or value > max_value:
                value = initial

            widget_attrs.update({
                'data-slider-value': value,
            })
        else:
            widget_attrs.update({
                'data-slider-value': initial,
            })

        kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': initial,
            'required': self.data.required,
            'choices': choices,
            'widget': Select(attrs=widget_attrs),
        }

        return [(self.data.name, ChoiceField, kwargs)]


form_element_plugin_registry.register(SliderInputPlugin)
