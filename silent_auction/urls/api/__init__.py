from django.conf.urls import url
from django.conf.urls import include


urlpatterns = [
    url(r'^bid/', include('silent_auction.urls.api.bid')),
    url(r'^event/', include('silent_auction.urls.api.event')),
    url(r'^item/', include('silent_auction.urls.api.item')),
]