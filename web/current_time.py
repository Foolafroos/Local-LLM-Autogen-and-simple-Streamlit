# filename: current_time.py
import datetime
from schedule import *
import os

def scheduled_task():
    print("Scheduled Task Executed!")
    
    # Removing the task from scheduler to avoid repeating it
    remove_job(rounded_schedule(timestamp=datetime.timedelta(hours=9), function=scheduled_task, days=weekdays(), minutes=0)))
    
    # Exit the program
    os._exit(1)

run_pending()
register(scheduled_task)

# This line is added to run the scheduler in a background thread
daemon = scheduler(time())

while True:
    pass