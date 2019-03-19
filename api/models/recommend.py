from sqlalchemy import Column

from api import db
from api.models.base import BaseModel


class Article(BaseModel, db.Model):
    __tablename__ = 'article'
    user_id = Column(db.ForeignKey('user.id'), comment='发布者id')
    title = Column(db.String(50), comment='标题')
    content = Column(db.String(5000), comment='内容')
    category = Column(db.String(20), comment='分类')
    valid = Column(db.Boolean(), comment='有效性')
    clicks = Column(db.Integer(), comment='点击量')
    likes = Column(db.Integer(), comment='点赞量')


class ArticleCatalog(BaseModel, db.Model):
    __tablename__ = 'article_catalog'
    name = Column(db.String(50), comment='分类名称')
    valid = Column(db.Boolean(), comment='有效性')


class Comment(BaseModel, db.Model):
    __tablename__ = 'comment'
    user_id = Column(db.ForeignKey('user.id'), comment='用户id')
    content = Column(db.String(200), comment='评论内容')
    article_id = Column(db.ForeignKey('article.id'), comment='所属内容ID')
    father_id = Column(db.ForeignKey('comment.id'), comment='父评论ID')
    valid = Column(db.Boolean(), comment='有效性')
