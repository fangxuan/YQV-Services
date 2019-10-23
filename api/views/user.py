from flask import Blueprint, request

from api.extensions import gen_md5
from api.models.user import Station, User
from api.schemas.user import user_login_schema
from api.serializer.user import user_info_ser
from api.views.base import common_response, SysStatus, render_data

blue_print = Blueprint('user', __name__, url_prefix='/api/v0/user')


@blue_print.route('/login', methods=['POST'])
def ycj_login():
    params = user_login_schema(request.json)
    account = params.get('account')
    password = params.get('password')

    data = User.query.filter(User.account == account, User.password == password).with_entities(*user_info_ser).first()

    if not data:
        return common_response(SysStatus.FAIL, None, '用户名密码不匹配')

    return common_response(SysStatus.SUCCESS, data, '成功')
