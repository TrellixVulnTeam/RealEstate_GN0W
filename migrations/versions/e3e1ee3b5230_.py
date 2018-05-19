"""empty message

Revision ID: e3e1ee3b5230
Revises: 
Create Date: 2018-04-09 10:47:25.382114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3e1ee3b5230'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_first_name'), 'users', ['first_name'], unique=False)
    op.create_index(op.f('ix_users_last_name'), 'users', ['last_name'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('houses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=60), nullable=True),
    sa.Column('house_num', sa.Integer(), nullable=True),
    sa.Column('area', sa.String(length=60), nullable=True),
    sa.Column('city', sa.String(length=60), nullable=True),
    sa.Column('room_cnt', sa.Integer(), nullable=True),
    sa.Column('bath_cnt', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('balcony', sa.Boolean(), nullable=True),
    sa.Column('utility', sa.Boolean(), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('house_num')
    )
    op.create_index(op.f('ix_houses_amount'), 'houses', ['amount'], unique=False)
    op.create_index(op.f('ix_houses_area'), 'houses', ['area'], unique=False)
    op.create_index(op.f('ix_houses_balcony'), 'houses', ['balcony'], unique=False)
    op.create_index(op.f('ix_houses_bath_cnt'), 'houses', ['bath_cnt'], unique=False)
    op.create_index(op.f('ix_houses_city'), 'houses', ['city'], unique=False)
    op.create_index(op.f('ix_houses_room_cnt'), 'houses', ['room_cnt'], unique=False)
    op.create_index(op.f('ix_houses_type'), 'houses', ['type'], unique=False)
    op.create_index(op.f('ix_houses_utility'), 'houses', ['utility'], unique=False)
    op.create_table('sites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=60), nullable=True),
    sa.Column('site_num', sa.Integer(), nullable=True),
    sa.Column('area', sa.String(length=60), nullable=True),
    sa.Column('city', sa.String(length=60), nullable=True),
    sa.Column('sq_feet', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('site_num')
    )
    op.create_index(op.f('ix_sites_amount'), 'sites', ['amount'], unique=False)
    op.create_index(op.f('ix_sites_area'), 'sites', ['area'], unique=False)
    op.create_index(op.f('ix_sites_city'), 'sites', ['city'], unique=False)
    op.create_index(op.f('ix_sites_sq_feet'), 'sites', ['sq_feet'], unique=False)
    op.create_index(op.f('ix_sites_type'), 'sites', ['type'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sites_type'), table_name='sites')
    op.drop_index(op.f('ix_sites_sq_feet'), table_name='sites')
    op.drop_index(op.f('ix_sites_city'), table_name='sites')
    op.drop_index(op.f('ix_sites_area'), table_name='sites')
    op.drop_index(op.f('ix_sites_amount'), table_name='sites')
    op.drop_table('sites')
    op.drop_index(op.f('ix_houses_utility'), table_name='houses')
    op.drop_index(op.f('ix_houses_type'), table_name='houses')
    op.drop_index(op.f('ix_houses_room_cnt'), table_name='houses')
    op.drop_index(op.f('ix_houses_city'), table_name='houses')
    op.drop_index(op.f('ix_houses_bath_cnt'), table_name='houses')
    op.drop_index(op.f('ix_houses_balcony'), table_name='houses')
    op.drop_index(op.f('ix_houses_area'), table_name='houses')
    op.drop_index(op.f('ix_houses_amount'), table_name='houses')
    op.drop_table('houses')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_last_name'), table_name='users')
    op.drop_index(op.f('ix_users_first_name'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
