"""Define batabase model for university example.

Notes:
    - all column with surfix `id` are integer.
    - all column with surfix `name` are string.
"""

from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table, Time
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.schema import (ForeignKeyConstraint, PrimaryKeyConstraint,
                               UniqueConstraint)

Base = declarative_base()


class Student(Base):
    """Model for student table.

    Notes:
        - ForeignKey([table_name].[column_name])
        - relationship([ClassName], backref=[table_name])
    """

    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String(36))
    dept_name = Column(String(36), ForeignKey("department.dept_name"))
    tot_cred = Column(Integer)

    # relationship
    takes = relationship("Takes", backref="student")
    takes = relationship("Advisor", backref="student")


class Department(Base):
    """Model for department table."""

    __tablename__ = "department"

    dept_name = Column(String(36), primary_key=True)
    building = Column(String(36))
    budget = Column(Integer)

    # relationship
    student = relationship("Student", backref="department")
    course = relationship("Course", backref="department")
    instructor = relationship("Instructor", backref="department")


class Instructor(Base):
    """Model for instructor table."""

    __tablename__ = "instructor"

    id = Column(Integer, primary_key=True)
    name = Column(String(36))
    dept_name = Column(String(36), ForeignKey("department.dept_name"))
    salary = Column(Integer)

    # relationship
    advisor = relationship("Advisor", backref="instructor")
    teaches = relationship("Teaches", backref="instructor")


class Advisor(Base):
    """Model for advisor table.

    Notes:
        - It maps student id and instructor id.
        - If there are multi primary keys, declare it multiple times.
    """

    __tablename__ = "advisor"

    s_id = Column(Integer, ForeignKey("student.id"), primary_key=True)  # student id
    i_id = Column(
        Integer, ForeignKey("instructor.id"), primary_key=True
    )  # instructor id


class Takes(Base):
    """Model for takes table.

    Notes:
        - Add primary key constraint directly is possible.
    """

    __tablename__ = "takes"

    id = Column(Integer, ForeignKey("student.id"))
    course_id = Column(Integer)
    sec_id = Column(Integer)
    semester = Column(String(8))
    year = Column(Integer)
    grade = Column(String(8))  # A+, A, B+, B, ...

    # Add primary key constraint directly
    __table_args__ = (
        PrimaryKeyConstraint(id, course_id, sec_id, semester, year),
        ForeignKeyConstraint(
            ["course_id", "sec_id", "semester", "year"],
            ["section.course_id", "section.sec_id", "section.semester", "section.year"],
        ),
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
    time_slot_id = Column(Integer, ForeignKey("time_slot.time_slot_id"))

    # relationship
    takes = relationship("Takes", backref="section")
    teaches = relationship("Teaches", backref="section")

    # add unique constraint(ForeignKey)
    __table_args__ = (
        ForeignKeyConstraint(
            ["building", "room_no"], ["classroom.building", "classroom.room_no"]
        ),
        UniqueConstraint(building, room_no),
    )


class TimeSlot(Base):
    """Model for time_slot table."""

    __tablename__ = "time_slot"

    time_slot_id = Column(Integer, unique=True, primary_key=True)
    day = Column(Date, primary_key=True)
    start_time = Column(Time, primary_key=True)
    end_time = Column(Time)

    section = relationship("Section", backref="tiem_slot")


class Teaches(Base):
    """Model for teacher table."""

    __tablename__ = "teaches"

    id = Column(Integer, ForeignKey("instructor.id"), primary_key=True)
    course_id = Column(Integer, primary_key=True)
    sec_id = Column(Integer, primary_key=True)
    semester = Column(String(8), primary_key=True)
    year = Column(Integer, primary_key=True)

    # add unique constraint(ForeignKey)
    __table_args__ = (
        ForeignKeyConstraint(
            ["course_id", "sec_id", "semester", "year"],
            ["section.course_id", "section.sec_id", "section.semester", "section.year"],
        ),
    )


class ClassRoom(Base):
    """Model for classroom table."""

    __tablename__ = "classroom"

    building = Column(String(32), primary_key=True)
    room_no = Column(Integer, primary_key=True)
    capacity = Column(Integer)

    section = relationship("Section", backref="classroom")


class Course(Base):
    """Model for course table."""

    __tablename__ = "course"

    course_id = Column(Integer, primary_key=True)
    title = Column(String)
    dept_name = Column(String(36), ForeignKey("department.dept_name"))
    credits = Column(Integer)

    # relationship
    prereq = relationship("Prereq", backref="course")


class Prereq(Base):
    """Model for prereq table."""

    __tablename__ = "prereq"

    course_id = Column(Integer, ForeignKey("course.course_id"), primary_key=True)
    prereq_id = Column(Integer, ForeignKey("course.course_id"), primary_key=True)
