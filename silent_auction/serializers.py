from rest_framework import serializers
from parler_rest.serializers import (
    TranslatableModelSerializer,
    TranslatedFieldsField,
)
from silent_auction.models import (
    Bid,
    Event,
    EventAdmin,
    Item,
)


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


class EventAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAdmin
        fields = (
            'event',
            'user',
        )


class EventSerializer(TranslatableModelSerializer):
    items = serializers.StringRelatedField(many=True, read_only=True)
    translations = TranslatedFieldsField(shared_model=Event)

    class Meta:
        model = Event
        fields = (
            'start_date',
            'end_date',
            'owner',
            'items',
            'translations',
        )


class ItemSerializer(TranslatableModelSerializer):
    bids = serializers.StringRelatedField(many=True, read_only=True)
    translations = TranslatedFieldsField(shared_model=Item)

    class Meta:
        model = Item
        fields = (
            'seller',
            'retail_value',
            'min_bid',
            'event',
            'bids',
            'translations',
        )
