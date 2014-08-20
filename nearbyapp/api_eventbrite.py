#!/usr/bin/python
import sys,os

sys.path.append(os.path.join(os.path.dirname(__file__), 'nearbyapp'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nearbyapp.settings")
from django.conf import settings

from api.models import *
import eventbrite
import pdb
#to strip the html tag in desc
def remove_html_markup(s):
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
app_key='7D2FFPVTEHALDHKIQB'
api = eventbrite.API(app_key)

events = api.call('/event_search', city='Delhi')

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
		event.description = (remove_html_markup(e['event']['description'])).encode('unicode_escape')
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


