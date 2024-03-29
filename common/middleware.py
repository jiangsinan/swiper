from django.utils.deprecation import MiddlewareMixin

from common import errors
from common.errors import LogicException, LogicError
from lib.http import render_json
from user.models import Users


class AuthMiddleware(MiddlewareMixin):
    WHITE_LIST = [
        '/api/user/verify-phone',
        '/api/user/login',
    ]

    def process_request(self,request):
        if request.path in self.WHITE_LIST:
            return None

        uid = request.session.get('uid')
        if uid is None:
            return render_json(code=errors.LOGIN_REQUIRED)


        request.user = Users.objects.get(id=uid)


class LogicExceptionMiddleware(MiddlewareMixin):

    def process_exception(self, request, exception):
        if isinstance(exception, (LogicException, LogicError)):
            return render_json(code=exception.code)