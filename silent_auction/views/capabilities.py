"""Views for silent_auction capabilities"""
from django.contrib.sites.models import Site
from django.views.generic.base import TemplateView

from silent_auction.settings import PROTOCOL
from silent_auction.settings import COPYRIGHT
from silent_auction.settings import FEEDS_FORMAT


class CapabilityView(TemplateView):
    """
    Base view for the weblog capabilities.
    """

    def get_context_data(self, **kwargs):
        """
        Populate the context of the template
        with technical informations for building urls.
        """
        context = super(CapabilityView, self).get_context_data(**kwargs)
        context.update({'protocol': PROTOCOL,
                        'copyright': COPYRIGHT,
                        'feeds_format': FEEDS_FORMAT,
                        'site': Site.objects.get_current()})
        return context


class HumansTxt(CapabilityView):
    """
    http://humanstxt.org/
    """
    content_type = 'text/plain'
    template_name = 'silent_auction/humans.txt'


class RsdXml(CapabilityView):
    """
    http://en.wikipedia.org/wiki/Really_Simple_Discovery
    """
    content_type = 'application/rsd+xml'
    template_name = 'silent_auction/rsd.xml'


class WLWManifestXml(CapabilityView):
    """
    http://msdn.microsoft.com/en-us/library/bb463260.aspx
    """
    content_type = 'application/wlwmanifest+xml'
    template_name = 'silent_auction/wlwmanifest.xml'


class OpenSearchXml(CapabilityView):
    """
    http://www.opensearch.org/
    """
    content_type = 'application/opensearchdescription+xml'
    template_name = 'silent_auction/opensearch.xml'