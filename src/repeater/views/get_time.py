import time
from datetime import datetime


def value():
    return str(time.time())

def string(time_value=time.gmtime()):
    time_value = int(time_value)
    time_object = datetime.fromtimestamp(time_value)
    return time_object.strftime("%A %d %B %Y %H:%M:%S GMT")
