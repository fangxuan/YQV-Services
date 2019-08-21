from enum import unique, Enum

from sqlalchemy import Column

from api import db
from api.models.base import BaseModel, Model


@unique
class PlantStatus(Enum):
    HEALTHY = "健康"
    SICK = "生病"
    DEAD = "死亡"
    THIN = "缺肥"
    DRY = "缺水"
    RESET = "重新播种中"


@unique
class ItemType(Enum):
    SEED = "种子"
    FERTILIZER = "肥料"
    PESTICIDE = "药物"


class Plant(BaseModel, Model):
    __tablename__ = 'plant'
    name = Column(db.String(40), comment='名称')
    category = Column(db.String(40), comment='分类')
    needs = Column(db.String(40), comment='成长条件')
    active_flag = Column(db.Boolean(), server_default=db.text("True"), comment="是否启用，True启用 False不启用", index=True)
    seed_unit = Column(db.String(4), comment='种子单位')


class UserPlant(BaseModel, Model):
    __tablename__ = 'user_plant'
    plant_id = Column(db.ForeignKey('plant.id'), comment="植物id")
    user_id = Column(db.ForeignKey('user.id'), comment="用户id")
    active_flag = Column(db.Boolean(), server_default=db.text("True"), comment="是否启用，True启用 False不启用", index=True)
    water = Column(db.Integer(), comment='水分')
    fertilizer = Column(db.Integer(), comment='肥料')
    pesticide = Column(db.Integer(), comment='药')
    price = Column(db.Numeric(4, 2), comment='价值')
    harvest_at = Column(db.Date(), comment='预计收获时间')
    status = Column(db.Enum(PlantStatus), comment='状态')
    image = Column(db.String(1024), comment='图片')


class Seed(BaseModel, Model):
    __tablename__ = 'seed'
    plant_id = Column(db.ForeignKey('plant.id'), comment='植物id')
    category = Column(db.String(40), comment='分类')
    price = Column(db.Numeric(4, 2), comment='单位种子价格')
    unit = Column(db.String(4), comment='种子单位')
    time_cost = Column(db.String(40), comment='预计所需时间')
    area_need = Column(db.Integer(), comment='占地面积')
    area_unit = Column(db.String(40), comment='占地面积单位')


class Storage(BaseModel, Model):
    __tablename__ = 'storage'
    user_id = Column(db.ForeignKey('user.id'), comment='用户id')
    item_type = Column(db.Enum(ItemType), comment='物品类型')
    item_id = Column(db.ForeignKey('seed.id'), comment='物品ou o')
    quantity = Column(db.Integer(), comment='数量')


class UserPlantCoin(BaseModel, Model):
    __tablename__ = 'user_plant_coin'
    user_id = Column(db.ForeignKey('user.id'), comment='用户')
    coin = Column(db.Integer(), comment='金币')


class Fertilizer(BaseModel, Model):
    __tablename__ = 'fertilizer'
    name = Column(db.String(40), comment='名称')
    category = Column(db.String(40), comment='分类')
    price = Column(db.Numeric(4, 2), comment='单位价格')
    unit = Column(db.String(4), comment='单位')


class Pesticide(BaseModel, Model):
    __tablename__ = 'pesticide'
    name = Column(db.String(40), comment='名称')
    category = Column(db.String(40), comment='分类')
    price = Column(db.Numeric(4, 2), comment='单位价格')
    unit = Column(db.String(4), comment='单位')
