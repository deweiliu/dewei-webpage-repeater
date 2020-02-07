from django.http import HttpResponse
from repeater.views.repeat import decoder
def repeat(request,encoded_url):
   
    url=decoder.decode(encoded_url)
    return HttpResponse("Hello, world. You are visiting %s"%url)