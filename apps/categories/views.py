from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer

class CategoryAPI(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset =Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        if self.action == 'retrive':
            return (IsAuthenticated(),)
        return (AllowAny(),)
        

