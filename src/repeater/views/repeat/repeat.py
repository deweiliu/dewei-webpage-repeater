
from repeater.views.repeat import complete_url
from repeater.views.repeat import request
from repeater.views.repeat import parser


def repeat(url):
    url = complete_url.complete(url)

    webpage = dict()
    r = request.Request(url)

    if(r.is_valid()):

        response = r.get_response()
        p = parser.Parser(response)
        webpage['title'] = p.get_title()
        webpage['body'] = p.get_body()

    else:
        webpage['title'] = "N/A"
        webpage['body'] = "N/A"

    webpage['status'] = r.get_status()
    webpage['gmt_time'] = r.get_time()
    webpage['url'] = url
    return webpage
