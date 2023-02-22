from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from jobs.jobs import feedsCronJob, newsletterCronJob


def start():
    print("Starting CronJobs")
    scheduler = BackgroundScheduler()
    scheduler.add_job(newsletterCronJob, "interval", days=1)
    scheduler.add_job(feedsCronJob, "interval", hours=1)
    scheduler.start()
    print("Ending CronJobs")
