from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from jobs.jobs import API_SCHEDULAR


def start():
    print("At start")
    scheduler = BackgroundScheduler()
    task = API_SCHEDULAR()
    scheduler.add_job(task.run, "interval", minutes=5)
    scheduler.start()
    print("Here")
