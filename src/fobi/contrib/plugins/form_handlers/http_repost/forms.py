from django import forms
from django.utils.translation import ugettext_lazy as _

from .....base import BasePluginForm, get_theme

__title__ = 'fobi.contrib.plugins.form_handlers.http_repost.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('HTTPRepostForm',)

theme = get_theme(request=None, as_instance=True)


class HTTPRepostForm(forms.Form, BasePluginForm):
    """Form for ``HTTPRepostPlugin``."""

    plugin_data_fields = [
        ("endpoint_url", ""),
    ]

    endpoint_url = forms.URLField(
        label=_("Endpoint URL"),
        required=True,
        widget=forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )
    )
