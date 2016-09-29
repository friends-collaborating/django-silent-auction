"""Settings of silent_auction"""
from django.conf import settings


PROTOCOL = getattr(settings, 'SILENT_AUCTION_PROTOCOL', 'http')
COPYRIGHT = getattr(settings, 'SILENT_AUCTION_COPYRIGHT', 'Friends Collaborating')
FEEDS_FORMAT = getattr(settings, 'SILENT_AUCTION_FEEDS_FORMAT', 'rss')