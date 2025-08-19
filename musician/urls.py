from rest_framework.routers import DefaultRouter
from .views import MusicianViewSet

router = DefaultRouter()
router.register(r"musicians", MusicianViewSet, basename="musician")

urlpatterns = router.urls
