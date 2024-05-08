from rest_framework.permissions import BasePermission

class ProductPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.user.pk == request.user.pk)z