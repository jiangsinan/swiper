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

# 七牛云配置
QN_ACCESS_KEY = 'xgCbAAXzadtdbc_Ab2fc4lZdvTG9N-yE5nHynAYk'
QN_SECRET_KEY = 'W18Qk66RQzW-F7i6dasZXfZMK_du8zA42dzdT3sh'
QN_BUCKET = 'swiper'
QN_HOST = 'http://pu6a9l328.bkt.clouddn.com'