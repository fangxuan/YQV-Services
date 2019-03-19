import json
from enum import Enum

from flask import Response


class SysStatus(Enum):
    SUCCESS = '成功'
    FAIL = '失败'
    NOT_FOUND = '页面未找到'
    PARAMETER_CHECK_ERROR = '参数校验失败'


def common_response(sys_status, data, message):
    if not message:
        message = sys_status.value
    res = json.dumps({'sys_status': sys_status.name, 'data': data, 'message': message})

    return Response(res, mimetype='application/json')
