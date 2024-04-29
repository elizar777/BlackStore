from rest_framework.routers import DefaultRouter

from apps.users.views import UserAPI

router = DefaultRouter()
router.register('user', UserAPI , "api_user")

urlpatterns = router.urls