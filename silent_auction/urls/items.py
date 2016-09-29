from rest_framework import routers
from silent_auction.views.items import ItemViewSet

router = routers.SimpleRouter()
router.register(r'items', ItemViewSet)
urlpatterns = router.urls
