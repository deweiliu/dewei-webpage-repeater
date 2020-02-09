import time

def value():
    return time.time()

def string(time_value=time.gmtime()):
    time_value=float(time_value)
    return time.strftime("%A %d %B %Y %H:%M:%S GMT", time_value)
