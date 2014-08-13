# nearbyapp/app/urls.py

from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView


class PartialGroupView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(PartialGroupView, self).get_context_data(**kwargs)
        # update the context
        return context

partial_patterns = patterns('',
    url(r'^home.html$', PartialGroupView.as_view(template_name='views/home.html')),
    url(r'^detail.html$', PartialGroupView.as_view(template_name='views/detail.html')),
    # ... more partials ...,
)

sqs = SearchQuerySet().facet('category').facet('event_date')

urlpatterns = patterns('',
    url(r'^$', 'app.views.home'),
    url(r'^login/(\w*)', 'app.views.login', name='login'),
    url(r'^logout/(?P<eventid>\w+)', 'app.views.logout', name='logout'),
    #url(r'^$', TemplateView.as_view(template_name='index.html')),
    #url(r'^views/', include(partial_patterns, namespace='partials')),
    #url(r'^events/(\w*)', 'app.views.detail'),
    #url(r'^views/post.html', 'myproject.views.post_view'),
    url(r'^bookmarks/set/(?P<fbid>\w+)/(?P<eventid>\w+)/', 'app.views.bookmark_set', name='set_bookmark'),
    url(r'^bookmarks/unset/(?P<fbid>\w+)/(?P<eventid>\w+)/', 'app.views.bookmark_unset', name='unset_bookmark'), 
    url(r'^bookmarks/get/(?P<fbid>\w+)/(?P<eventid>\w+)', 'app.views.bookmark_get'), 
    url(r'^friends/(?P<fbid>\w+)/(?P<eventid>\w+)', 'app.views.friends_on_event'),
    url(r'^events/(?P<eventid>\w+)', 'app.views.event_page'),
    (r'^search/', include('haystack.urls')),
)