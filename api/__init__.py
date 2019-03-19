from flask import Flask
from redis import StrictRedis
# from flask_session import Session
from api.extensions import db
from api.settings import DevConfig, REDIS_HOST, REDIS_POST
from api.views import user


def create_app(env_config):
    app = Flask(__name__)
    app.config.from_object(env_config)
    db.init_app(app)
    # csrf = CSRFProtect(app)
    # @app.after_request
    # def set_csrf_token(response):
    #     # 1. 生成csrf_token随机值
    #     csrf_token = generate_csrf()
    #     # 2.借助响应对象设置csrf_token到cookie中
    #     response.set_cookie("csrf_token", csrf_token)
    #     # 3.返回响应对象
    #     return response

    # Session(app)

    app.register_blueprint(user.blue_print)
    return app


redis_store = StrictRedis(host=REDIS_HOST, port=REDIS_POST, decode_responses=True)
