import pandas as pd
import datetime as dt
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