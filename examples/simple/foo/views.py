import uuid
import logging

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from fobi.helpers import handle_uploaded_file

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

    return HttpResponse("POST: {0}\nFILES: {1}".format(request.POST, request.FILES))
