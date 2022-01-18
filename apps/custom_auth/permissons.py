from rest_framework.permissions import BasePermission


class CustomIsAuthenticated(BasePermission):
    '''
    add in 'DEFAULT_PERMISSION_CLASSES', to vaildate permission
    
    implentation in 'as_view' funciton, authenticate when api request
    '''
    def has_permission(self, request, view):
        return bool(request.user and request.user.active)
