import datetime

from django.core.cache import cache

from common import errors, config
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
        raise errors.SidError

    ret = Swiped.swipe(uid=uid, sid=sid, mark='like')

    if ret and Swiped.is_like(sid,uid):
        # Friend.make_friend(uid,sid)
        Friend.objects.make_friends(uid, sid)
    return ret


def superlike_some(uid, sid):
    if not Users.objects.filter(id=sid).exists():
        return False

    ret = Swiped.swipe(uid=uid,sid=sid,mark='superlike')
    if ret:
        Friend.make_friend(uid,sid)
    return ret


def rewind(user):
    """
    撤销当前登录用户的上传一次滑动操作
    每天只能撤销三次
    :param user:
    :return:
    """
    key = config.REWIND_CACHE_PREFIX % user.id

    rewind_times = cache.get(key, 0)

    if rewind_times >= config.REWIND_TIMES:
        raise errors.RewindLimitError

    swipe = Swiped.objects.filter(uid=user.id).latest('created_at')

    if swipe.mark in ['like', 'superlike']:
        Friend.cancel_friends(user.id, swipe.sid)

    swipe.delete()

    now = datetime.datetime.now()
    timeout = 86400 - now.hour * 3600 - now.minute * 60 - now.second
    cache.set(key, rewind_times + 1, timeout=timeout)


def liked_me(user):
    """
    喜欢我的人列表
    :param user:
    :return:
    """
    # 过滤掉已经加为好友的用户
    friend_uid_list = Friend.friend_list(user.id)

    swipe_list = Swiped.objects.filter(sid=user.id, mark='like').exclude(uid__in=friend_uid_list)

    liked_me_uid_list = [s.uid for s in swipe_list]

    return liked_me_uid_list