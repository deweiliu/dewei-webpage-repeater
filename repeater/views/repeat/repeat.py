from django.http import HttpResponse
from repeater.views.repeat import decoder
from repeater.views.repeat import parser
from django.template import loader

def repeat(request,encoded_url):
    url=decoder.decode(encoded_url)
    webpage=parser.parse_webpage(url)


    template = loader.get_template('repeater/repeat.html')

    return HttpResponse(template.render(webpage, request))    
    
