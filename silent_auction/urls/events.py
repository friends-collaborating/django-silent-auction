from rest_framework import routers
from silent_auction.views.events import EventViewSet

router = routers.SimpleRouter()
router.register(r'events', EventViewSet)
urlpatterns = router.urls
