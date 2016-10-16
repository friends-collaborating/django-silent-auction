# -*- coding: utf-8 -*-
import datetime
import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from parler.models import TranslatableModel
from parler.models import TranslatedFields
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.fields import PPOIField


class Event(TranslatableModel):
    _uid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    translations = TranslatedFields(
        name=models.CharField(_("name"), max_length=160),
        slug=models.SlugField(_("slug"), max_length=160),
        description=models.TextField(_("description")),
        meta={"unique_together": [
            ('language_code', 'slug', ),
            ('language_code', 'name', ),
        ]},
    )
    start_date_time = models.DateTimeField(
        _("start time"),
        default=timezone.now,
    )
    end_date_time = models.DateTimeField(
        _("end time"),
        default=timezone.now,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="auction_events",
        verbose_name=_('owner'),
    )

    class Meta:
        app_label = "silent_auction"
        verbose_name = _("event")
        verbose_name_plural = _("events")

    def __str__(self):
        return str(self.pk)


class EventAdmin(models.Model):
    _uid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    event = models.ForeignKey(
        "Event",
        on_delete=models.PROTECT,
        verbose_name=_("event"),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name=_("username"),
    )

    class Meta:
        app_label = "silent_auction"
        verbose_name = _("event admin")
        verbose_name_plural = _("event admins")
        unique_together =(
            ("event", "user", )
        )

    def __str__(self):
        return str(self.pk)


class Item(TranslatableModel):
    _uid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="auction_items",
        verbose_name=_("seller"),
    )
    retail_value = models.DecimalField(
        _("retail value"),
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
    )
    starting_bid = models.DecimalField(
        _("starting bid"),
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
    )
    min_bid_increase = models.DecimalField(
        _("min bid increase"),
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True,
    )
    event = models.ForeignKey(
        "Event",
        related_name='items',
        verbose_name=_("event"),
    )
    translations = TranslatedFields(
        name=models.CharField(_("name"), max_length=160),
        slug=models.SlugField(_("slug"), max_length=160),
        description=models.TextField(_("description")),
        meta={"unique_together": [
            ('language_code', 'slug', ),
            ('language_code', 'name', ),
        ]},
    )

    class Meta:
        app_label = "silent_auction"
        verbose_name = _("item")
        verbose_name_plural = _("items")

    def __str__(self):
        return str(self.pk)


class ItemImage(TranslatableModel):
    _uid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )

    translations = TranslatedFields(
        name=models.CharField(_("name"), max_length=160),
        description=models.TextField(_("description")),
    )

    item = models.ForeignKey(
        "Item",
        related_name='images',
        verbose_name=_("item"),
    )

    image = VersatileImageField(
        _('image'),
        upload_to='item_images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    def __str__(self):
        return str(self.pk)


class Bid(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    bidder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="auction_bids",
        verbose_name=_("bidder"),
    )
    item = models.ForeignKey(
        "Item",
        on_delete=models.CASCADE,
        related_name="bids",
        verbose_name=_("item"),
    )
    value = models.DecimalField(
        _("value"),
        max_digits=7,
        decimal_places=2,
    )
    created = models.DateTimeField(
        editable=False,
        default=timezone.now,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name_plural = "Bids"

    def __str__(self):
        return str(self.pk)
