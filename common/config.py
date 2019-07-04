"""
业务模块配置
"""

# 云之讯短信平台配置
YZX_SMS_URL = 'https://open.ucpaas.com/ol/sms/sendsms'

YZX_SMS_PARAMS = {
    'sid': 'cf0effa0ea608bc42cf76941d7bad4ea',
    'token': 'dfcb1b3b5aeb4dba1fb49155b2cf46ba',
    'appid': 'acfdae85b2614a799becc632ce011f11',
    'templateid': '482043',
    'param': None,
    'mobile': None
}

# 缓存 key prefix
VERIFY_CODE_CACHE_PREFIX = 'verfiy_code:%s'