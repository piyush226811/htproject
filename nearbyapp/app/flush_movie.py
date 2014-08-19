#!/usr/bin/env python

#import sys,os

#sys.path.append(os.path.join(os.path.dirname(__file__), 'nearbyapp'))
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nearbyapp.settings")

from django_cron import CronJobBase, Schedule

#from django.conf import settings
from api.models import *
#from django.db import connection, transaction

class FlushMovie(CronJobBase):

    RUN_EVERY_HOUR = 0.2;

    schedule = Schedule(run_every_mins=RUN_EVERY_HOUR)
    code = 'eventful.hour_notif'    # a unique code

    def do(self):
        Movie.objects.all().delete()
