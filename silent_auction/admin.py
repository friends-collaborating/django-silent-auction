# -*- coding: utf-8 -*-
from django.contrib import admin
from parler.admin import (
    TranslatableAdmin,
    TranslatableStackedInline, )
from silent_auction.forms import BidForm
from silent_auction.models import Bid
from silent_auction.models import Event
from silent_auction.models import EventAdmin
from silent_auction.models import Item
from silent_auction.models import ItemImage


class ItemInline(TranslatableStackedInline):
    model = Item
    extra = 0


class ItemImageInline(TranslatableStackedInline):
    model = ItemImage
    extra = 0


@admin.register(Bid)
class BidAdminConf(admin.ModelAdmin):
    form = BidForm
    list_display = [
        'pk', 'bidder', 'item', 'value', 'created', 'modified',
    ]


@admin.register(Event)
class EventAdminConf(TranslatableAdmin):
    list_display = [
        'pk', 'name', 'owner', 'start_date_time', 'end_date_time',
    ]
    inlines = [
        ItemInline,
    ]


@admin.register(EventAdmin)
class EventAdminAdminConf(admin.ModelAdmin):
    list_display = [
        'pk', 'user', 'event',
    ]


@admin.register(Item)
class ItemAdminConf(TranslatableAdmin):
    list_display = [
        'pk', 'seller', 'retail_value', 'starting_value', 'event', 'name', 'slug',
    ]
    inlines = [
        ItemImageInline,
    ]