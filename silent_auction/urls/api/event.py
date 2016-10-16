# -*- coding: utf-8 -*-
from django.conf.urls import url
from silent_auction.views.api import event


urlpatterns = [
    url(
        regex=r'^$',
        view=event.list_events,
        name='list_events',
    ),
    url(
        regex=r'^create/$',
        view=event.create_event,
        name='create_event',
    ),
    url(
        regex=r'^update/(?P<uuid>[-\w]+)/$',
        view=event.update_event,
        name='update_event',
    ),
    url(
        regex=r'^(?P<uuid>[-\w]+)/$',
        view=event.retrieve_event,
        name='retrieve_event',
    ),
]