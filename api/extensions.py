import hashlib

from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

from api.settings import REDIS_HOST, REDIS_POST

db = SQLAlchemy()


def gen_md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode("utf-8"))
    return md5.hexdigest()


redis_store = StrictRedis(host=REDIS_HOST, port=REDIS_POST, decode_responses=True)
