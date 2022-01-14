import uuid

from django.db import models

from apps.base.models import BaseDateTime


class UserSession(BaseDateTime):
    ip = models.GenericIPAddressField('Host')
    port = models.IntegerField('Port', default=22)
    protocol = models.CharField('Protocol', max_length=16)
    username = models.CharField('Username', max_length=16)
    sshkey_login = models.BooleanField('是否免密登录', default=False)
    password = models.CharField('Password', max_length=64, null=True)

    class Meta:
        unique_together = (("ip", "port", "protocol", "username"),)
        ordering = ['update_tm']
        app_label = 'vul_scan'


# Create your models here.
class ScanTask(BaseDateTime):
    system_id = models.IntegerField('系统ID', default=0)
    scan_id = models.UUIDField('扫描ID', default=uuid.uuid1())
    ips = models.CharField('扫描的网段', max_length=256)
    ports = models.CharField('扫描的端口', max_length=256)
    # scope = models.
    more = models.TextField()

    class Meta:
        ordering = ['update_tm']
        app_label = 'vul_scan'
