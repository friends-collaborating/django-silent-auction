from rest_framework import routers
from silent_auction.views.bids import BidViewSet

router = routers.SimpleRouter()
router.register(r'bids', BidViewSet)
urlpatterns = router.urls
