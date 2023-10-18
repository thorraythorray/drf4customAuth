from django.utils.translation import gettext_lazy as _
from django.contrib.auth.backends import BaseBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken
from rest_framework_simplejwt.settings import api_settings

from apps.custom_auth.models import Users


class CustomAuthBackend(BaseBackend):
    '''
    overwrite Authentication Backend with custom user model
    '''
    def authenticate(self, request, username=None, password=None, **kwargs):
        '''
        Params transfered from serialization ('is_valid' function)
        '''
        # TODO: ignore password validation
        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            return None

        return user


class CustomJWTAuthentication(JWTAuthentication):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_model = Users

    def get_user(self, validated_token):
        """
        Attempts to find and return a user using the given validated token.
        """
        try:
            user_id = validated_token[api_settings.USER_ID_CLAIM]
        except KeyError:
            raise InvalidToken(_('Token contained no recognizable user identification'))

        try:
            user = self.user_model.objects.get(**{api_settings.USER_ID_FIELD: user_id})
            print('custom jwt get user!', user.username)
        except self.user_model.DoesNotExist:
            raise AuthenticationFailed(_('User not found'), code='user_not_found')

        if not user.active:
            raise AuthenticationFailed(_('User is inactive'), code='user_inactive')

        return user


def custom_jwt_token_authentication_rule(user):
    '''
    only authenticate in case with Getting Token

    refer 'from rest_framework_simplejwt.authentication import default_user_authentication_rule'
    '''
    return user is not None and user.active
