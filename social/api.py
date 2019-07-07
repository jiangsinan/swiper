from common import errors
from lib.http import render_json
from social import logic
from social.models import Swiped
from user.models import Users

def recommend(request):
    """
    根据当前登录用户的 profile 筛选符合条件的用户
    :param request:
    :return:
    """
    recm_users = logic.recommend_users(request.user)

    users = [u.to_dict() for u in recm_users]

    return render_json(data=users)


def like(request):
    sid = int(request.POST.get('sid'))
    user = request.user
    if logic.like_some(user.id,sid):
        return render_json()
    else:
        return render_json(code = errors.LIKE_ERR)


def superlike(request):
    sid = int(request.POST.get('sid'))
    user = request.user
    if logic.superlike_some(user.id, sid):
        return render_json()
    else:
        return render_json(code=errors.LIKE_ERR)


def dislike(request):
    return None


def rewind(request):
    return None


def liked_me(request):
    return None


def friends(request):
    return None