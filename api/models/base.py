from sqlalchemy import Column, func

from api import db


class BaseModel(object):
    __table_args__ = {'extend_existing': True}
    id = Column(db.Integer, primary_key=True)
    created_at = Column(db.DateTime, server_default=func.now(), comment='创建时间')
    updated_at = Column(db.DateTime, server_default=func.now(), server_onupdate=func.now(), comment='修改时间')
