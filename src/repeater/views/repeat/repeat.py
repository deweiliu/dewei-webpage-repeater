
from repeater.views.repeat import complete_url
from repeater.views.repeat import request
from repeater.views.repeat import parser
from repeater.views import get_time


def repeat(url):
    result = dict()

    # HTML template
    result['html'] = 'repeater/repeat.html'

    # variables
    variables = dict()
    variables['title'] = "N/A"
    variables['body'] = "N/A"
    start = float(get_time.value())

    url = complete_url.complete(url)
    r = request.Request(url)
    if(r.is_valid()):
        try:
            response = r.get_response()
            p = parser.Parser(response)
            variables['title'] = p.get_title()
            variables['body'] = p.get_body()
            variables['head'] = p.get_head()
        except:
            pass

    finish = float(get_time.value())
    variables['processing_time'] = "%.0fms" % ((finish-start)*1000)
    variables['response_time'] = "%.0fms" % (r.get_response_time())
    variables['status'] = r.get_status()
    variables['gmt_time'] = r.get_time()
    variables['url'] = url

    result['variables'] = variables
    return result
