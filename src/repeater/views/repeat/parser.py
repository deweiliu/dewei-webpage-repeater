from bs4 import BeautifulSoup
from urllib import parse


class Parser():
    def __init__(self, response):
        super().__init__()

        soup = BeautifulSoup(response.text, "html.parser")  # Parse HTML Page
        try:
            self.title = soup.find('title').text
        except:
            self.title='N/A'

        body = soup.find('body')
        for a in soup.findAll('a'):
            try:
                link = a['href']
                new_link = self.change_link(response.url, link)
                a['href'] = new_link
            except:
                pass

        self.body = body

    def change_link(self, url, link):

        if(link.startswith('/')):
            # change the relative link to obsulate link of the origin domain
            p = parse.urlparse(url)
            link = p.scheme+"://"+p.netloc+link
        
        if(link.startswith('http')):
            # if it is a http or https link, it will be directed to this application
            
            link = parse.quote(link, safe='') # URL encoding
            link = "/?url="+link
            print(link)
        return link

    def get_body(self):
        return self.body

    def get_title(self):
        return self.title
