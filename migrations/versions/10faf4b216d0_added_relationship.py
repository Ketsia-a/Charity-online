"""Added relationship

Revision ID: 10faf4b216d0
Revises: 85a6bc37561d
Create Date: 2020-12-16 13:15:41.124953

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '10faf4b216d0'
down_revision = '85a6bc37561d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('event_pic_path', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('category', sa.String(length=255), nullable=False),
    sa.Column('value', sa.String(length=255), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_events_category'), 'events', ['category'], unique=False)
    op.drop_index('ix_event_category', table_name='event')
    op.drop_table('event')
    op.add_column('donors', sa.Column('event_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'donors', 'events', ['event_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'donors', type_='foreignkey')
    op.drop_column('donors', 'event_id')
    op.create_table('event',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('event_pic_path', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('category', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('value', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='event_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='event_pkey')
    )
    op.create_index('ix_event_category', 'event', ['category'], unique=False)
    op.drop_index(op.f('ix_events_category'), table_name='events')
    op.drop_table('events')
    # ### end Alembic commands ###