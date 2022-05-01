"""Define batabase model for university example."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Student(Base):
    """Model for student table."""

    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String(36))
    dept_name = Column(String(36))
    tot_cred = Column(Integer)
