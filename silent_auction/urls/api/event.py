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
        regex=r'^(?P<event_uuid>[-\w]+)/$',
        view=event.retrieve_event,
        name='retrieve_event',
    ),
    url(
        regex=r'^(?P<event_uuid>[-\w]+)/update/$',
        view=event.update_event,
        name='update_event',
    ),
    url(
        regex=r'^(?P<event_uuid>[-\w]+)/delete/$',
        view=event.delete_event,
        name='delete_event',
    ),
    url(
        regex=r'^(?P<event_uuid>[-\w]+)/items/$',
        view=event.list_event_items,
        name='list_event_items',
    ),
]