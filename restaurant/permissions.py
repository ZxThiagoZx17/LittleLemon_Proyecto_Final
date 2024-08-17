from rest_framework.permissions import BasePermission, IsAuthenticated


class IsOwnerOrAdmin(BasePermission):
    """
    Custom permission to only allow owners of the object
    to edit it or view it.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in ['GET', 'HEAD', 'OPTIONS', 'POST']:
            return True
        if request.user.is_staff:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            return request.user.is_staff or request.user.is_superuser
        return obj.user == request.user


class IsAdminOrStaffOrOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_superuser:
            return True
        return obj.user == request.user