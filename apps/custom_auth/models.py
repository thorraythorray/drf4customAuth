from django.db import models

from apps.base.models import BaseDateTime


USER_PERMISSION_LEVEL = (
    (0, 'supervisor'),
    (1, 'administrator'),

    (6, 'staff'),

    (11, 'guest')
)

# Create your models here.
class Users(BaseDateTime):
    username = models.CharField('名字', max_length=128, unique=True, db_index=True)
    email = models.CharField('邮箱', max_length=255, unique=True)
    phone = models.IntegerField('电话', null=True, blank=True, unique=True)
    active = models.BooleanField('是否激活')
    level = models.SmallIntegerField('等级', choices=USER_PERMISSION_LEVEL, default=6)
    password = models.CharField('密码', max_length=128)
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        ordering = ['create_tm']

    def is_supervisor(self):
        return self.level == 0


class CustomSessions(BaseDateTime):
    ip = models.GenericIPAddressField('Host')
    port = models.IntegerField('Port', default=22)
    protocol = models.CharField('Protocol', max_length=16)
    username = models.CharField('Username', max_length=16)
    sshkey_login = models.BooleanField('是否免密登录', default=False)
    password = models.CharField('Password', max_length=64, null=True)

    class Meta:
        unique_together = (("ip", "port", "protocol", "username"),)
        ordering = ['update_tm']
