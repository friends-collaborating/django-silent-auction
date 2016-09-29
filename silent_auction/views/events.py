from rest_framework import viewsets
from silent_auction.models import Event


class EventViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def list(self, request):
        queryset = Event.objects.all()

    def create(self, request):
        queryset = Event.objects.all()

    def retrieve(self, request, pk=None):
        queryset = Event.objects.all()

    def update(self, request, pk=None):
        queryset = Event.objects.all()

    def partial_update(self, request, pk=None):
        queryset = Event.objects.all()

    def destroy(self, request, pk=None):
        queryset = Event.objects.all()
