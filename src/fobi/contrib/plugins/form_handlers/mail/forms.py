from __future__ import absolute_import

from django import forms
from django.utils.translation import ugettext_lazy as _

from .....base import BasePluginForm, get_theme

from .fields import MultiEmailField
from .widgets import MultiEmailWidget

__title__ = 'fobi.contrib.plugins.form_handlers.mail.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('MailForm',)

theme = get_theme(request=None, as_instance=True)


class MailForm(forms.Form, BasePluginForm):
    """Form for ``BooleanSelectPlugin``."""

    plugin_data_fields = [
        ("from_name", ""),
        ("from_email", ""),
        ("to_name", ""),
        ("to_email", ""),
        ("subject", ""),
        ("body", ""),
    ]

    from_name = forms.CharField(
        label=_("From name"),
        required=True,
        widget=forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )
    )
    from_email = forms.EmailField(
        label=_("From email"),
        required=True,
        widget=forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )
    )
    to_name = forms.CharField(
        label=_("To name"),
        required=True,
        widget=forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )
    )
    to_email = MultiEmailField(  # forms.EmailField(
        label=_("To email"),
        required=True,
        widget=MultiEmailWidget(  # forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )
    )
    subject = forms.CharField(
        label=_("Subject"),
        required=True,
        widget=forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )
    )
    body = forms.CharField(
        label=_("Body"),
        required=False,
        widget=forms.widgets.Textarea(
            attrs={'class': theme.form_element_html_class}
        )
    )
