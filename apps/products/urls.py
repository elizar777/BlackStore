from rest_framework.routers import DefaultRouter

from apps.products.views import ProductAPI

router = DefaultRouter()
router.register('product', ProductAPI, "api_products")

urlpatterns = router.urls