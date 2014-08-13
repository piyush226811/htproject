# Create your views here.

# example/simple/views.py

from django.shortcuts import render_to_response
from django.core.context_processors import csrf 
from django.shortcuts import redirect

from django.http import HttpResponse
from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter
from api.models import User, Bookmark, Event

from config import CONFIG

authomatic = Authomatic(CONFIG, 'a super secret random string')


def bookmark_set(request, fbid, eventid):
    
    response = HttpResponse();
    user = User.objects.get(fbid = fbid);
    event = Event.objects.get(id=eventid);

    if 'fbid' in request.session:
        if request.session['fbid'] == fbid:
            #response.write("logged in");
            pass;
        else:
            #response.write("wrong user"); 
            return 1;
    else:
        #response.write("no login");
        return 1;


    if Bookmark.objects.filter(user = user.fbid, event = eventid).count() > 0:
        #response.write("Bookmark already exists")
        return 1;
    
    bookmark = Bookmark.objects.create(user=user,event=event);
    bookmark.event_name = event.title
    bookmark.date = event.event_date
    bookmark.time = event.event_time
    bookmark.email = user.email
    bookmark.sent = 0

    #bookmark.user = user.fbid;
    #bookmark.event = eventid;
    bookmark.save()
     
    #response.write("bookmark saved for user = "+fbid+" event = "+eventid);

    return response;

def bookmark_unset(request, fbid, eventid):
    
    response = HttpResponse();
    user = User.objects.get(fbid = fbid);
    event = Event.objects.get(id=eventid);

    if 'fbid' in request.session:
        if request.session['fbid'] == fbid:
            #response.write("logged in");
            pass;
        else:
            #response.write("wrong user"); 
            return 1;
    else:
        #response.write("no login");
        return 1;
    
    bookmark = Bookmark.objects.get(user=fbid,event=eventid);
    bookmark.delete()
    #response.write("Bookmark already exists")
    return response;

def bookmark_get(request,fbid, eventid):
    
    user = User.objects.get(fbid = fbid);
    fbid=int(fbid)
    
    #response = HttpResponse();

    if 'fbid' in request.session:
        #response.write("logged in<br>");
        #response.write(fbid);
        pass;
    else:
        #response.write("no login");
        return 1;

    if fbid > 0:
        if Bookmark.objects.filter(user = user.id, event = eventid).count() > 0:
            #response.write("check");
            #response.write(user);
            bookmark = Bookmark.objects.get(user = user.id, event = eventid);
            
            #response.write(bookmark);
            #response.write("<br>bookmark id = ");
            #response.write(bookmark.id);    
        else:
            #response.write("bookmark doesn't exist");
            pass;
    
       
    elif fbid == 0:
        if Bookmarks.objects.filter(event = eventid).count() > 0:
            
            bookmark_obj = Bookmark.objects.all().filter(event = eventid);
        
            for bookmark in bookmark_obj:
                pass
                #response.write(bookmark);
                #response.write("<br>bookmark id = ");
                #response.write(bookmark.id);

        else:
            #response.write("bookmark events don't exist");
            pass;
    
        
    return 1;


def friends_on_event(fbid, eventid):

    response = HttpResponse();


   
    user_obj = User.objects.get(fbid = fbid);

    friendlist = user_obj.friendlist.split(",");
    #friend_user = User.objects.all().filter(fbid = friendlist)

    bookmark_obj = Bookmark.objects.all().filter(user__in = friendlist, event = eventid);

    return bookmark_obj;
   

    for bookmark in bookmark_obj:
        response.write("<img src='http://graph.facebook.com/"+str(bookmark.user.fbid)+"/picture?type=small'>");
       
    #response.write(friendlist);
    #return response;
    

def event_page(request, eventid):

    #response = HttpResponse();

    event_obj = Event.objects.get(id = eventid)
    bookmark_obj = ()
    login_check = False
    bookmark_check = False

    c = {}
    c.update(csrf(request))

    if 'fbid' in request.session:
        login_check = True
        user = User.objects.get(fbid = request.session['fbid'])
        fbid=int(request.session['fbid'])
        
        #response.write("<br>logged in<br>");
        if Bookmark.objects.filter(user = user.fbid, event = eventid).count() > 0:
            bookmark_obj = friends_on_event(request.session['fbid'],eventid)
            bookmark_check = True
        else:
            bookmark_check = False

        #data['bookmark_obj']=bookmark_obj
        

        #for bookmark in bookmark_obj:
            #response.write("Test+");
            #response.write("<img src='http://graph.facebook.com/"+bookmark.user.fbid+"/picture?type=small'>");

    
        
    return render_to_response('views/detail.html', {'bookmarks': bookmark_obj, 'event':event_obj, 'login':login_check, 'bookmark_check':bookmark_check, 'request': request, 'c':c});







