from rest_framework import serializers
from silent_auction.models import Bid, Event, Item, Location


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ('bidder', 'item', 'value', )


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('name', 'start_date', 'end_date', 'description', 'owner', 'location')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'description', 'seller', 'retail_value', 'min_bid', 'event', 'tags')


class LocationSerializer(serializers.ModelSerializer):
    events = serializers.StringRelatedField(many=True)
    class Meta:
        model = Location
        fields = ('name', 'events')


