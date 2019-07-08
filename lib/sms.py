import requests

from common import config


def send(phone_num,code):
    params = config.YZX_SMS_PARAMS.copy()
    print(type(phone_num),type(code))
    params['mobile']=phone_num
    params['param']=code
    print(phone_num,code)

    resp = requests.post(config.YZX_SMS_URL,json=params)
    print(resp.status_code)

    if resp.status_code==200:
        result = resp.json()
        if result.get('code')=='000000':
            return True
    return False