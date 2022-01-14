from rest_framework import serializers

from apps.vul_scan.models import UserSession, ScanTask


class UserSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserSession
        fields = '__all__'


class ScanTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScanTask
        fields = '__all__'
