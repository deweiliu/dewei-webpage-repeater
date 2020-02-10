from django.http import HttpResponse
from django.template import loader
from repeater.views.repeat import repeat
import os
from repeater.views import get_time


def controller(request):
    url = request.GET.get('url')
    webpage = dict()
    if(url == None):
        html = 'repeater/home.html'
    else:
        webpage = repeat.repeat(url)
        html = 'repeater/repeat.html'

    build_time = os.getenv('build_time',default=0)
    webpage['build_time'] = get_time.string(build_time)

    deploy_time = os.getenv('deploy_time')
    webpage['deploy_time'] = get_time.string(deploy_time)

    template = loader.get_template(html)
    return HttpResponse(template.render(webpage, request))
