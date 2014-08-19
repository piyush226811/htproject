from django.db import models

# Create your models here.

class Event (models.Model):
    eventid = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True, null=True)
    organizer = models.CharField(max_length=150, blank=True, null=True)
    venue = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    latitude = models.CharField(max_length=30, blank=True, null=True)
    longitude = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    api_vendor = models.CharField(max_length=30, blank=True)
    event_url = models.URLField(blank=True)
    event_date = models.DateField(blank=True, null=True)
    event_time = models.TimeField(blank=True, null=True)

    def __unicode__ (self):
        return str(self.eventid)

class User (models.Model):

    fbid = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    friendlist = models.TextField(blank=True, null=True)

    def __unicode__ (self):
        return str(self.name)

class Bookmark (models.Model):

    user = models.ForeignKey(User, to_field='fbid', related_name='bookmarks')
    event = models.ForeignKey(Event, related_name='bookmarks')
    event_name = models.CharField(max_length=100, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    email = models.CharField(max_length=45, null=True)
    sent = models.IntegerField(max_length=11, null=True)

    def __unicode__ (self):
        return str(self.user+","+self.event);

class Exp_Event (models.Model):
    eventid = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True, null=True)
    organizer = models.CharField(max_length=255, blank=True, null=True)
    venue = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    latitude = models.CharField(max_length=30, blank=True, null=True)
    longitude = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    api_vendor = models.CharField(max_length=30, blank=True)
    event_url = models.URLField(blank=True)
    event_date = models.DateField(blank=True, null=True)
    event_time = models.TimeField(blank=True, null=True)

    def __unicode__ (self):
        return str(self.eventid)

class Movie (models.Model):
    title = models.CharField(max_length=255, blank=True)
    theater = models.CharField(max_length=150, blank=True, null=True)
    venue = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    timing = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__ (self):
        return str(self.theater)

class City (models.Model):
    city_name = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__ (self):
        return str(self.city_name)

class Movie_bookmark (models.Model):

    user = models.ForeignKey(User, to_field='fbid', related_name='movie_bookmarks')
    theater = models.CharField(max_length=45, unique = True)
    address = models.CharField(max_length=45, null=True)
    city = models.CharField(max_length=45, null=True)

    def __unicode__ (self):
        return str(self.user+","+self.theater);
