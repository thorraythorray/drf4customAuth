from rest_framework import viewsets

from apps.vul_scan.models import UserSession, ScanTask
from apps.vul_scan.serializers import UserSessionSerializer, ScanTaskSerializer


class UserSessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserSession.objects.all()
    serializer_class = UserSessionSerializer


class ScanTaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ScanTask.objects.all()
    serializer_class = ScanTaskSerializer
