from rest_framework.routers import DefaultRouter

from apps.categories.views import CategoryAPI

router = DefaultRouter()
router.register('products', CategoryAPI, "api_products")

urlpatterns = router.urls
