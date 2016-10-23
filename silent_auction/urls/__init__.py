"""Defaults urls for the silent_auction project"""
from django.conf.urls import url
from django.conf.urls import include


urlpatterns = [
    url(r'^api/', include('silent_auction.urls.api', namespace='api')),
]