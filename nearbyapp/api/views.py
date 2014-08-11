# Create your views here.

from rest_framework import generics, permissions

from api.serializers import EventSerializer, UserSerializer, BookmarkSerializer
from api.models import Event, User, Bookmark


class EventList(generics.ListAPIView):
    model = Event
    serializer_class = EventSerializer
    filter_fields = ('title')
    permission_classes = [
        permissions.AllowAny
    ]


class EventDetail(generics.RetrieveAPIView):
    model = Event
    serializer_class = EventSerializer
    lookup_field = 'pk'


class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
    lookup_field = 'fbid'


class UserBookmarkList(generics.ListAPIView):
    model = Bookmark
    serializer_class = BookmarkSerializer
    
    def get_queryset(self):
        queryset = super(UserBookmarkList, self).get_queryset()
        return queryset.filter(user__fbid=self.kwargs.get('fbid'))

class EventBookmarkList(generics.ListAPIView):
    model = Bookmark
    serializer_class = BookmarkSerializer
    
    def get_queryset(self):
        queryset = super(EventBookmarkList, self).get_queryset()
        return queryset.filter(event__pk=self.kwargs.get('pk'))


class BookmarkList(generics.ListCreateAPIView):
    model = Bookmark
    serializer_class = BookmarkSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class BookmarkDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Bookmark
    serializer_class = BookmarkSerializer
    permission_classes = [
        permissions.AllowAny
    ]
