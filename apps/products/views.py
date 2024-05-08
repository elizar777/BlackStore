from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.products.models import Product
from apps.products.serializers import ProductSerializer
from apps.products.permissions import ProductPermissions

class ProductAPI(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset =Product.objects.all()
    serializer_class = ProductSerializer
    
    
    def get_permissions(self):
        if self.action == 'retrive':
            return (IsAuthenticated(),)
        if self.action in ('update','partial_update', 'destroy'):
            return (ProductPermissions(), )
        return (AllowAny(),)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)