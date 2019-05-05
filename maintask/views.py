from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from .models import Name
from .tasks import demo_task

from logging import getLogger

logger = getLogger(__name__)

def index(request):
    template = loader.get_template('maintask/index.html')

    names = Name.objects.all()

    context = {
        'names': names,
    }

    return HttpResponse(template.render(context, request))


@csrf_exempt
def tasks(request):
    if request.method == 'POST':
        return _post_tasks(request)
    else:
        return JsonResponse({}, status=405)

def _post_tasks(request):
    message = request.POST['message']
    logger.debug('calling demo_task. message={0}'.format(message))
    demo_task(message, repeat=1)
    return JsonResponse({}, status=302)