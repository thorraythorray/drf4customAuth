from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomJWTTokenSerializer(TokenObtainPairSerializer):
    username_field = "username"
    
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data["username"] = self.user.username
        data["user_id"] = self.user.id

        return data
