from django.http import HttpResponse
from django.template import loader

from repeater.views.repeat import repeat
from repeater.views import home


def controller(request):
    url = request.GET.get('url')
    if(url == None or url == ''):
        response = home.home()
    else:
        response = repeat.repeat(url)

    template = loader.get_template(response['html'])
    return HttpResponse(template.render(response['variables'], request))
