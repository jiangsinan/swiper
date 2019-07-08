from django.db import models

# Create your models here.

class Vip(models.Model):
    """
    会员
    """
    name = models.CharField(max_length=32, unique=True)
    level = models.IntegerField(unique=True, default=0)
    # price decimal(5,2)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        db_table = 'vips'


class Permission(models.Model):
    """
    权限
    """
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField()

    class Meta:
        db_table = 'permissions'


class VipPermission(models.Model):
    """
    会员-权限 关系
    """
    vip_id = models.IntegerField()
    perm_id = models.IntegerField()

    class Meta:
        db_table = 'vip_permissions'
