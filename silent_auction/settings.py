"""Settings of silent_auction"""
from django.conf import settings


PROTOCOL = getattr(settings, 'SILENT_AUCTION_PROTOCOL', 'http')
