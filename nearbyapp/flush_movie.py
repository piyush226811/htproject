#!/usr/bin/env python

import sys,os

sys.path.append(os.path.join(os.path.dirname(__file__), 'nearbyapp'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nearbyapp.settings")

from django.conf import settings
from api.models import *
#from django.db import connection, transaction

def delete_old_movies():

    Movie.objects.all().delete()
    #old.delete()
    #Events.objects.filter(event_date__lte = date.today()).delete()


if __name__ == '__main__':
    delete_old_movies()
