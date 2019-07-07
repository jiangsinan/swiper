from django.db import models

# Create your models here.

class Swiped(models.Model):
    """
    划过的记录
    """
    MARKS = (
        ('like', '喜欢'),
        ('dislike', '不喜欢'),
        ('superlike', '超级喜欢')
    )

    uid = models.IntegerField()
    sid = models.IntegerField()
    mark = models.CharField(max_length=16, choices=MARKS)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def is_like(cls,sid,uid):
        return cls.objects.filter(uid=uid,sid=sid,mark__in=['like','superlike']).exists()


    class Meta:
        db_table = 'swiped'


class Friend(models.Model):
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    @classmethod
    def make_friend(cls,uid1,uid2):

        uid1,uid2 = (uid1,uid2) if uid1 <= uid2 else (uid2,uid1)
        cls.objects.create(uid1=uid1,uid2=uid2)

    class Meta:
        db_table = 'friends'