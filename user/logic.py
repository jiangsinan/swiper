from django.core.cache import cache

from common import utils, config
from lib import sms


def send_verify_code(phone_num):
    code = utils.gen_random_code(6)
    ret = sms.send(phone_num,code)

    if ret:
        key = config.VERIFY_CODE_CACHE_PREFIX % phone_num
        print(key)
        cache.set(key,code,60*60)

    return ret
