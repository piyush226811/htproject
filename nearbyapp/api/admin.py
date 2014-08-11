from django.contrib import admin
from api.models import Event,User,Exp_Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "eventid", "title", "description", "organizer", "venue", "category", "image", "latitude", "longitude", "city", "api_vendor", "event_url", "event_date", "event_time")

class Exp_EventAdmin(admin.ModelAdmin):
    list_display = ("id", "eventid", "title", "description", "organizer", "venue", "category", "image", "latitude", "longitude", "city", "api_vendor", "event_url", "event_date", "event_time")

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "fbid", "name", "email", "friendlist")

admin.site.register(Event, EventAdmin)
admin.site.register(Exp_Event, EventAdmin)
admin.site.register(User, UserAdmin)
