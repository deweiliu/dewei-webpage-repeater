
import requests
from repeater.views import get_time


class Request():
    def __init__(self, url):
        super().__init__()
        self.valid = False

        start = float(get_time.value())
        try:
            self.response = requests.get(url)
            self.valid = True
        except:
            print("URL not valid %s" % url)

        finish = float(get_time.value())
        self.time_stamp = get_time.string(finish)

        if(self.valid):
            self.response_time = "%sms" % ((finish-start)*1000)

            status_code = self.response.status_code
            status_description = Request.code2text(status_code)
            self.status = "%s. Status Code %s" % (
                status_description, status_code)
        else:
            self.status = "Error. No response from the requested server."
            self.response_time = "N/A"

    def is_valid(self):
        return self.valid

    def get_response(self):
        return self.response

    def get_time(self):
        return self.time_stamp

    @staticmethod
    def code2text(status_code):
        description = requests.status_codes._codes[status_code][0]
        return str(description).upper()

    def get_status(self):
        return self.status

    def get_response_time(self):
        return self.response_time
