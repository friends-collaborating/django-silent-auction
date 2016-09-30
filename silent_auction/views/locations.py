from rest_framework import viewsets
from silent_auction.models import Location
from silent_auction.serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
