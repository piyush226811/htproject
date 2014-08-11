from rest_framework import permissions


class SafeMethodsOnlyPermission(permissions.BasePermission):
    """Only can access non-destructive methods (like GET and HEAD)"""
    def has_permission(self, request, view):
        return self.has_object_permission(request, view)
    
    def has_object_permission(self, request, view, obj=None):
        return request.method in permissions.SAFE_METHODS