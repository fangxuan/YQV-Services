"""empty message

Revision ID: 755939bbc598
Revises: 93a7a49aed59
Create Date: 2019-08-13 09:41:02.656207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '755939bbc598'
down_revision = '93a7a49aed59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_plant_coin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True, comment='创建时间'),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True, comment='更新时间'),
    sa.Column('user_id', sa.Integer(), nullable=True, comment='用户'),
    sa.Column('coin', sa.Integer(), nullable=True, comment='金币'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('storage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True, comment='创建时间'),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True, comment='更新时间'),
    sa.Column('user_id', sa.Integer(), nullable=True, comment='用户'),
    sa.Column('item_id', sa.Integer(), nullable=True, comment='物品ou o'),
    sa.ForeignKeyConstraint(['item_id'], ['seed.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('coin', sa.Integer(), nullable=True, comment='金币'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'coin')
    op.drop_table('storage')
    op.drop_table('user_plant_coin')
    # ### end Alembic commands ###
