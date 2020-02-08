
import requests
import time

class Request():
    def __init__(self,url):
        super().__init__()
        self.valid=False
        try:
            self.response=requests.get(url)
            self.valid=True
        except:
            print("URL not valid %s"%url)
        self.time=(time.strftime("GMT %d %b %Y, %H:%M:%S",time.gmtime()))
        
    def is_valid(self):
        return self.valid
    def get_response(self):
        return self.response

    def get_time(self):
        return self.time


