import random
import re

PHONE_PATTERN = re.compile(r'^1[3-9]\d{9}$')

def is_phone_num(phone_num):
    if PHONE_PATTERN.match(phone_num):
        return True
    return False


def gen_random_code(length = 4):
    if length<=0:
        length=1
    code = random.randrange(10**(length-1),10**length)

    return str(code)