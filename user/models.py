from django.db import models

# Create your models here
class Users(models.Model):
    phonenum = models.CharField(max_length=11,unique=True)
    nickname = models.CharField(max_length=32)
    sex = models.IntegerField(default=0)
    birth_year = models.IntegerField(default=2000)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=64)

    class Meta:
        db_table = 'users'