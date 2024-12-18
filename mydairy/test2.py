from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Kolkata')
now = datetime.now(tz)
print("Current Time:", now)
