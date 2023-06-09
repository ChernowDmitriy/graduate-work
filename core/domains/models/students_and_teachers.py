import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from infrastructures.database import ORMBaseModel


class Student(ORMBaseModel):
    __tablename__ = 'students'

    user_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = relationship('User', backref='Student')


class Teacher(ORMBaseModel):
    __tablename__ = 'teachers'

    user_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey('users.id'))
    user = relationship('User', backref='Teacher')
