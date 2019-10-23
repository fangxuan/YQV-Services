from flask import Blueprint, request

from api.extensions import gen_md5
from api.models.user import Station, User
from api.schemas.user import user_login_schema
from api.views.base import common_response, SysStatus, render_data

blue_print = Blueprint('ycj', __name__, url_prefix='/api/v0/ycj')


@blue_print.route('/login', methods=['POST'])
def ycj_login():
    params = user_login_schema(request.json)
    phone = params.get('phone')
    password = params.get('password')

    data = User.query.filter(User.account == phone, User.password == password).first()

    if not data:
        return common_response(SysStatus.FAIL, None, '用户名密码不匹配')
    print(data.user_name)
    print("23432424")

    return common_response(SysStatus.SUCCESS, "2311", '成功')
