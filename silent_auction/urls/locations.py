from rest_framework import routers
from silent_auction.views.locations import LocationViewSet

router = routers.SimpleRouter()
router.register(r'locations', LocationViewSet)
urlpatterns = router.urls
