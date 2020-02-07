import requests
import html2text
def parse_webpage(url):
    webpage=dict()


    response=requests.get(url)
    body=response.text
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    text = converter.handle(body)

    webpage['title']='Web title'
    webpage['body']=text
    return webpage