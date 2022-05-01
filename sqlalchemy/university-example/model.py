"""Define batabase model for university example.

Notes:
    - all `id`s are integer.
"""

from sqlalchemy import Column, Integer, String, Date, Time
from sqlalchemy.orm import declarative_base
from sqlalchemy.schema import PrimaryKeyConstraint

Base = declarative_base()


class Student(Base):
    """Model for student table."""

    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String(36))
    dept_name = Column(String(36))
    tot_cred = Column(Integer)


class Department(Base):
    """Model for department table."""

    __tablename__ = "department"

    dept_name = Column(String(36), primary_key=True)
    building = Column(String(36))
    budget = Column(Integer)


class Instructor(Base):
    """Model for instructor table."""

    __tablename__ = "instructor"

    id = Column(Integer, primary_key=True)
    name = Column(String(36))
    dept_name = Column(String(36))
    salary = Column(Integer)


class Advisor(Base):
    """Model for advisor table.

    Notes:
        - It maps student id and instructor id.
        - If there are multi primary keys, declare it multiple times.
    """

    __tablename__ = "advisor"

    s_id = Column(Integer, primary_key=True)  # student id
    i_id = Column(Integer, primary_key=True)  # instructor id


class Takes(Base):
    """Model for takes table.

    Notes:
        - Add primary key constraint directly is possible.
    """

    __tablename__ = "takes"

    id = Column(Integer)
    course_id = Column(Integer)
    sec_id = Column(Integer)
    semester = Column(String(8))
    year = Column(Integer)
    grade = Column(String(8))  # A+, A, B+, B, ...

    # Add primary key constraint directly
    __table_args__ = (
        PrimaryKeyConstraint(id, course_id, sec_id, semester, year),
        {},
    )


class Section(Base):
    """Model for section table."""

    __tablename__ = "section"

    course_id = Column(Integer, primary_key=True)
    sec_id = Column(Integer, primary_key=True)
    semester = Column(String(8), primary_key=True)
    year = Column(Integer, primary_key=True)
    building = Column(String(32))
    room_no = Column(Integer)
    time_solot_id = Column(Integer)


class Teaches(Base):
    """Model for teacher table."""

    __tablename__ = "teaches"

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, primary_key=True)
    sec_id = Column(Integer, primary_key=True)
    semester = Column(String(8), primary_key=True)
    year = Column(Integer, primary_key=True)


class ClassRoom(Base):
    """Model for classroom table."""

    __tablename__ = "classroom"

    building = Column(String(32), primary_key=True)
    room_no = Column(Integer, primary_key=True)
    capacity = Column(Integer)


class TimeSlot(Base):
    """Model for timeslot table."""

    __tablename__ = "timeslot"

    time_solot_id = Column(Integer, primary_key=True)
    day = Column(Date, primary_key=True)
    start_time = Column(Time, primary_key=True)
    end_time = Column(Time)


class Course(Base):
    """Model for course table."""

    __tablename__ = "course"

    course_id = Column(Integer, primary_key=True)
    title = Column(String)
    dept_name = Column(String(36))
    credits = Column(Integer)


class Prereq(Base):
    """Model for prereq table."""

    __tablename__ = "prereq"

    course_id = Column(Integer, primary_key=True)
    prereq_id = Column(Integer, primary_key=True)
