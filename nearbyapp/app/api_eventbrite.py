#!/usr/bin/python
#import sys,os

#sys.path.append(os.path.join(os.path.dirname(__file__), 'nearbyapp'))
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nearbyapp.settings")
#from django.conf import settings

from django_cron import CronJobBase, Schedule

from api.models import *
import eventbrite
import pdb

class EventbriteApi(CronJobBase):

    RUN_EVERY_HOUR = 0.2;

    schedule = Schedule(run_every_mins=RUN_EVERY_HOUR)
    code = 'eventbrite.hour_notif'    # a unique code
    def remove_html_markup(self,s):
            tag = False
            quote = False
            out = ""

            for c in s:
                    if c == '<' and not quote:
                        tag = True
                    elif c == '>' and not quote:
                        tag = False
                    elif (c == '"' or c == "'") and tag:
                        quote = not quote
                    elif not tag:
                        out = out + c

            return out

    
    def do(self):
        cityname=City.objects.all()
        #print cityname
        for city in cityname:
            print city.city_name
            location=city.city_name
            if (location!="None"):
        #to strip the html tag in desc
        
                app_key='7D2FFPVTEHALDHKIQB'
                api = eventbrite.API(app_key)

                events = api.call('/event_search', city= location)

                for e in events['events']:
                	#pdb.set_trace()
                	if(e.get("summary")):
                		print "ok"
                	else:
                		#print e["event"]["locale"]
                		(event, created) = Event.objects.get_or_create(eventid=e["event"]['id'])
                		if not created: continue

                		print 'Processing event: "%s"' % e['event']['title']

                		event.eventid = e["event"]['id']
                		event.title = e['event']['title']
                		event.description = self.remove_html_markup(e['event']['description'])
                		event.organizer = e["event"]["organizer"]["name"]
                		event.venue = e["event"]["venue"]['name'] + e["event"]["venue"]['address_2'] + e["event"]["venue"]['address'] + e["event"]["venue"]['city'] +e["event"]["venue"]['region'] + e["event"]["venue"]['postal_code']
                		if e["event"].get('category'):
                			event.category = e["event"]["category"]
                		else:
                			event.category = 'None'
                		if e["event"].get('logo'):
                			event.image = e["event"]['logo']
                		else:
                			event.image = 'None'

                		event.latitude = e["event"]["venue"]['latitude']
                		event.longitude = e["event"]["venue"]['longitude']
                		event.city = e["event"]["venue"]['city']
                		event.api_vendor = 'Eventbrite'
                		event.event_url = e["event"]["organizer"]["url"]

                		datetime = e["event"]['start_date'].split(' ')
                		event.event_date = datetime[0]
                		event.event_time = datetime[1]

                		event.save()


