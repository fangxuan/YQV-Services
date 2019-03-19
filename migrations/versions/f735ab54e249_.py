"""empty message

Revision ID: f735ab54e249
Revises: dd589e9b5286
Create Date: 2019-03-19 16:55:34.160224

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f735ab54e249'
down_revision = 'dd589e9b5286'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_table('article')
    op.drop_table('article_catalog')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article_catalog',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True, comment='创建时间'),
    sa.Column('updated_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True, comment='修改时间'),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=True, comment='分类名称'),
    sa.Column('valid', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True, comment='有效性'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('article',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True, comment='创建时间'),
    sa.Column('updated_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True, comment='修改时间'),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='发布者id'),
    sa.Column('title', mysql.VARCHAR(length=50), nullable=True, comment='标题'),
    sa.Column('content', mysql.VARCHAR(length=5000), nullable=True, comment='内容'),
    sa.Column('category', mysql.VARCHAR(length=20), nullable=True, comment='分类'),
    sa.Column('valid', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True, comment='有效性'),
    sa.Column('clicks', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='点击量'),
    sa.Column('likes', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='点赞量'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='article_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('comment',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True, comment='创建时间'),
    sa.Column('updated_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True, comment='修改时间'),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='用户id'),
    sa.Column('content', mysql.VARCHAR(length=200), nullable=True, comment='评论内容'),
    sa.Column('article_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='所属内容ID'),
    sa.Column('father_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True, comment='父评论ID'),
    sa.Column('valid', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True, comment='有效性'),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], name='comment_ibfk_1'),
    sa.ForeignKeyConstraint(['father_id'], ['comment.id'], name='comment_ibfk_2'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='comment_ibfk_3'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
