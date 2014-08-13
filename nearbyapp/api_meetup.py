#!/usr/bin/python
import sys,os
import time

sys.path.append(os.path.join(os.path.dirname(__file__), 'nearbyapp'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nearbyapp.settings")
from django.conf import settings

from api.models import *
import meetup
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
#############
src= '157853802'
src_id = 'dc946017de5b74d68a832be2dc831d47872ed751'
api = meetup.API(src,src_id)

events = api.call('/2/open_events?status=upcoming&radius=25.0&and_text=False&limited_events=False&desc=False&offset=0&photo-host=public&format=json', lat='28.38',lon='77.03')

for e in events['results']:
	(event, created) = Event.objects.get_or_create(eventid=e['id'])
	if not created: continue

	print 'Processing event: "%s"' % e["name"]

	event.eventid = e['id']
	event.title = e['name']
	event.organizer = e['group']['name']

	if e.get('description'):

		event.description = remove_html_markup(e['description'])
	else:
		event.description = 'None'

	if e.get('venue'):
		event.venue = e['venue']['name'] + e['venue']['address_1']
	else:
		event.venue = 'None'

	event.category = e['group']['who']


	if e.get('venue'):
		event.city = e['venue']['city']
	else:
		event.city = 'None'

	event.latitude = e['group']['group_lat']
	event.longitude = e['group']['group_lon']
	event.api_vendor = 'Meetup'
	event.event_url = e['event_url']
	event.event_date = str(time.strftime('%Y-%m-%d',  time.gmtime(e['time']/1000)))
	event.event_time = str(time.strftime('%H:%M:%S',  time.gmtime(e['time']/1000)))

	event.save()




