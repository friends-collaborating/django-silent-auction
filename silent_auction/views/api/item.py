# -*- coding: utf-8 -*-
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User
from django.db.models import Max
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from silent_auction.serializers import (
    BidSerializer,
    ItemSerializer,
)
from silent_auction.models import (
    Bid,
    Item,
)


@api_view(['GET', ])
def retrieve_item(request, item_uuid):
    """
    """
    if request.method == 'GET':
        try:
            queryset = Item.objects.get(pk=item_uuid)
        except Item.DoesNotExist:
            response_data = {
                "error": {
                    "state": "not found",
                    "details": "Item object with ID {} could not be found.".format(item_uuid)
                }
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = ItemSerializer(queryset, context={'request': request})
            response_data = serializer.data
            return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST', ])
def create_item(request):
    """
    """
    if request.method == 'POST':
        response_data = {"details": "not implemented"}
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(['PUT', ])
def update_item(request, item_uuid):
    """
    """
    if request.method == 'PUT':
        response_data = {"details": "not implemented"}
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def delete_item(request, item_uuid):
    """
    """
    if request.method == 'GET':
        response_data = {"details": "not implemented"}
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def list_items(request):
    if request.method == 'GET':
        queryset = Item.objects.all()
        serializer = ItemSerializer(queryset, many=True, context={'request': request})
        response_data = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def retrieve_highest_bid(request, item_uuid):
    """
    """
    if request.method == 'GET':
        try:
            queryset = Bid.objects.filter(item=Item.objects.get(pk=item_uuid)).latest('value')
        except Item.DoesNotExist:
            response_data = {
                "error": {
                    "state": "not found",
                    "details": "Event object with ID {} could not be found.".format(item_uuid)
                }
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = BidSerializer(queryset)
            response_data = serializer.data
            return Response(response_data, status=status.HTTP_200_OK)