from django.http import HttpResponse
from repeater.views.repeat import decoder
from repeater.views.repeat import parser
def repeat(request,encoded_url):
   
    url=decoder.decode(encoded_url)
    webpage=parser.parse_webpage(url)

    return HttpResponse(webpage['content'])