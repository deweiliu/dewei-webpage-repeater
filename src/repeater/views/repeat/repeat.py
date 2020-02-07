import requests
import html2text
from repeater.views.repeat import complete_url
def repeat(url):
    url=complete_url.complete(url)

    webpage=dict()

    try:
        response=requests.get(url)
    except:
        return None
    body=response.text
    
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    text = converter.handle(body)

    webpage['title']='Web title'
    webpage['body']=text
    webpage['message']="The following content was retrieved from %s"%url
    return webpage