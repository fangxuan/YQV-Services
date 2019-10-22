"""empty message

Revision ID: 798b26ae283d
Revises: 755939bbc598
Create Date: 2019-10-16 22:25:01.225140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '798b26ae283d'
down_revision = '755939bbc598'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fertilizer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('category', sa.String(length=40), nullable=True),
    sa.Column('price', sa.Numeric(precision=4, scale=2), nullable=True),
    sa.Column('unit', sa.String(length=4), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('permission_y',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('name', sa.Enum('ADMIN', 'STATION_ADMIN', 'USER', name='permissionenum'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pesticide',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('category', sa.String(length=40), nullable=True),
    sa.Column('price', sa.Numeric(precision=4, scale=2), nullable=True),
    sa.Column('unit', sa.String(length=4), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('station',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('station_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['station_id'], ['station.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_y',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=False),
    sa.Column('permission_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.id'], ),
    sa.ForeignKeyConstraint(['permission_id'], ['permission_y.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('storage', sa.Column('item_type', sa.Enum('SEED', 'FERTILIZER', 'PESTICIDE', name='itemtype'), nullable=True))
    op.add_column('storage', sa.Column('quantity', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('money', sa.Numeric(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'money')
    op.drop_column('storage', 'quantity')
    op.drop_column('storage', 'item_type')
    op.drop_table('user_y')
    op.drop_table('department')
    op.drop_table('station')
    op.drop_table('pesticide')
    op.drop_table('permission_y')
    op.drop_table('fertilizer')
    # ### end Alembic commands ###
