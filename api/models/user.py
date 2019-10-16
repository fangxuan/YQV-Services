from sqlalchemy import Column

from api import db
from api.models.base import BaseModel, Model


class User(BaseModel, Model):
    __tablename__ = 'user'
    name = Column(db.String(50), comment='用户名')
    password = Column(db.String(128), comment='密码')
    gender = Column(db.String(4), comment='性别')
    phone = Column(db.String(20), comment='手机号')
    email = Column(db.String(50), comment='邮箱')
    avatar = Column(db.String(128), comment='头像')
    birthday = Column(db.Date(), comment='生日')
    coin = Column(db.Integer, comment='积分')
    money = Column(db.Numeric, comment='XIN')


# class Permission(BaseModel, db.Model):
#     __tablename__ = 'permission'
#     user_id = Column(db.ForeignKey('user.id'), comment='用户id')
#     password = Column(db.String(128), comment='权限')
