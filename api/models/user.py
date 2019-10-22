from enum import unique, Enum

from sqlalchemy import Column

from api import db
from api.models.base import BaseModel, Model


@unique
class PermissionEnum(Enum):
    ADMIN = '超级管理员'
    STATION_ADMIN = '局长'
    USER = '普通用户'


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


# 局表
class Station(BaseModel, Model):
    __tablename__ = 'station'
    station_name = Column(db.String(50), comment='局名称')


# 部门表
class Department(BaseModel, Model):
    __tablename__ = 'department'
    depart_name = Column(db.String(50), comment='部门名称')
    station_id = Column(db.ForeignKey('station.id'), comment='局id', nullable=False)


# 用户表
class UserY(BaseModel, Model):
    __tablename__ = 'user_y'
    account = Column(db.String(64), comment='账户', nullable=False)
    user_name = Column(db.String(50), comment='真实姓名')
    password = Column(db.String(128), comment='密码', nullable=False)
    department_id = Column(db.ForeignKey('department.id'), comment='部门id', nullable=False)
    permission_id = Column(db.ForeignKey('permission_y.id'), comment='权限id')


# 权限表
class Permission(BaseModel, Model):
    __tablename__ = 'permission_y'
    permi_name = Column(db.Enum(PermissionEnum), comment='权限名称')
