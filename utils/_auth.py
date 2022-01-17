from rest_framework_simplejwt.models import TokenUser
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.authentication import BaseAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth.middleware import AuthenticationMiddleware


from rest_framework_simplejwt.authentication import default_user_authentication_rule


def _jwt_user_authentication_rule(user):
    '''
    overloads 'from rest_framework_simplejwt.authentication import default_user_authentication_rule'
    '''
    print('qqqqqqq', user)
    return user is not None and user.active    


class _IsAuthenticated(IsAuthenticated):
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.active)
    


from django.db.models import Q
from django.contrib.auth.backends import BaseBackend

from apps.custom_auth.models import Users


class CustomAuthBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        # TODO: check password 明文加密
        # password = encrypt_str(password)
        print("username", username)
        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            return None
        print("user_id", user.id)
        return user


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class JWTTokenSerializer(TokenObtainPairSerializer):
    username_field = "username"


class JWTTokenObtainView(TokenObtainPairView):
    serializer_class = JWTTokenSerializer