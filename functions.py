import pandas as pd
from datetime import datetime, date
import re

def convertTime(time):
    if time is None or pd.isnull(time):
        return None

    form = re.match(r'(\d{1,2}):(\d{2})(\s*[AP]M)', time)
    if form:
        try:
            time = pd.to_datetime(time, format='%I:%M%p')
        except ValueError:
            time = pd.to_datetime(time, format='%I:%M %p')

    else:
        try:
            time = pd.to_datetime(time, format='%Y-%m-%d %I:%M%p')
        except ValueError:
            time = pd.to_datetime(time, format='%Y-%m-%d %I:%M %p')
    
    # Return time as a datetime object
    time = time.time()
    return time

def timeDifference(time1, time2):
    res = datetime.combine(date.min, time2) - datetime.combine(date.min, time1)
    res = int(res.total_seconds() / 60)
    return res