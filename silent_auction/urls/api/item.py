# -*- coding: utf-8 -*-
from django.conf.urls import url
from silent_auction.views.api import item


urlpatterns = [
    url(
        regex=r'^$',
        view=item.list_items,
        name='list_items',
    ),
    url(
        regex=r'^create/$',
        view=item.create_item,
        name='create_item',
    ),
    url(
        regex=r'^update/(?P<uuid>[-\w]+)/$',
        view=item.update_item,
        name='update_item',
    ),
    url(
        regex=r'^(?P<uuid>[-\w]+)/$',
        view=item.retrieve_item,
        name='retrieve_item',
    ),
]