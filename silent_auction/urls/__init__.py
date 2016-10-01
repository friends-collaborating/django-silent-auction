"""Defaults urls for the silent_auction project"""
from django.conf.urls import url
from django.conf.urls import include


urlpatterns = [
    url(r'^', include('silent_auction.urls.bids')),
    url(r'^', include('silent_auction.urls.events')),
    url(r'^', include('silent_auction.urls.items')),
    url(r'^', include('silent_auction.urls.locations')),
]