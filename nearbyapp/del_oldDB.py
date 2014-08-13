#!/usr/bin/env python

import sys,os

sys.path.append(os.path.join(os.path.dirname(__file__), 'nearbyapp'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nearbyapp.settings")

from django.conf import settings
from api.models import *
from datetime import date
from django.db import connection, transaction

def delete_old_sessions():
    
    for old in Event.objects.filter(event_date__lte = date.today()):
        new = Exp_Event(eventid = old.eventid, title = old.title, description = old.description, organizer = old.organizer, venue = old.venue, category = old.category, image = old.image, latitude = old.latitude, longitude = old.longitude, city = old.city, api_vendor = old.api_vendor, event_url = old.event_url, event_date = old.event_date, event_time = old.event_time)
        new.save()
	old.delete()
    #Events.objects.filter(event_date__lte = date.today()).delete()


if __name__ == '__main__':
    delete_old_sessions()
