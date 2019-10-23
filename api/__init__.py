from flask import Flask
from flask_session import Session
from flask_wtf.csrf import CSRFProtect, generate_csrf
from api.extensions import db
from api.settings import DevConfig
from api.views import user


def create_app(env_config):
    app = Flask(__name__)
    app.config.from_object(env_config)
    # 懒加载，延迟加载
    db.init_app(app)

    # csrf = CSRFProtect(app)
    #
    # @app.after_request
    # def set_csrf_token(response):
    #     # 1. 生成csrf_token随机值
    #     csrf_token = generate_csrf()
    #     # 2.借助响应对象设置csrf_token到cookie中
    #     response.set_cookie("csrf_token", csrf_token)
    #     # 3.返回响应对象
    #     return response

    Session(app)

    # 注册视图
    app.register_blueprint(user.blue_print)
    return app
