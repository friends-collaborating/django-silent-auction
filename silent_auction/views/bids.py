from rest_framework import viewsets
from silent_auction.models import Bid
from silent_auction.serializers import BidSerializer


class BidViewSet(viewsets.ModelViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    queryset = Bid.objects.all()
    serializer_class = BidSerializer
