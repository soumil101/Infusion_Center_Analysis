import pandas as pd
from datetime import datetime, date
import re

def convertTime(time):
    form = re.match(r'(\d{1,2}):(\d{2})(\s*[AP]M)', time)
    if form:
        try:
            time = date.strptime(time, '%H:%M%p')
        except ValueError:
            time = date.strptime(time, '%H:%M %p')

    else:
        try:
            time = date.strptime(time, '%Y-%m-%d %H:%M%p')
        except ValueError:
            time = date.strptime(time, '%Y-%m-%d %H:%M %p')
    
    # Return time as a datetime object
    return time

def timeDifference(time1, time2):
    res = datetime.combine(date.min, time2) - datetime.combine(date.min, time1)
    res = int(res.total_seconds() / 60)
    return res