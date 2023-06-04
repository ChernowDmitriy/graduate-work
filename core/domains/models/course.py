import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from infrastructures.database import ORMBaseModel


class Course(ORMBaseModel):
    __tablename__ = 'courses'

    name = sa.Column(sa.String)
    price = sa.Column(sa.Float)
    rating = sa.Column(sa.Float)
    description = sa.Column(sa.String)

    is_free = sa.Column(sa.Boolean, default=False)
    is_certified = sa.Column(sa.Boolean, default=False)
    image = sa.Column(sa.String)
    text = sa.Column(sa.String)


class CourseCreator(ORMBaseModel):
    __tablename__ = 'course_creator'

    course_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey('courses.id', ondelete='CASCADE'))
    course = relationship('Course', backref='CourseCreator')

    author_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey('authors.id', ondelete='CASCADE'))
    author = relationship('Author', backref='CourseCreator')


class UserCourse(ORMBaseModel):
    __tablename__ = 'user_course'

    student_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey('students.id', ondelete='CASCADE'))
    student = relationship('Student', backref='UserCourse')

    course_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey('courses.id', ondelete='CASCADE'))
    course = relationship('Course', backref='UserCourse')

    is_favorite = sa.Column(sa.Boolean, default=False)
    is_bought = sa.Column(sa.Boolean, default=False)
    is_archive = sa.Column(sa.Boolean, default=False)
