from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_authenticated:
            return False
            
        # Check if user is the author
        if hasattr(obj, 'author') and obj.author == request.user:
            return True
            
        # Check user role permissions
        if hasattr(request.user, 'role'):
            return request.user.role in ['admin', 'editor']
            
        return False