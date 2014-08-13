from django.conf.urls import patterns, url, include

from api.views import *

user_urls = patterns('',
    url(r'^/(?P<fbid>[0-9a-zA-Z_-]+)/bookmarks$', UserBookmarkList.as_view(), name='users-bookmark'),
    url(r'^/(?P<fbid>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^$', UserList.as_view(), name='user-list')
)

event_urls = patterns('',
    url(r'^/(?P<pk>\d+)/bookmarks$', EventBookmarkList.as_view(), name='events-bookmark'),
    url(r'^/(?P<pk>\d+)$', EventDetail.as_view(), name='event-detail'),
    url(r'^$', EventList.as_view(), name='event-list')
)

bookmark_urls = patterns('',
    url(r'^/(?P<pk>\d+)$', BookmarkDetail.as_view(), name='bookmark-detail'),
    url(r'^$', BookmarkList.as_view(), name='bookmark-list')
)

urlpatterns = patterns('',
    url(r'^users', include(user_urls)),
    url(r'^events', include(event_urls)),
    url(r'^bookmarks', include(bookmark_urls)),
)