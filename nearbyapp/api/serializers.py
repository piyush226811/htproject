from rest_framework import serializers

from api.models import Event, User, Bookmark, Movie


class EventSerializer(serializers.ModelSerializer):
    bookmarks = serializers.HyperlinkedIdentityField('bookmarks', view_name='events-bookmark', lookup_field='pk')

    class Meta:
        model = Event
        fields = ('id', 'eventid', 'title', 'description', 'organizer', 'venue', 'category', 'image', 'latitude', 'longitude', 'city', 'api_vendor', 'event_url', 'event_date', 'event_time','bookmarks')


class UserSerializer(serializers.ModelSerializer):
    bookmarks = serializers.HyperlinkedIdentityField('bookmarks', view_name='users-bookmark', lookup_field='fbid')

    class Meta:
        model = User
        fields = ('id', 'fbid', 'name', 'email', 'friendlist','bookmarks')


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id', 'user','event')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','theater', 'title', 'category', 'venue', 'city', 'timing', 'date')
