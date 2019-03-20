import random

from flask import Blueprint, request, session

from api.extensions import gen_md5, redis_store, db, login_user_data
from api.models.user import User
from api.schemas.user import login_schema, register_schema, sms_schema
from api.views.base import common_response, SysStatus

blue_print = Blueprint('user', __name__, url_prefix='/api/users')


@blue_print.route('/login', methods=['POST'])
def user_login():
    params = login_schema(request.json or '')
    phone = params.get('phone')
    password = params.get('password')
    password = gen_md5(password)

    user = User.query.filter(User.phone == phone, User.password == password).first()
    if user:
        session['user_id'] = user.id
        return common_response(SysStatus.SUCCESS, user.name, '登录成功')
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
    print(real_sms_code)
    if sms_code != real_sms_code:
        return common_response(SysStatus.FAIL, None, '短信校验码错误')

    password = gen_md5(password1)

    user = User.query.filter(User.phone == phone).first()
    if user:
        return common_response(SysStatus.FAIL, user.phone, '该手机号已注册')
    else:
        user = User(phone=phone, password=password)
        db.session.add(user)
        db.session.commit()
        redis_store.delete('{}-sms'.format(phone))
        return common_response(SysStatus.FAIL, None, '注册成功')


@blue_print.route('/sms', methods=['POST'])
def sms():
    params = sms_schema(request.json or '')
    phone = params.get('phone')

    sms_code = random.randint(0, 999999)
    sms_code = "%06d" % sms_code

    redis_store.set('{}-sms'.format(phone), sms_code, 60 * 5)
    print(sms_code)
    return common_response(SysStatus.FAIL, None, '发送成功')


@blue_print.route('/info', methods=['GET'])
@login_user_data
def user_info_get(user):
    # params = sms_schema(request.json or '')
    # user_id = params.get('id')

    user_id = user.id
    user = User.query.filter(User.id == user_id).first()
    print(user)
    return common_response(SysStatus.FAIL, None, '发送成功')
