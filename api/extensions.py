import functools
import hashlib

from flask import session, current_app
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

from api.settings import REDIS_HOST, REDIS_POST
from api.views.base import common_response, SysStatus

db = SQLAlchemy()


def gen_md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode("utf-8"))
    return md5.hexdigest()


redis_store = StrictRedis(host=REDIS_HOST, port=REDIS_POST, decode_responses=True)


# 将视图函数添加上该装饰器，就能获取到用户对象
def login_user_data(view_func):
    # 防止内层装饰器修改被装饰的函数的名字
    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):

        # 需求：
        # 获取session里面uers_id
        user = None

        user_id = session.get("user_id")
        if not user_id:
            user_id = 1  # TODO:方便测试，未登陆用户id为1，登陆状态为是True
            login = True
        # 根据user_id查询用户数据
        try:
            # 延迟导入 解决循环导入问题
            from api.models.user import User
            if user_id:
                user = User.query.get(user_id)
                if not user:
                    return common_response(SysStatus.FAIL, None, '请先登陆')
        except Exception as e:
            current_app.logger.error(e)
        # 3.保存数据后在view_func函数中能够获取到用户数据(*******)
        # g.user = user
        # 在进入实现函数里面由于是处于同一个request请求，里面就能够获取g对象中的临时变量
        result = view_func(user, **kwargs)
        return result

    return wrapper
