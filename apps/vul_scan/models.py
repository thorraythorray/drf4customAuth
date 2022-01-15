import uuid

from django.db import models

from apps.base.models import BaseDateTime


# Create your models here.
class ScanTask(BaseDateTime):
    system_id = models.IntegerField('系统ID', default=0)
    scan_id = models.CharField('扫描ID', max_length=128)
    ips = models.CharField('扫描的网段', max_length=256)
    ports = models.CharField('扫描的端口', max_length=256)
    # scope = models.
    more = models.TextField()

    class Meta:
        ordering = ['update_tm']
        app_label = 'vul_scan'
