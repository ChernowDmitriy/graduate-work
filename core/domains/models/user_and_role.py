import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from infrastructures.database import ORMBaseModel


class User(ORMBaseModel):

    __tablename__ = 'users'

    email = sa.Column(sa.String, nullable=False)
    password = sa.Column(sa.String, nullable=False)

    first_name = sa.Column(sa.String, nullable=False)
    last_name = sa.Column(sa.String, nullable=False)
    middle_name = sa.Column(sa.String)
    age = sa.Column(sa.SmallInteger, nullable=False)
    birthdate = sa.Column(sa.Date)
    city = sa.Column(sa.String, nullable=False)

    is_active = sa.Column(sa.Boolean, default=True)


class Role(ORMBaseModel):
    __tablename__ = 'roles'

    name = sa.Column(sa.String, nullable=False)


class UserRole(ORMBaseModel):
    __tablename__ = 'user_role'

    user_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = relationship('User', backref='UserRole')

    role_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey('roles.id', ondelete='CASCADE'), nullable=False)
    role = relationship('Role', backref='UserRole')
