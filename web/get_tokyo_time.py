# filename: get_tokyo_time.py
import pytz
from datetime import datetime

def get_tokyo_time():
    # Load the Japan time zone
    japan = pytz.timezone('Asia/Tokyo')

    # Get the current date and time in UTC
    utc_now = datetime.utcnow()

    # Convert the UTC time to Tokyo time (JST)
    jst_now = utc_now.replace(tzinfo=pytz.utc).astimezone(japan)

    return jst_now.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    print("Current time in Tokyo:", get_tokyo_time())