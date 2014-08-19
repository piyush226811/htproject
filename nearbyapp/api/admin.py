from django.contrib import admin
from api.models import Event,User,Exp_Event, Movie, City

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "eventid", "title", "description", "organizer", "venue", "category", "image", "latitude", "longitude", "city", "api_vendor", "event_url", "event_date", "event_time")

class Exp_EventAdmin(admin.ModelAdmin):
    list_display = ("id", "eventid", "title", "description", "organizer", "venue", "category", "image", "latitude", "longitude", "city", "api_vendor", "event_url", "event_date", "event_time")

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "fbid", "name", "email", "friendlist")

class MovieAdmin(admin.ModelAdmin):
    list_display = ("theater", "title", "venue", "category","timing", "date","city")

class CityAdmin(admin.ModelAdmin):
    list_display = ("city_name",)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Exp_Event, EventAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(City, CityAdmin)
