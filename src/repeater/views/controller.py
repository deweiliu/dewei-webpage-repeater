from django.http import HttpResponse
from django.template import loader
from repeater.views.repeat import repeat


def controller(request):
    url = request.GET.get('url')
    webpage = dict()
    if(url == None):
        html = 'repeater/home.html'
    else:
        webpage = repeat.repeat(url)
        html = 'repeater/repeat.html'


    template = loader.get_template(html)
    return HttpResponse(template.render(webpage, request))
