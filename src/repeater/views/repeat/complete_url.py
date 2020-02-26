from urllib import parse
def complete(url):
    if not (url.startswith('http')):
        url='http://'+url
    p = parse.urlparse(url)
    url=p.geturl()
    
    return url