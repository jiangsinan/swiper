from django.conf import settings
from django.http import JsonResponse

from common import errors


def render_json(code=errors.OK,data=None):
    result = {
        'code':code
    }

    if data:
        result['data'] = data

    if settings.DEBUG:
        json_dump_params = {'indent':4,'ensure_ascii':False}
    else:
        json_dump_params = {'separators':(':',',')}
    return JsonResponse(result,json_dumps_params=json_dump_params)