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

class FriendManager(models.Manager):
    """
    自定义 Manager，扩充 models.Manager 的默认行为，增加和业务相关的方法
    """
    def make_friends(self, uid1, uid2):
        uid1, uid2 = (uid1, uid2) if uid1 <= uid2 else (uid2, uid1)
        # self.create(uid1=uid1, uid2=uid2)
        self.get_or_create(uid1=uid1, uid2=uid2)

class Friend(models.Model):


    objects = FriendManager()

    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    @classmethod
    def make_friend(cls,uid1,uid2):

        uid1,uid2 = (uid1,uid2) if uid1 <= uid2 else (uid2,uid1)
        cls.objects.create(uid1=uid1,uid2=uid2)

    @classmethod
    def cancel_friends(cls, uid1, uid2):

        uid1, uid2 = (uid1, uid2) if uid1 <= uid2 else (uid2, uid1)
        cls.objects.filter(uid1=uid1, uid2=uid2).delete()



    class Meta:
        db_table = 'friends'