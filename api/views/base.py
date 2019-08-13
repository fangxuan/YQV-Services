import datetime
from decimal import Decimal

from enum import Enum

from flask import Response, render_template
import simplejson

from api.settings import origin


class SysStatus(Enum):
    SUCCESS = '成功'
    FAIL = '失败'
    NOT_FOUND = '页面未找到'
    PARAMETER_CHECK_ERROR = '参数校验失败'


class StatusCode(Enum):
    SUCCESS = 2000
    FAIL = 2001
    NOT_FOUND = 4004
    PARAMETER_CHECK_ERROR = 3001


class DatatimeEncoder(simplejson.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, Enum):
            return {obj.name: obj.value}
        elif isinstance(obj, Decimal):
            return str(obj.quantize(Decimal('0.00')))
        return simplejson.JSONEncoder.default(self, obj)


def common_response(sys_status, data, message):
    if not message:
        message = sys_status.value
    res = simplejson.dumps({'sys_status': sys_status.name, 'data': data, 'message': message}, ensure_ascii=False,
                           use_decimal=False,
                           cls=DatatimeEncoder)
    response = Response(res, mimetype='application/json')
    response.headers.add('Access-Control-Allow-Origin', origin)

    return response


def render_data(username, body):
    html_str = """<h1>Farm land</h1><div>{username}</div><body>{body}</body>""".format(username, body)
    return render_template(html_str)
