
import requests
import html2text
import time
class Parser():
    def __init__(self,url):
        super().__init__()
        self.valid=False
        try:
            response=requests.get(url)
            self.time=(time.strftime("%b %d %Y %H:%M:%S"))
            self.valid=True
        except:
            print("URL not valid %s"%url)
            return
        body=response.text
    
        converter = html2text.HTML2Text()
        converter.ignore_links = False
        self.title="Web title"
        self.body = converter.handle(body)

        
    def is_valid(self):
        return self.valid
    def get_title(self):
        return self.title
    def get_body(self):
        return self.body
    def get_time(self):
        return self.time


