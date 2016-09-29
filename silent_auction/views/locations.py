from rest_framework import viewsets
from silent_auction.models import Location

class LocationViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def list(self, request):
        queryset = Location.objects.all()

    def create(self, request):
        queryset = Location.objects.all()

    def retrieve(self, request, pk=None):
        queryset = Location.objects.all()

    def update(self, request, pk=None):
        queryset = Location.objects.all()

    def partial_update(self, request, pk=None):
        queryset = Location.objects.all()

    def destroy(self, request, pk=None):
        queryset = Location.objects.all()
