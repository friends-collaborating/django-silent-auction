# -*- coding: utf-8 -*-
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from silent_auction.serializers import (
    EventSerializer,
    ItemSerializer,
)
from silent_auction.models import (
    Event,
    Item,
)


@api_view(['GET', ])
def retrieve_event(request, event_uuid):
    """
    """
    if request.method == 'GET':
        try:
            queryset = Event.objects.get(pk=event_uuid)
        except Event.DoesNotExist:
            response_data = {
                "error": {
                    "state": "not found",
                    "details": "Event object with ID {} could not be found.".format(event_uuid)
                }
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = EventSerializer(queryset, context={'request': request})
            response_data = serializer.data
            return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST', ])
def create_event(request):
    """
    """
    if request.method == 'POST':
        response_data = {"details": "not implemented"}
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(['PUT', ])
def update_event(request, event_uuid):
    """
    """
    if request.method == 'PUT':
        response_data = {"details": "not implemented"}
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def delete_event(request, event_uuid):
    """
    """
    if request.method == 'GET':
        response_data = {"details": "not implemented"}
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def list_events(request):
    """
    """
    if request.method == 'GET':
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True, context={'request': request})
        response_data = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def list_event_items(request, event_uuid):
    """
    """
    if request.method == 'GET':
        try:
            queryset = Item.objects.filter(event=Event.objects.get(pk=event_uuid))
        except Event.DoesNotExist:
            response_data = {
                "error": {
                    "state": "not found",
                    "details": "Event object with ID {} could not be found.".format(event_uuid)
                }
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = ItemSerializer(queryset, many=True, context={'request': request})
            response_data = serializer.data
            return Response(response_data, status=status.HTTP_200_OK)