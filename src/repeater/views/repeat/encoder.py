from urllib import parse
def encode(url):
    encoded_url=parse.quote(url, safe='')
    return encoded_url