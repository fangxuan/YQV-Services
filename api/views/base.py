import datetime

from enum import Enum

from flask import Response, json


class SysStatus(Enum):
    SUCCESS = '成功'
    FAIL = '失败'
    NOT_FOUND = '页面未找到'
    PARAMETER_CHECK_ERROR = '参数校验失败'


class DatatimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, Enum):
            return {obj.name: obj.value}
        return json.JSONEncoder.default(self, obj)


def common_response(sys_status, data, message):
    if not message:
        message = sys_status.value
    res = json.dumps({'sys_status': sys_status.name, 'data': data, 'message': message}, ensure_ascii=False, cls=DatatimeEncoder)

    return Response(res, mimetype='application/json')
