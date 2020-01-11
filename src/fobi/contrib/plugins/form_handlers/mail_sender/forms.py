from __future__ import absolute_import

from django import forms
from django.utils.translation import gettext_lazy as _

from .....base import BasePluginForm, get_theme

__title__ = 'fobi.contrib.plugins.form_handlers.mail_sender.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('MailSenderForm',)

theme = get_theme(request=None, as_instance=True)


class MailSenderForm(forms.Form, BasePluginForm):
    """Form for ``BooleanSelectPlugin``."""

    plugin_data_fields = [
        ("from_name", ""),
        ("from_email", ""),
        ("to_name", ""),
        ("form_field_name_to_email", ""),
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
    form_field_name_to_email = forms.CharField(
        label=_("Form field name to email"),
        required=True,
        help_text=_("Name of the form field to be used as email."),
        widget=forms.widgets.TextInput(
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
