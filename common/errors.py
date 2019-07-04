"""
业务返回码，错误码配置
"""

OK = 0

# 用户系统
# 1001 = '手机号格式错误'
PHONE_NUM_ERR = 1001  # 手机号格式错误
SMS_SEND_ERR = 1002  # 短信发送失败
VERIFY_CODE_ERR = 1003  # 验证码错误
LOGIN_REQUIRED = 1004  # 未登录