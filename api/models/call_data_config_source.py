from sqlalchemy import Column

from api import db
from api.models.base import BaseModel, Model


class DataSource(BaseModel, Model):
    __tablename__ = 'data_source'
    name = Column(db.String(200), comment='名称')
    operator = Column(db.String(200), comment='操作人')
