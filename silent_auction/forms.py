# -*- coding: utf-8 -*-
import logging
from decimal import Decimal
from django import forms
from django.utils.translation import ugettext_lazy as _
from silent_auction.models import Bid
from silent_auction.models import Event
from silent_auction.models import Item

logger = logging.getLogger(__name__)


class BidForm(forms.ModelForm):
    model = Bid

    def clean_value(self):
        item = self.cleaned_data["item"]
        value = self.cleaned_data["value"]
        is_above_start_value = self.is_above_starting_value(item=item, value=value)
        is_above_increase = self.is_above_min_increase(item=item, value=value)
        if not (is_above_start_value and is_above_increase):
            raise forms.ValidationError(
                _("Insufficient value"),
                code='insufficient_value')
        return value

    def clean(self):
        bidder = self.cleaned_data["bidder"]
        item = self.cleaned_data["item"]
        if self.is_bid_against_self(item=item, bidder=bidder):
            raise forms.ValidationError(
                _("You already have the winning bid!"),
                code='already_winning')

    def is_bid_against_self(self, item, bidder):
        """
        """
        winning_bid = item.get_winning_bid()
        if winning_bid is not None:
            if bidder == winning_bid.bidder:
                return True
        return False

    def is_above_starting_value(self, item, value):
        """
        """
        starting_value = item.starting_value
        if starting_value is None:
            starting_value = Decimal('0.00')
        if value < starting_value:
            logger.info("starting_value {} is greater than bid value {}".format(starting_value, value))
            return False
        return True

    def is_above_min_increase(self, item, value):
        """
        """
        min_increase = item.min_increase
        if min_increase is None:
            min_increase = Decimal('0.01')
        winning_bid = item.get_winning_bid()
        if winning_bid is None:
            winning_value = Decimal('0.00')
        else:
            winning_value = winning_bid.value
        next_min_winning_value = winning_value + min_increase
        if value < next_min_winning_value:
            logger.info("next_min_winning_value {} is greater than bid value {}".format(next_min_winning_value, value))
            return False
        else:
            return True


class EventForm(forms.ModelForm):
    model = Event


class ItemForm(forms.ModelForm):
    model = Item
