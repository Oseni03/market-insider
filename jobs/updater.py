from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from jobs.jobs import API_SCHEDULAR#, Newsletter


def start():
    print("Starting CronJob")
    scheduler = BackgroundScheduler()
    task = API_SCHEDULAR()
    scheduler.add_job(task.run, "interval", minutes=180)
    # newsletter = Newsletter()
    # scheduler.add_job(newsletter.main, "interval", minutes=360)
    scheduler.start()
    print("Ending CronJob")
