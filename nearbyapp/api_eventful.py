#!/usr/bin/python
import sys,os

sys.path.append(os.path.join(os.path.dirname(__file__), 'nearbyapp'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nearbyapp.settings")
from django.conf import settings

from api.models import *
import eventful
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
api = eventful.API('mm576kLMq5X9DRgt')
# api.login('username', 'password')
events = api.call('/events/search', l='Gurgaon')
events = api.call('/events/search', l='Gurgaon',page_size=(events['total_items']))
#print events
for e in events['events']['event']:
	(event, created) = Event.objects.get_or_create(eventid=e['id'])
	if not created: continue

	print 'Processing event: "%s"' % e['title']

	event.eventid = e['id']
	event.title = e['title']
	event.description = remove_html_markup(e['description'])
	event.organizer = e['owner']
	if e.get('venue_address'):
		event.venue = e['venue_address']
	else:
		event.venue = 'None'

	event.category = 'None'

	if e.get('image'):
		event.image = e['image']['url']
	else:
		event.image = 'None'

	event.latitude = e['latitude']
	event.longitude = e['longitude']
	event.city = e['city_name']
	event.api_vendor = 'Eventful'
	event.event_url = e['url']

	datetime = e['start_time'].split(' ')
	event.event_date = datetime[0]
	event.event_time = datetime[1]

	event.save()