def home(request):
    # Create links and OpenID form to the Login handler.
    event = Event.objects.all()
    login_check = False

    if 'fbid' in request.session:
        login_check = True

    return render_to_response('index.html', {'events': event, 'login':login_check, 'request': request})

def login(request, provider_name):
    # We we need the response object for the adapter.


    name = 'flag'
    email = 'flag'
    fbid = 'flag'

    response = HttpResponse()
    
    if 'fbid' in request.session:
        response.write(request.session['fbid']+' logged in as '+request.session['name']);

    # Start the login procedure.
    result = authomatic.login(DjangoAdapter(request, response), provider_name)
    
    frend_ids = '';

    # If there is no result, the login procedure is still pending.
    # Don't write anything to the response if there is no result!
    if result:
        # If there is result, the login procedure is over and we can write to response.
        response.write('<a href="..">Home</a>')
        
        if result.error:
            # Login procedure finished with an error.
            response.write('<h2>Damn that error: {0}</h2>'.format(result.error.message))
        
        elif result.user:
            # Hooray, we have the user!
            
            # OAuth 2.0 and OAuth 1.0a provide only limited user data on login,
            # We need to update the user to get more info.

           
            if not (result.user.name and result.user.id):
                result.user.update()
            
            # Welcome the user.

            name = result.user.name
            fbid = result.user.id
            email = result.user.email

            response.write(u'<h1>Hi {0}</h1>'.format(result.user.name))
            response.write(u'<h2>Your id is: {0}</h2>'.format(result.user.id))
            response.write(u'<h2>Your email is: {0}</h2>'.format(result.user.picture))
            
            response.write(dir(result.user))


            request.session['fbid'] = fbid
            request.session['name'] = name
            #request.session['']
            # Seems like we're done, but there's more we can do...
            
            # If there are credentials (only by AuthorizationProvider),
            # we can _access user's protected resources.
            if result.user.credentials:
                
                # Each provider has it's specific API.
                if result.provider.name == 'fb':
                    response.write('Your are logged in with Facebook.<br />')
                    
                    # frens
                    url = 'https://graph.facebook.com/v2.0/me/friends'
                    url = url.format(result.user.id)
                    
                    
                    # Access user's protected resource.
                    access_response = result.provider.access(url)
                    
                    response.write(url);
                    #return response

                    if access_response.status == 200:
                        # Parse response.
                        #statuses = access_response.data.get('feed').get('data')
                        error = access_response.data.get('error')
                        frens = access_response.data.get('data')
                        
                        #response.write(access_response.data);
                        #return response

                        if error:
                            response.write(u'Damn that error: {0}!'.format(error))
                            
                        elif frens:
                            
                            frend_ids = '';

                            for message in frens:
                                
                                text = message.get('name')
                                frend_fbid = message.get('id')
                                
                                frend_ids += frend_fbid+',';


                                #response.write(u'<h3>{0}</h3>'.format(text))
                                #response.write(u'Posted on: {0}'.format(date))
                               
                    else:
                        response.write('Damn that unknown error!<br />')
                        #response.write(u'Status: {0}'.format(response.status))
    
    #response.write(frend_ids)

   
    response.write(result);

    #return response;
    if name == 'flag' or fbid == 'flag' or name == '' or fbid == '':
        return response;

    if User.objects.filter(fbid=fbid).count() > 0:
        user = User.objects.get(fbid=fbid);
    else: user = User.objects.create()
    
        #response.write("Check345564567");
         #return response;
    
    
    user.fbid = fbid
    user.friendlist = frend_ids
    user.name = name
    
    user.email = email

    user.save();
    #response.write("Check34556");
    #return response
    return redirect(home)

def logout(request,eventid):

    request.session.flush()
    if eventid == 'home':
        return redirect(home)
    else:
        return redirect('/events/'+eventid)