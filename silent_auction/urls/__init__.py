"""Defaults urls for the silent_auction project"""
from django.conf.urls import url
from django.conf.urls import include


urlpatterns = [
    url(r'^events/', include('silent_auction.urls.events')),
    url(r'^locations/', include('silent_auction.urls.locations')),
    url(r'^items/', include('silent_auction.urls.items')),
    url(r'^bids/', include('silent_auction.urls.items')),
    url(r'^', include('silent_auction.urls.capabilities')),
]