from bs4 import BeautifulSoup
import sys
import urllib2
import pdb
import time
import sys,os
import datetime
week_days = {    1:'monday',    2:'tuesday', 	3:'wednesday',    4:'thursday',    5:'friday',    6:'saturday',    7:'sunday'
}

sys.path.append(os.path.join(os.path.dirname(__file__), 'nearbyapp'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nearbyapp.settings")
from django.conf import settings

from django_cron import CronJobBase, Schedule
from api.models import *
class MoviesApi(CronJobBase):

	RUN_EVERY_HOUR = 1;

	schedule = Schedule(run_every_mins=RUN_EVERY_HOUR)
	code = 'movies.hour_notif'    # a unique code
	def do(self):
		cityname=City.objects.all()
		print cityname
		for city in cityname:
			print city.city_name
			location=city.city_name
			if (location!="None"):
				day=int(time.strftime("%w"))
				num=0
				t=0
				cur_date=datetime.date.today()
				while(1):
					print "Movies in "+location+" on "+week_days[day]+" are "
					while(1):
						url = "http://www.google.com/movies?near="+location+"&date="+str(t)+"&start="+str(num)
						content = urllib2.urlopen(url).read()
						soup = BeautifulSoup(content)
					
						if(soup.find("div",class_="theater")):
							pass;
						else:		
							break
						
						for link in soup.find_all("div",class_="theater"):
							th_name=(link.find("h2",class_="name")).text			
							th_venue=((link.find("div",class_="info")).text).replace("#" , "")
							print (link.find("h2",class_="name")).text ## theater name
							print ((link.find("div",class_="info")).text).replace("#" , "") ## theater venue

							for movies in link.find_all("div",class_="movie"):
								m = Movie.objects.create()
								m.theater = th_name
								m.venue = th_venue
								m.title = (movies.find("div", class_="name")).text
								cat=((movies.find("span", class_="info")).text).replace("- Trailer" , "")			
								m.category = (cat.encode('ascii','ignore'))
								tm = movies.find(class_="times").text	
								m.timing=str(tm.encode('ascii','ignore')) 			
								m.city=location
								m.date= cur_date.strftime("%Y-%m-%d")
								m.save()
								print (movies.find("div", class_="name")).text ## movie name
								print ((movies.find("span", class_="info")).text).replace("- Trailer" , "") ## movie type
								print tm;
							print "**********************************************"	
						num=num+10
					
					num=0
					day=day+1
					cur_date += datetime.timedelta(days=1)
					t=t+1
					url = "http://www.google.com/movies?near="+location+"&date="+str((t))
					content = urllib2.urlopen(url).read()
					soup = BeautifulSoup(content)
					if(soup.find("div",class_="theater")):
						pass;
					else:		
						break
				
