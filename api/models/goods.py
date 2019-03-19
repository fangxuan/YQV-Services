from flask_sqlalchemy import Model
from sqlalchemy import Column

from api import db
from api.models.base import BaseModel



class Goods(BaseModel, Model):
    __tablename__ = 'goods'
    name = Column(db.String(50), comment='商品名')
    category = Column(db.String(50), comment='分类')
    price = Column(db.DECIMAL(6, 2), comment='价格')
    thumbnail = Column(db.String(20), comment='缩略图')
    detail = Column(db.String(50), comment='详情')




