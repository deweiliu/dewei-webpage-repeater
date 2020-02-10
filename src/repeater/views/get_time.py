import time
from datetime import datetime


def value():
    return str(time.gmtime())


def string(time_value=None):
    if(time_value == None):
        time_value = value()
    time_value = int(float(time_value))
    time_object = datetime.fromtimestamp(time_value)
    return time_object.strftime("%A %d %B %Y %H:%M:%S GMT")
