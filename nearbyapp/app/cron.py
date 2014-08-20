from django_cron import CronJobBase, Schedule
from api.models import Bookmark
from datetime import date,datetime, timedelta
from tasks import email_24, email_1

class MyCronJob(CronJobBase):

    RUN_EVERY_MINS = 0.1;

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'events.hour_notif'    # a unique code

    def do(self):

        #time_threshold = datetime.now().time() + timedelta(hours=24).time();

        time_threshold = datetime.now() + timedelta(hours=24);


        bookmark_obj = Bookmark.objects.filter(date__lt=time_threshold.date(),sent=0);

        sent_list_h =[];

        m = {}
        d = {}

        for bookmark in bookmark_obj:


            if bookmark.event in d:
                d[bookmark.event]['mail_list']=d[bookmark.event]['mail_list']+ bookmark.email + ",";
                #print bookmark.event;
                #print d[bookmark.event]['mail_list']
            else:
                d[bookmark.event]= {'mail_list':bookmark.email+", "};
                d[bookmark.event]['name'] = bookmark.event_name;
                d[bookmark.event]['time'] = bookmark.time;
                d[bookmark.event]['date'] = bookmark.date;

                #print d[bookmark.event]['name']


            time_threshold_h = datetime.now() + timedelta(minutes=120)

            time_threshold_h = time_threshold_h.time();

            if(bookmark.time < time_threshold_h):

                sent_list_h.append(bookmark.id);

                if bookmark.event in m:
                    m[bookmark.event]['mail_list'] = m[bookmark.event]['mail_list'] + bookmark.email + ", ";
                else:
                    m[bookmark.event] = {'mail_list':bookmark.email+", "};
                    m[bookmark.event]['name'] = bookmark.event_name;
                    m[bookmark.event]['time'] = bookmark.time.hour - datetime.now().hour;
                    m[bookmark.event]['date'] = bookmark.date;


        for key in d:
            delay = 3;
            print d[key];
            email_24.apply_async((d[key],), countdown = delay)


        for key in m:
            delay = 2;
            email_1.apply_async((m[key],), countdown = delay)

        #Bookmark.objects.filter(sent=0).update(sent=1)
        #Bookmark.objects.filter(id__in=sent_list_h).update(sent=2)
        print(sent_list_h)

