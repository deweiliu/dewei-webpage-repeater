
import requests
from repeater.views import get_time  

class Request():
    def __init__(self, url):
        super().__init__()
        self.valid = False
        try:
            self.response = requests.get(url)
            self.valid = True
        except:
            print("URL not valid %s" % url)
        self.time = get_time.string()

        if(self.valid):
            status_code = self.response.status_code
            status_description = Request.code2text(status_code)
            self.status = "%s. Status Code %s" % (status_description,status_code)
        else:
            self.status="Error. No response from the requested server."

    def is_valid(self):
        return self.valid

    def get_response(self):
        return self.response

    def get_time(self):
        return self.time

    @staticmethod
    def code2text(status_code):
        description= requests.status_codes._codes[status_code][0]
        return str(description).upper()

    def get_status(self):
        return self.status
