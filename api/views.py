import logging
from django.conf import settings
#from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
#from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from core import main_tools


logger = logging.getLogger('django')


@csrf_exempt
@api_view(['GET',])
@renderer_classes([JSONRenderer])
def search(request):
    """
    get:Returns a list of songs matching key words
    """
    q = request.GET.get('q', None)  # q is the GET param for searching
    local_only = True and request.GET.get('local', False)  # local is the GET param to avoid YouTube search
    if q is None:
        return Response( {'status': 'ERR', 'results': list(), 'errors': 'Please, provide a valid search term.'} )
    else:
        return Response( {'status': 'OK', 'results': main_tools.search(q, local_only), 'errors': ''} )
