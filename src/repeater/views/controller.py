from django.http import HttpResponse
from django.template import loader

from repeater.views.repeat import repeat
from repeater.views import home


def controller(request):
    default_url = "https://en.wikipedia.org"
    url = request.GET.get('url')

    if(url == None):
        response = home.home(default_url)
    else:
        if(url == ''):
            url = default_url
        response = repeat.repeat(url)

    template = loader.get_template(response['html'])

    return HttpResponse(template.render(response['variables'], request))
