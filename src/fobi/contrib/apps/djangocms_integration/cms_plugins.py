from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from fobi.integration.processors import IntegrationProcessor

from .models import FobiFormWidget
from .settings import WIDGET_FORM_SENT_GET_PARAM

__title__ = 'fobi.contrib.apps.djangocms_integration.cms_plugins'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('FobiFormWidgetPlugin',)


class FobiFormWidgetPlugin(CMSPluginBase, IntegrationProcessor):
    """Fobi form widget plugin."""

    model = FobiFormWidget
    name = _("Fobi form")
    render_template = "djangocms_integration/widget.html"
    text_enabled = True
    cache = False

    # Fobi integration processor configuration
    form_sent_get_param = WIDGET_FORM_SENT_GET_PARAM
    can_redirect = False
    login_required_template_name = 'djangocms_integration/login_required.html'

    def process(self, request, instance, **kwargs):
        """This is where most of the form handling happens.

        :param django.http.HttpRequest request:
        :return django.http.HttpResponse | str:
        """
        return self._process(request, instance, **kwargs)

    def render(self, context, instance, placeholder):
        """Render."""
        self.process(context['request'], instance)
        rendered_context = getattr(self, 'rendered_output', '')
        context.update({
            'object': instance,
            'instance': instance,
            'placeholder': placeholder,
            'rendered_context': rendered_context
        })
        return context


plugin_pool.register_plugin(FobiFormWidgetPlugin)
