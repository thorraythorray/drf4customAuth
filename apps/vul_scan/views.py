from rest_framework import viewsets

from apps.vul_scan.models import ScanTask
from apps.vul_scan.serializers import ScanTaskSerializer


class ScanTaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ScanTask.objects.all()
    serializer_class = ScanTaskSerializer
