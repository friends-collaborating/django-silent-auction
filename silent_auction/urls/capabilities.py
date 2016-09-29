"""Urls for the silent_auction capabilities"""
from django.conf.urls import url

from silent_auction.views.capabilities import RsdXml
from silent_auction.views.capabilities import HumansTxt
from silent_auction.views.capabilities import OpenSearchXml
from silent_auction.views.capabilities import WLWManifestXml


urlpatterns = [
    url(
        regex=r'^rsd.xml$',
        view=RsdXml.as_view(),
        name='rsd'
    ),
    url(
        regex=r'^humans.txt$',
        view=HumansTxt.as_view(),
        name='humans'
    ),
    url(
        regex=r'^opensearch.xml$',
        view=OpenSearchXml.as_view(),
        name='opensearch'
    ),
    url(
        regex=r'^wlwmanifest.xml$',
        view=WLWManifestXml.as_view(),
        name='wlwmanifest',
    ),
]
