from enum import unique, Enum

from sqlalchemy import Column

from api import db
from api.models.base import BaseModel, Model


@unique
class SmokeEnum(Enum):
    FAKE = '假冒烟'
    SMUGGLED = '走私烟'
    OTHER = '其他烟'


class Case(BaseModel, Model):
    __tablename__ = 'case'
    caseID = Column(db.String(128), comment='案件编号', nullable=False)
    caseCustomerCode = Column(db.ForeignKey('store.customerCode'), comment='客户编码', nullable=False)
    caseDate = Column(db.date(), comment='案发时间')
    caseValue = Column(db.DECIMAL(6, 2), comment='案值')
    count = Column(db.Integer, comment='卷烟数量（条数）', nullable=False)
    caseNature = Column(db.String(128), comment='案件性质')
    endDate = Column(db.date(), comment='结案日期')
    undertakeName = Column(db.String(128), comment='承办人')
    department = Column(db.String(128), comment='办案机关')
    caseAddress = Column(db.String(128), comment='案发地')
    addressPhoto = Column(db.String(200), comment='藏匿卷烟具体位置（图片')
    isCriminal = Column(db.Boolean(), server_default=db.text("False"), comment="有无刑事处罚，True有 False没有", index=True)
    smokeProperty = Column(db.Enum(SmokeEnum), comment='涉烟属性')


class Maketing(BaseModel, Model):
    __tablename__ = 'maketing'
    purchaseDate = Column(db.date(), comment='进货时间')
    purchaseWeek = Column(db.Integer, comment='周进货总量（条）')
    sellWeek = Column(db.Integer, comment='周销售总量（条）')
    inventoryRatio = Column(db.Integer, comment='周存销比')


class CodeSegment(BaseModel,Model):
    __tablename__ = 'codeSegment'
    segmentCustomerCode = Column(db.ForeignKey('store.customerCode'), comment='客户编码', nullable=False)
    outDate = Column(db.date(), comment='外流时间')
    outCount = Column(db.Integer, comment='外流条数（条）')






