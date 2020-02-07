def invalid(url):
    response=dict()
    response['url_message']="The URL is not valid, please check it again.\n%s"%url
    return response