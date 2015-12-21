import uuid
import logging

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.shortcuts import render_to_response

from fobi.models import FormEntry
from fobi.helpers import handle_uploaded_file
from fobi.base import get_theme

logger = logging.getLogger('fobi')

@csrf_exempt
def endpoint(request):
    """
    Endpoint.

    :param django.http.HttpRequest request:
    :param string template_name:
    :return django.http.HttpResponse:
    """
    logger.debug("POST: {0}\nFILES: {1}".format(request.POST, request.FILES))

    for field_name, imf in request.FILES.items():
        handle_uploaded_file('foo', "{0}".format(uuid.uuid4()))

    return HttpResponse(
        "POST: {0}\nFILES: {1}".format(request.POST, request.FILES)
    )


def forms_list(request, template_name='foo/forms_list.html'):
    """
    Fobi forms list.
    """
    form_entries = FormEntry._default_manager.filter(is_public=True) \
                                             .select_related('user')
    theme = get_theme(request=request, as_instance=True)
    context = {
        'form_entries': form_entries,
        'theme': theme,
        'show_custom_actions': False,
        'show_edit_link': False,
        'show_delete_link': False,
        'show_export_link': False,
    }
    return render_to_response(
        template_name, context, context_instance=RequestContext(request)
    )
