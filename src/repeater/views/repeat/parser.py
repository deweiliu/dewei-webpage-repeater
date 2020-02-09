from bs4 import BeautifulSoup
from urllib import parse


class Parser():
    def __init__(self, response):
        super().__init__()
        self.url = response.url

        soup = BeautifulSoup(response.text, "html.parser")  # Parse HTML Page
        try:
            self.title = soup.find('title').text
        except:
            self.title = 'N/A'

        # process <head>
        self.head = soup.find('head')
        self.head = Parser.remove_tag_from_element(
            self.head, ['title', 'link', 'script'])
        self.head = self.change_head(self.head, self.url)
        self.head = Parser.element2text(self.head, 'head')

        # process <body>
        self.body = soup.find('body')
        self.body = Parser.remove_tag_from_element(
            self.body, ['script'])
        self.body = self.change_body(self.body, self.url)
        self.body = Parser.element2text(self.body, 'body')

    def change_body(self, body, url):
        # process <a>
        for a in body.findAll('a'):
            try:
                link = a['href']
                new_link = Parser.change_link(url, link)
                a['href'] = new_link
            except:
                pass
        # process <img>
        for img in body.findAll('img'):
            try:
                link = img['src']
                print(link)
                new_link = Parser.change_link(url, link, link2myself=False)
                print(new_link)
                img['src'] = new_link
            except:
                pass
        return body

    @staticmethod
    def element2text(element, tag):
        text = str(element)
        length = len(tag)
        if(text[0:length+2] == "<%s>" % tag):
            if(text[-(length+3):] == "</%s>" % tag):
                text = text[length+2:-(length+3)]
        return text

    @staticmethod
    def remove_tag_from_element(element, remove_list):
        for each in remove_list:
            tags = element.findAll(each)
            for tag in tags:
                tag.decompose()

        return element

    def change_head(self, head, url):
        links = head.findAll('link')
        for link in links:
            href = link['href']
            new_href = Parser.change_link(url, href, link2myself=False)
            link['href'] = new_href
        return head

    @staticmethod
    def change_link(url, href, link2myself=True):

        if(href.startswith('#')):
            return href

        if ("//" not in href):
            # If this is not an absolute path
            if(not href.startswith('/')):
                href = '/%s' % href  # add /
            p = parse.urlparse(url)
            href = p.scheme+"://"+p.netloc+href

        if(link2myself):
            if(href.startswith('http')):
                # if it is a http or https link, it will be redirected to this application

                href = parse.quote(href, safe='')  # URL encoding
                href = "/?url="+href
        return href

    def get_body(self):
        return self.body

    def get_head(self):
        return self.head

    def get_title(self):
        return self.title
