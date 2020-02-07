
from repeater.views.repeat import complete_url
from repeater.views.repeat import parser
def repeat(url):
    url=complete_url.complete(url)

    webpage=dict()

    p=parser.Parser(url)
    if(not p.is_valid()):
        return None

    webpage['title']=p.get_title()
    webpage['body']=p.get_body()
    webpage['message']="The following content was retrieved from %s"%url
    return webpage