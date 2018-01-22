from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from fobi.base import FormElementPlugin, get_theme

from . import UID
from .constants import RECAPTCHA_FIELD
from .fields import InvisibleRecaptchaField
from .forms import InvisibleRecaptchaInputForm
from .widgets import InvisibleRecaptchaWidget

__title__ = 'fobi.contrib.plugins.form_elements.security.' \
            'invisible_recaptcha.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('InvisibleRecaptchaInputPlugin',)

theme = get_theme(request=None, as_instance=True)


class InvisibleRecaptchaInputPlugin(FormElementPlugin):
    """Invisible Recaptcha field plugin."""

    uid = UID
    name = _("Invisible Recaptcha")
    group = _("Security")
    form = InvisibleRecaptchaInputForm
    is_hidden = True

    def get_form_field_instances(self,
                                 request=None,
                                 form_entry=None,
                                 form_element_entries=None,
                                 **kwargs):
        """Get form field instances."""

        recaptcha_response = ''
        if request.method == 'POST':
            recaptcha_response = request.POST.get(RECAPTCHA_FIELD)

        field_kwargs = {
            'label': self.data.label,
            'required': self.data.required,
            'widget': InvisibleRecaptchaWidget(
                attrs={'class': theme.form_element_html_class}
            ),
            'recaptcha_response': recaptcha_response,
        }

        return [(self.data.name, InvisibleRecaptchaField, field_kwargs)]
