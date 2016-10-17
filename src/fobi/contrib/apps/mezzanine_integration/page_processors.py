# from mezzanine.conf import settings
from mezzanine.pages.page_processors import processor_for

from fobi.integration.processors import IntegrationProcessor

from .models import FobiFormPage
from .settings import WIDGET_FORM_SENT_GET_PARAM

__title__ = 'fobi.contrib.apps.mezzanine_integration.page_processors'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'FobiFormProcessor',
    'process_fobi_form',
)


class FobiFormProcessor(IntegrationProcessor):
    """Form processor."""

    form_sent_get_param = WIDGET_FORM_SENT_GET_PARAM

    def process(self, request, instance, **kwargs):
        """This is where most of the form handling happens.

        :param django.http.HttpRequest request:
        :return django.http.HttpResponse | str:
        """
        return self._process(request, instance, **kwargs)


@processor_for(FobiFormPage)
def process_fobi_form(request, page):
    """Process the ``FobiFormPage``."""
    fobi_form_processor = FobiFormProcessor()
    response = fobi_form_processor.process(
        request, instance=page.get_content_model()
    )

    if response:
        return response

    return {
        'fobi_form_response': getattr(fobi_form_processor, 'rendered_output')
    }
