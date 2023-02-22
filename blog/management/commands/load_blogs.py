import os
from django.core.management.base import BaseCommand

from jobs.jobs import feedsCronJob


class Command(BaseCommand):
    help = 'Loads blogs from rss' 
    
    def handle(self, *args, **kwargs):
        feedsCronJob()
        self.stdout.write(self.style.SUCCESS("Blogs loaded successfully!"))
