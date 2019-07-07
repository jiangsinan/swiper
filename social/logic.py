import datetime

from social.models import Swiped, Friend
from user.models import Users


def recommend_users(user):
    """
    筛选符合 user.profile 条件的用户
    过滤掉已经被划过的用户
    :param user:
    :return:
    """
    today = datetime.date.today()

    # 1999 = 2019 - 20
    max_year = today.year - user.profile.min_dating_age
    # 2001 = 2019 - 18
    min_year = today.year - user.profile.max_dating_age

    swiped_users = Swiped.objects.filter(uid=user.id).only('sid')
    swiped_sid_list = [s.sid for s in swiped_users]

    users = Users.objects.filter(
        sex=user.profile.dating_sex,
        location=user.profile.location,
        birth_year__gte=min_year,
        birth_year__lte=max_year,
    ).exclude(id__in=swiped_sid_list)[:20]

    return users


def like_some(uid, sid):
    if not Users.objects.filter(id=sid).exists():
        return False
    Swiped.objects.create(uid=uid,sid=sid,mark = 'like')

    if Swiped.is_like(sid,uid):
        Friend.make_friend(uid,sid)
    return True


def superlike_some(uid, sid):
    if not Users.objects.filter(id=sid).exists():
        return False
    Swiped.objects.create(uid=uid,sid=sid,mark = 'superlike')

    Friend.make_friend(uid,sid)
    return True