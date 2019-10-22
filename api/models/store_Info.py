from enum import unique, Enum

from sqlalchemy import Column

from api import db
from api.models.base import BaseModel, Model


@unique
class StateEnum(Enum):
    NARMAL = '正常营业'
    CLOSE = '停业'
    REST = '歇业'


@unique
class BusinessFormatEnum(Enum):
    TOP = '高危(副食品店,烟酒商店,商场)'
    MIDDLE = '中(便利店,超市)'
    LOW = '低(娱乐服务类,其他)'


@unique
class AdminiEnum(Enum):
    BENJI = '本级'
    LANXI = '兰溪'
    PUJIANG = '浦江'
    YIWU = '义乌'
    DONGYANG = '东阳'
    PANAN = '磐安'
    YONGKANG = '永康'
    WUYI = '武义'


@unique
class MarketTypeEnum(Enum):
    COUNTRYSIDE = '农村'
    TOWNSHIP = '乡镇'
    COUNTRYTOWN = '县城城区'
    URBAN = '市区'


class Store(BaseModel, Model):
    __tablename__ = 'store'
    storeName = Column(db.String(128), comment='零售户名称', nullable=False)
    legalPerson = Column(db.String(50), comment='零售户法人姓名', nullable=False)
    personNumber = Column(db.String(18), comment='零售户法人身份证号', nullable=False)
    licenseNumber = Column(db.String(128), comment='营业执照号', nullable=False)
    customerCode = Column(db.String(128), comment='客户编码', nullable=False)
    photos = Column(db.String(200), comment='零售户照片')
    businessNumber = Column(db.String(200), comment='烟草经营许可证号', nullable=False)
    businessDate = Column(db.Date(), comment='烟草经营许可证发证日期')
    businessOffice = Column(db.String(200), comment='烟草经营许可证发证机关')
    businessState = Column(db.Boolean(), server_default=db.text("False"), comment="烟草经营许可证是否到期，True到期 False不到期",
                           index=True)
    businessTerm = Column(db.Date(), comment='烟草经营许可证期限', nullable=False)
    address = Column(db.String(200), comment='经营地址', nullable=False)
    state = Column(db.Enum(StateEnum), comment='经营状态', nullable=False)
    storeCategory = Column(db.String(20), comment='零售户合理定量类别', nullable=False)
    isChain = Column(db.Boolean(), server_default=db.text("False"), comment="是否连锁，True连锁 False不连锁", index=True)
    businessFormat = Column(db.Enum(BusinessFormatEnum), comment='经营业态', nullable=False)
    administrative = Column(db.Enum(AdminiEnum), comment='行政区划', nullable=False)
    marketType = Column(db.Enum(MarketTypeEnum), comment='市场类型')
    phoneFirst = Column(db.String(20), comment='主呼电话', nullable=False)
    phoneSecond = Column(db.String(20), comment='备呼电话')
    settlement = Column(db.String(200), comment='电子结算账号', nullable=False)
    circle = Column(db.Boolean(), server_default=db.text("False"), comment="是否敏感商圈，True敏感(商工住) False不敏感(文办混)",
                    index=True)
    isDowngrade = Column(db.Boolean(), server_default=db.text("False"), comment="是否有降级降档情况，True有 False没有", index=True)


class personInfo(BaseModel, Model):
    __tablename__ = 'personInfo'
    name = Column(db.String(20), comment='法人姓名', nullable=False)
    sex = Column(db.Boolean(), server_default=db.text("False"), comment="性别，True女 False男", index=True)
    idCard = Column(db.ForeignKey('store.personIdCard'), comment='法人身份证号')
    idAddress = Column(db.String(128), comment='身份证住址', nullable=False)
    birthday = Column(db.date(), comment='出生日期')
    nation = Column(db.String(128), comment='民族')
    censusRegister = Column(db.String(128), comment='户籍', nullable=False)
    phone = Column(db.String(128), comment='联系电话', nullable=False)
    addressNow = Column(db.String(128), comment='当前住址', nullable=False)
    levelEducation = Column(db.String(128), comment='文化程度')













