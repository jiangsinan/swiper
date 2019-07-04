import datetime

from django.db import models

# Create your models here
from django.utils.functional import cached_property

from lib.orm import ModelToDictMixin


class Users(models.Model):
    phonenum = models.CharField(max_length=11,unique=True)
    nickname = models.CharField(max_length=32,null=True)
    sex = models.IntegerField(default=0)
    birth_year = models.IntegerField(default=2000)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=64,null=True)

    class Meta:
        db_table = 'users'

    @cached_property
    def age(self):
        today = datetime.date.today()
        birthday = datetime.date(self.birth_year,self.birth_month,self.birth_day,)

        return (today-birthday).days//365

    @property
    def profile(self):

        if not hasattr(self,'_profile'):
            self._profile,_ = Profile.objects.get_or_create(id=self.id)

        return self._profile


    def to_dict(self):
        return {
            'phonenum': self.phonenum,
            'nickname': self.nickname,
            'sex': self.sex,
            'avatar': self.avatar,
            'location': self.location,
            'age': self.age
        }



class Profile(models.Model,ModelToDictMixin):
    LOCATIONS = (
        ('bj', '北京'),
        ('sz', '深圳'),
        ('sh', '上海'),
    )

    SEXS = (
        (0, '全部'),
        (1, '男'),
        (2, '女')
    )

    location = models.CharField(max_length=64, choices=LOCATIONS)
    min_distance = models.IntegerField(default=1)
    max_distance = models.IntegerField(default=10)
    min_dating_age = models.IntegerField(default=18)
    max_dating_age = models.IntegerField(default=81)
    dating_sex = models.IntegerField(default=0, choices=SEXS)

    vibration = models.BooleanField(default=True)
    only_matche = models.BooleanField(default=True)
    auto_play = models.BooleanField(default=True)

    class Meta:
        db_table = 'profiles'