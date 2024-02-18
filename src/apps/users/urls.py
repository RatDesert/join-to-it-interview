from rest_framework.routers import DefaultRouter

from src.apps.users.views import UserRegistrationViewSet

router = DefaultRouter()
router.register("", UserRegistrationViewSet, basename="users")

urlpatterns = router.urls
