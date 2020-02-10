
from repeater.views.repeat import complete_url
from repeater.views.repeat import request
from repeater.views.repeat import parser
from repeater.views import get_time

def repeat(url):
    webpage = dict()
    webpage['title'] = "N/A"
    webpage['body'] = "N/A"    
    start = float(get_time.value())

    url = complete_url.complete(url)
    r = request.Request(url)
    if(r.is_valid()):
        try:
            response = r.get_response()
            p = parser.Parser(response)
            webpage['title'] = p.get_title()
            webpage['body'] = p.get_body()
            webpage['head'] = p.get_head()
        except:
            pass

    finish = float(get_time.value())
    processing_time = "%sms" % ((finish-start)*1000)
    webpage['processing_time'] = processing_time

    webpage['response_time'] = r.get_response_time()
    webpage['status'] = r.get_status()
    webpage['gmt_time'] = r.get_time()
    webpage['url'] = url
    return webpage
