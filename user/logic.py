from common import utils
from lib import sms


def send_verify_code(phone_num):
    code = utils.gen_random_code(6)
    return sms.send(phone_num,code)