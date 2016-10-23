# -*- coding: utf-8 -*-
from django.conf.urls import url
from silent_auction.views.api import eventadmin


urlpatterns = [
    url(
        regex=r'^$',
        view=eventadmin.list_eventadmins,
        name='list_eventadmins',
    ),
    url(
        regex=r'^create/$',
        view=eventadmin.create_eventadmin,
        name='create_eventadmin',
    ),
    url(
        regex=r'^(?P<uuid>[-\w]+)/$',
        view=eventadmin.retrieve_eventadmin,
        name='retrieve_eventadmin',
    ),
    url(
        regex=r'^(?P<uuid>[-\w]+)/update/$',
        view=eventadmin.update_eventadmin,
        name='update_eventadmin',
    ),
    url(
        regex=r'^(?P<uuid>[-\w]+)/delete/$',
        view=eventadmin.delete_eventadmin,
        name='delete_eventadmin',
    ),
]