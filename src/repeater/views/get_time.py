import time

def value():
    return time.time()

def string(time_value=time.gmtime()):
    time_value=float(time_value)
    return time.strftime("GMT %d %b %Y, %H:%M:%S", time_value)
