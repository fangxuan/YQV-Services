import random

from flask import Blueprint, request, session

from api.extensions import gen_md5, redis_store, db, login_user_data
from api.models.user import User
from api.schemas.user import login_schema, register_schema, sms_schema, user_info_schema
from api.views.base import common_response, SysStatus, render_data

blue_print = Blueprint('user', __name__, url_prefix='/api/v0/user')


@blue_print.route('/login', methods=['POST'])
def user_login():
    params = login_schema(request.json or '')
    phone = params.get('phone')
    password = params.get('password')
    # password = gen_md5(password) # TODO：正式环境加密密码

    user = User.query.filter(User.phone == phone, User.password == password).first()
    if user:
        session['user_id'] = user.id
        return common_response(SysStatus.SUCCESS, user.name, '登录成功')
    else:
        return common_response(SysStatus.FAIL, None, '账号号或密码错误')


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
    print("sms-code for {}: {}".format(phone, real_sms_code))
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
        return common_response(SysStatus.FAIL, None, '注册成功')  # TODO:去除返回的验证码


@blue_print.route('/reset_password', methods=['POST'])
def lost_pass():
    params = register_schema(request.json or '')
    phone = params.get('phone')
    password_old = params.get('password_old')
    password = params.get('password')
    sms_code = params.get('sms_code')

    real_sms_code = redis_store.get('{}-sms'.format(phone))
    print("sms-code for {}: {}".format(phone, real_sms_code))
    if sms_code != real_sms_code:
        return common_response(SysStatus.FAIL, None, '短信校验码错误')

    # password = gen_md5(password1) TODO: 正式环境不要明文保存密码
    # password_old = gen_md5(password_old) TODO: 正式环境不要明文保存密码

    user = User.query.filter(User.phone == phone, User.password == password_old).first()
    if user:
        user.password = password
        user.save()
        redis_store.delete('{}-sms'.format(phone))
    else:
        return common_response(SysStatus.FAIL, None, '原密码错误')


@blue_print.route('/sms', methods=['POST'])
def sms():
    params = sms_schema(request.json or '')
    phone = params.get('phone')

    sms_code = random.randint(0, 999999)
    sms_code = "%06d" % sms_code

    redis_store.set('{}-sms'.format(phone), sms_code, 60 * 5)
    print(sms_code)
    return common_response(SysStatus.SUCCESS, {'code': sms_code}, '发送成功')


@blue_print.route('/info', methods=['GET'])
@login_user_data
def user_info_get(user):
    user_id = user.id
    user = User.query.filter(User.id == user_id).with_entities(User.id,
                                                               User.avatar,
                                                               User.name,
                                                               User.phone,
                                                               User.birthday,
                                                               User.gender,
                                                               User.email,
                                                               ).first()

    return common_response(SysStatus.SUCCESS, user, None)


@blue_print.route('/info', methods=['PUT'])
@login_user_data
def user_info_put(user):
    params = request.json or ''
    params = user_info_schema(params)
    user.update(params)
    user.save()
    return common_response(SysStatus.SUCCESS, user, None)


@blue_print.route('/my_farm', methods=['GET'])
@login_user_data
def my_farm(user):
    return render_data(username='509', body='this id a webpage body')
