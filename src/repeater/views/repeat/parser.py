from bs4 import BeautifulSoup

class Parser():
    def __init__(self,response):
        super().__init__()
        soup = BeautifulSoup(response.text, "html.parser") #Parse HTML Page
        self.title=soup.title.string
        self.body = soup.find('body')
        
             

    def get_body(self):
        return self.body
    def get_title(self):
        return self.title
        