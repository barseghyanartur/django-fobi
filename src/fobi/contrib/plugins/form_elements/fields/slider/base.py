from __future__ import absolute_import

from six import text_type, PY3

from django.forms.fields import ChoiceField
from django.forms.utils import flatatt
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from nine import versions

from fobi.base import (
    FormFieldPlugin,
    get_theme
)
from fobi.helpers import get_select_field_choices
from fobi.widgets import RichSelectInverseQuotes

from . import UID
from .constants import (
    SLIDER_DEFAULT_TOOLTIP,
    SLIDER_DEFAULT_HANDLE,
    SLIDER_SHOW_ENDPOINTS_AS_LABELED_TICKS,
    SLIDER_SHOW_ENDPOINTS_AS_TICKS,
    SLIDER_DEFAULT_SHOW_ENDPOINTS_AS
)
from .forms import SliderInputForm
from .helpers import generate_ticks
from .settings import (
    INITIAL,
    INITIAL_MAX_VALUE,
    INITIAL_MIN_VALUE,
    # MAX_VALUE,
    # MIN_VALUE,
    STEP
)

__title__ = 'fobi.contrib.plugins.form_elements.fields.slider.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
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

    def get_initial(self):
        """Get initial value.

        Might be used in integration plugins.
        """
        return int(self.data.initial) if self.data.initial else INITIAL

    def get_choices(self):
        """Get choices.

        Might be used in integration plugins.
        """
        max_value = int(self.data.max_value) \
            if self.data.max_value is not None \
            else INITIAL_MAX_VALUE
        min_value = int(self.data.min_value) \
            if self.data.min_value is not None \
            else INITIAL_MIN_VALUE
        step = int(self.data.step) if self.data.step is not None else STEP

        if PY3:
            _choices = [__r for __r in range(min_value, max_value + 1, step)]
            choices = [(__k, __v) for __k, __v in zip(_choices, _choices)]
        else:
            _choices = range(min_value, max_value + 1, step)
            choices = zip(_choices, _choices)

        return choices

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        initial = self.get_initial()
        max_value = int(self.data.max_value) \
            if self.data.max_value is not None \
            else INITIAL_MAX_VALUE
        min_value = int(self.data.min_value) \
            if self.data.min_value is not None \
            else INITIAL_MIN_VALUE
        step = int(self.data.step) if self.data.step is not None else STEP
        tooltip = self.data.tooltip \
            if self.data.tooltip is not None \
            else SLIDER_DEFAULT_TOOLTIP
        handle = self.data.handle \
            if self.data.handle is not None \
            else SLIDER_DEFAULT_HANDLE

        custom_ticks = get_select_field_choices(self.data.custom_ticks,
                                                key_type=int,
                                                value_type=text_type) \
            if self.data.custom_ticks \
            else []

        choices = self.get_choices()

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

            if custom_ticks:
                ticks_data = generate_ticks(custom_ticks)
            else:
                ticks_data = generate_ticks([
                    (min_value, self.data.label_start),
                    (max_value, self.data.label_end),
                ])
            # label_start = self.data.label_start \
            #     if self.data.label_start \
            #     else text_type(min_value)
            #
            # label_end = self.data.label_end \
            #     if self.data.label_end \
            #     else text_type(max_value)

            # widget_attrs.update({
            #     'data-slider-ticks': "[{0}, {1}]".format(
            #         min_value, max_value
            #     ),
            #     'data-slider-ticks-labels': '["{0!s}", "{1!s}"]'.format(
            #         label_start.encode('utf8'), label_end.encode('utf8')
            #     ),
            # })

            widget_attrs.update(ticks_data)

        # Show endpoints as ticks
        elif SLIDER_SHOW_ENDPOINTS_AS_TICKS == show_endpoints_as:

            if custom_ticks:
                ticks_data = generate_ticks(custom_ticks, empty_labels=True)
            else:
                ticks_data = generate_ticks([
                    (min_value, ""),
                    (max_value, ""),
                ])

            # widget_attrs.update({
            #     'data-slider-ticks': "[{0}, {1}]".format(
            #         min_value, max_value
            #     ),
            #     'data-slider-ticks-labels': '["{0}", "{1}"]'.format(
            #         "", ""
            #     ),
            # })

            widget_attrs.update(ticks_data)

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
            'widget': RichSelectInverseQuotes(**widget_kwargs),
        }

        return [(self.data.name, ChoiceField, field_kwargs)]
