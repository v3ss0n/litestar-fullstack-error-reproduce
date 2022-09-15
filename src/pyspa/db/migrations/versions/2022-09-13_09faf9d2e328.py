# type: ignore
"""

Revision ID: 09faf9d2e328
Revises: 
Create Date: 2022-09-13 23:10:29.170333

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

from pyspa.db.db_types import GUID, EmailString, JsonObject, PydanticType, TimestampAwareDateTime


sa.GUID = GUID
sa.EmailString = EmailString
sa.JsonObject = JsonObject
sa.PydanticType = PydanticType
sa.TimestampAwareDateTime = TimestampAwareDateTime


sa.GUID = GUID 
sa.EmailString = EmailString
sa.JsonObject = JsonObject
sa.PydanticType = PydanticType
sa.TimestampAwareDateTime = TimestampAwareDateTime

# revision identifiers, used by Alembic.
revision = '09faf9d2e328'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team',
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('created_at', sa.TimestampAwareDateTime(timezone=True), server_default=sa.text('now()'), nullable=False, comment='Date the record was inserted'),
    sa.Column('updated_at', sa.TimestampAwareDateTime(timezone=True), nullable=True, comment='Date the record was last modified'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_team')),
    sa.UniqueConstraint('id', name=op.f('uq_team_id'))
    )
    op.create_index(op.f('ix_team_created_at'), 'team', ['created_at'], unique=False)
    op.create_index(op.f('ix_team_name'), 'team', ['name'], unique=False)
    op.create_index(op.f('ix_team_updated_at'), 'team', ['updated_at'], unique=False)
    op.create_table('user_account',
    sa.Column('full_name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.EmailString(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('created_at', sa.TimestampAwareDateTime(timezone=True), server_default=sa.text('now()'), nullable=False, comment='Date the record was inserted'),
    sa.Column('updated_at', sa.TimestampAwareDateTime(timezone=True), nullable=True, comment='Date the record was last modified'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user_account')),
    sa.UniqueConstraint('id', name=op.f('uq_user_account_id')),
    comment='User accounts for application access'
    )
    op.create_index(op.f('ix_user_account_created_at'), 'user_account', ['created_at'], unique=False)
    op.create_index(op.f('ix_user_account_email'), 'user_account', ['email'], unique=True)
    op.create_index(op.f('ix_user_account_updated_at'), 'user_account', ['updated_at'], unique=False)
    op.create_table('team_invitation',
    sa.Column('team_id', sa.GUID(), nullable=False),
    sa.Column('email', sa.EmailString(length=255), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=False),
    sa.Column('is_accepted', sa.Boolean(), nullable=True),
    sa.Column('invited_by_id', sa.GUID(), nullable=False),
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('created_at', sa.TimestampAwareDateTime(timezone=True), server_default=sa.text('now()'), nullable=False, comment='Date the record was inserted'),
    sa.Column('updated_at', sa.TimestampAwareDateTime(timezone=True), nullable=True, comment='Date the record was last modified'),
    sa.Column('expires_at', sa.TimestampAwareDateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['invited_by_id'], ['user_account.id'], name=op.f('fk_team_invitation_invited_by_id_user_account')),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], name=op.f('fk_team_invitation_team_id_team')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_team_invitation')),
    sa.UniqueConstraint('id', name=op.f('uq_team_invitation_id'))
    )
    op.create_index(op.f('ix_team_invitation_created_at'), 'team_invitation', ['created_at'], unique=False)
    op.create_index(op.f('ix_team_invitation_expires_at'), 'team_invitation', ['expires_at'], unique=False)
    op.create_index(op.f('ix_team_invitation_updated_at'), 'team_invitation', ['updated_at'], unique=False)
    op.create_table('team_member',
    sa.Column('user_id', sa.GUID(), nullable=False),
    sa.Column('team_id', sa.GUID(), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=False),
    sa.Column('is_owner', sa.Boolean(), nullable=False),
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('created_at', sa.TimestampAwareDateTime(timezone=True), server_default=sa.text('now()'), nullable=False, comment='Date the record was inserted'),
    sa.Column('updated_at', sa.TimestampAwareDateTime(timezone=True), nullable=True, comment='Date the record was last modified'),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], name=op.f('fk_team_member_team_id_team')),
    sa.ForeignKeyConstraint(['user_id'], ['user_account.id'], name=op.f('fk_team_member_user_id_user_account')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_team_member')),
    sa.UniqueConstraint('id', name=op.f('uq_team_member_id')),
    sa.UniqueConstraint('user_id', 'team_id', name=op.f('uq_team_member_user_id'))
    )
    op.create_index(op.f('ix_team_member_created_at'), 'team_member', ['created_at'], unique=False)
    op.create_index(op.f('ix_team_member_role'), 'team_member', ['role'], unique=False)
    op.create_index(op.f('ix_team_member_updated_at'), 'team_member', ['updated_at'], unique=False)
    op.create_table('upload',
    sa.Column('file_name', sa.String(length=255), nullable=True),
    sa.Column('uploaded_by', sa.String(length=255), nullable=True),
    sa.Column('is_processed', sa.Boolean(), nullable=False),
    sa.Column('team_id', sa.GUID(), nullable=False),
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('created_at', sa.TimestampAwareDateTime(timezone=True), server_default=sa.text('now()'), nullable=False, comment='Date the record was inserted'),
    sa.Column('updated_at', sa.TimestampAwareDateTime(timezone=True), nullable=True, comment='Date the record was last modified'),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], name=op.f('fk_upload_team_id_team'), ondelete='cascade'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_upload')),
    sa.UniqueConstraint('id', name=op.f('uq_upload_id')),
    comment='Stores links to uploaded files'
    )
    op.create_index(op.f('ix_upload_created_at'), 'upload', ['created_at'], unique=False)
    op.create_index(op.f('ix_upload_file_name'), 'upload', ['file_name'], unique=False)
    op.create_index(op.f('ix_upload_is_processed'), 'upload', ['is_processed'], unique=False)
    op.create_index(op.f('ix_upload_updated_at'), 'upload', ['updated_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_upload_updated_at'), table_name='upload')
    op.drop_index(op.f('ix_upload_is_processed'), table_name='upload')
    op.drop_index(op.f('ix_upload_file_name'), table_name='upload')
    op.drop_index(op.f('ix_upload_created_at'), table_name='upload')
    op.drop_table('upload')
    op.drop_index(op.f('ix_team_member_updated_at'), table_name='team_member')
    op.drop_index(op.f('ix_team_member_role'), table_name='team_member')
    op.drop_index(op.f('ix_team_member_created_at'), table_name='team_member')
    op.drop_table('team_member')
    op.drop_index(op.f('ix_team_invitation_updated_at'), table_name='team_invitation')
    op.drop_index(op.f('ix_team_invitation_expires_at'), table_name='team_invitation')
    op.drop_index(op.f('ix_team_invitation_created_at'), table_name='team_invitation')
    op.drop_table('team_invitation')
    op.drop_index(op.f('ix_user_account_updated_at'), table_name='user_account')
    op.drop_index(op.f('ix_user_account_email'), table_name='user_account')
    op.drop_index(op.f('ix_user_account_created_at'), table_name='user_account')
    op.drop_table('user_account')
    op.drop_index(op.f('ix_team_updated_at'), table_name='team')
    op.drop_index(op.f('ix_team_name'), table_name='team')
    op.drop_index(op.f('ix_team_created_at'), table_name='team')
    op.drop_table('team')
    # ### end Alembic commands ###
