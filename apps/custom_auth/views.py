from rest_framework_simplejwt.views import TokenViewBase

from apps.custom_auth.serializers import CustomJWTTokenSerializer


class CustomJwtTokenView(TokenViewBase):
    '''
    Customize JWT token reponse format
    
    implentate as view funciton in 'api/token' url 
    '''
    # permission_classes = [CustomIsAuthenticated]
    serializer_class = CustomJWTTokenSerializer
