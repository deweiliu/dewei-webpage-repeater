from urllib import parse
def decode(encoded_url):
    decoded_url=parse.unquote(encoded_url)
    return decoded_url