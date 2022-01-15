from rest_framework import serializers

from apps.vul_scan.models import ScanTask


class ScanTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScanTask
        fields = '__all__'
