from flask import Blueprint, request

from api import redis_store
from api.extensions import gen_md5
from api.models.user import User
from api.schemas.user import login_schema, register_schema
from api.views.base import common_response, SysStatus

blue_print = Blueprint('user', __name__, url_prefix='/api/users')


@blue_print.route('/login', methods=['POST'])
def user_login():
    params = login_schema(request.json or '')
    phone = params.get('phone')
    password = params.get('password')
    password = gen_md5(password)
    print(password)

    user = User.query.filter(User.phone == phone, User.password == password).first()
    if user:
        return common_response(SysStatus.SUCCESS, user, '登录成功')
    else:
        return common_response(SysStatus.FAIL, None, '手号或密码错误')


@blue_print.route('/register', methods=['POST'])
def user_reg():
    params = register_schema(request.json or '')
    phone = params.get('phone')
    password1 = params.get('password1')
    password2 = params.get('password2')
    sms_code = params.get('sms_code')

    if password1 != password2:
        return common_response(SysStatus.FAIL, None, '密码不一致')

    real_sms_code = redis_store.get('{}-sms'.format(phone))
    if sms_code != real_sms_code:
        return common_response(SysStatus.FAIL, None, '短信校验码错误')

    password = gen_md5(password1)
    print(password)

    user = User.query.filter(User.phone == phone).first()
    if user:
        return common_response(SysStatus.FAIL, user, '该手机号已注册')
    else:
        return common_response(SysStatus.FAIL, None, '注册成功')
    #
