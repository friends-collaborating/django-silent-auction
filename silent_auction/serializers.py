from datetime import datetime
from rest_framework import serializers
from rest_framework.exceptions import ParseError
from silent_auction.models import Bid, Event, Item, Location


class TagListSerializer(serializers.Field):
    def to_internal_value(self, data):
        if type(data) is not list:
            raise ParseError("expected a list of data")
        return data

    def to_representation(self, obj):
        if type(obj) is not list:
            return [tag.name for tag in obj.all()]
        return obj


class BidSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(
        read_only=True,
    )
    class Meta:
        model = Bid
        fields = (
            'bidder',
            'item',
            'value',
            'timestamp',
        )


class EventSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Event
        fields = (
            'name',
            'start_date',
            'end_date',
            'description',
            'owner',
            'location',
            'items',
        )


class ItemSerializer(serializers.ModelSerializer):
    bids = serializers.StringRelatedField(many=True, read_only=True)
    # tags = TagListSerializer(allow_null=True, read_only=True)
    class Meta:
        model = Item
        fields = (
            'name',
            'description',
            'seller',
            'retail_value',
            'min_bid',
            'event',
            'bids',
        )


class LocationSerializer(serializers.ModelSerializer):
    events = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Location
        fields = (
            'name',
            'events',
        )
