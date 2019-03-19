import hashlib

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def gen_md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode("utf-8"))
    return md5.hexdigest()
