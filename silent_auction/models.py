import uuid
from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager


class Location(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    name = models.CharField(
        max_length=160,
        unique=True,
    )
    slug = models.SlugField(
        max_length=160,
        unique=True,
    )

    class Meta:
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    name = models.CharField(
        max_length=160,
    )
    slug = models.SlugField(
        max_length=160,
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.ForeignKey(
        "Location"
    )
    description = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="auction_events",
    )

    class Meta:
        verbose_name_plural = "Events"
        unique_together = (
            ("name", "location", ),
            ("slug", "location", ),
        )

    def __str__(self):
        return "{name} @ {location}".format(
            name=self.name,
            location=self.location,
        )


class EventAdmin(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = "Event Admin"

    def __str__(self):
        return str(self.id)


class Item(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    name = models.CharField(
        max_length=160,
    )
    slug = models.SlugField(
        max_length=160,
    )
    description = models.TextField()
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    retail_value = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )
    min_bid = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )
    event = models.ForeignKey(
        "Event"
    )

    tags = TaggableManager()

    class Meta:
        verbose_name_plural = "Items"
        unique_together = (
            ("event", "name", ),
        )

    def __str__(self):
        return self.name


class Bid(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    bidder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="auction_bids",
    )
    item = models.ForeignKey(
        "Item",
        on_delete=models.CASCADE,
    )
    value = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )
    timestamp = models.DateTimeField(
        auto_created=True,
    )

    class Meta:
        verbose_name_plural = "Bids"

    def __str__(self):
        return str(self.id)