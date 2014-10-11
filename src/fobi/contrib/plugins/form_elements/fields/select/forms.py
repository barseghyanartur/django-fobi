__title__ = 'fobi.contrib.plugins.form_elements.fields.select.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('SelectInputForm',)

from django import forms
from django.utils.translation import ugettext_lazy as _

from fobi.base import BaseFormFieldPluginForm, get_theme

theme = get_theme(request=None, as_instance=True)

class SelectInputForm(forms.Form, BaseFormFieldPluginForm):
    """
    Form for ``SelectInputPlugin``.
    """
    plugin_data_fields = [
        ("label", ""),
        ("name", ""),
        ("choices", ""),
        ("help_text", ""),
        ("initial", ""),
        ("required", False)
    ]

    label = forms.CharField(
        label = _("Label"),
        required = True,
        widget = forms.widgets.TextInput(attrs={'class': theme.form_element_html_class})
        )
    name = forms.CharField(
        label = _("Name"),
        required = True,
        widget = forms.widgets.TextInput(attrs={'class': theme.form_element_html_class})
        )
    choices = forms.CharField(
        label = _("Choices"),
        required = False,
        help_text = _("Enter either single values or pairs - one per line. Example:<code><br/>"
                      "&nbsp;&nbsp;&nbsp;&nbsp;1<br/>"
                      "&nbsp;&nbsp;&nbsp;&nbsp;2<br/>"
                      "&nbsp;&nbsp;&nbsp;&nbsp;alpha, Alpha<br/>"
                      "&nbsp;&nbsp;&nbsp;&nbsp;beta, Beta<br/>"
                      "&nbsp;&nbsp;&nbsp;&nbsp;omega"
                      "</code><br/>"
                      "It finally transforms into the following Python code:<code><br/>"
                      '&nbsp;&nbsp;&nbsp;&nbsp;(<br />'
                      '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1, 1),<br/>'
                      '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2, 2),<br/>'
                      '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;("alpha", "Alpha"),<br/>'
                      '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;("beta", "Beta"),<br/>'
                      '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;("omega", "omega"))<br/>'
                      '&nbsp;&nbsp;&nbsp;&nbsp;)'
                      "</code>"),
        widget = forms.widgets.Textarea(attrs={'class': theme.form_element_html_class})
        )
    help_text = forms.CharField(
        label = _("Help text"),
        required = False,
        widget = forms.widgets.Textarea(attrs={'class': theme.form_element_html_class})
        )
    initial = forms.CharField(
        label = _("Initial"),
        required = False,
        widget = forms.widgets.TextInput(attrs={'class': theme.form_element_html_class})
        )
    required = forms.BooleanField(
        label = _("Required"),
        required = False,
        widget = forms.widgets.CheckboxInput(attrs={'class': theme.form_element_html_class})
        )
