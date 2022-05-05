"""Define batabase model for university example.

Notes:
    - all column with surfix `id` are integer.
    - all column with surfix `name` are string.
"""

from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table, Time
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.schema import (
    ForeignKeyConstraint,
    PrimaryKeyConstraint,
    UniqueConstraint,
)

Base = declarative_base()


# Test 1: Student -> School
# ForeignKey 를 설정하면 해당 Row를 추가하기 전에 ForeignKey의 값이 존재해야 한다.


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String(36))
    grade = Column(Integer)
    school_name = Column(String(36), ForeignKey("school.name"))


class School(Base):
    __tablename__ = "school"

    name = Column(String(36), primary_key=True)
    address = Column(String(36))
    type = Column(String(36))

    student = relationship("Student", backref="school")


# Test 2: Guest -> Cafe -> Coffee
# - relationship의 존재 여부는 중요하지 않다.
# - relationship은 ForeignKey가 정의된 Class, ForeignKey가 가리키는 Class 모두에서 설정 가능하다.


class Guest(Base):
    __tablename__ = "guest"

    id = Column(Integer, primary_key=True)
    name = Column(String(36))
    cafe_name = Column(String(36), ForeignKey("cafe.name"))


class Cafe(Base):
    __tablename__ = "cafe"

    name = Column(String(36), primary_key=True)
    address = Column(String(36))
    coffee_name = Column(String(36), ForeignKey("coffee.name"))

    guests = relationship("Guest", backref="cafe")  # ForeignKey가 가리키는 Class
    coffees = relationship("Coffee", backref="cafe")  # ForeignKey가 존재하는 Class


class Coffee(Base):
    __tablename__ = "coffee"

    name = Column(String(36), primary_key=True)
    origin = Column(String(36))


# Test 3: Brewery ->  MaltWhisky   <- Farm
#         Bar     <- BlendedWhisky
# - Column 단위에서 개별적으로 ForeignKey를 설정하는 것과,  __table_args__ 에서
#       ForeignKeyConstraint를 설정하는 것은 서로 다르다.
#   - 하나씩 하면 개별적으로 Uniqueness가 보장되어야 한다.
#   - 복수의 Column에서 함께 Foreign Key를 설정하면 Uniqueness도 함께 보장되어야 한다.
#   - 다 같이 했을 때는 다 같이 Uniqueness가 보장되어야 한다. 하나가 Primary
#       key여도 다른 것에 같이 uniqueness가 없으면 안 된다.
#
# - relationship()을 사용할 때, 동일한 Table을 참조하는 경우에는 ForeignKey를 명시해야 한다.


class Brewery(Base):
    __tablename__ = "brewery"

    name = Column(String(36))
    location = Column(String(36))

    __table_args__ = (PrimaryKeyConstraint(name), UniqueConstraint("name", "location"))


class Master(Base):
    __tablename__ = "master"

    name = Column(String(36), primary_key=True)
    age = Column(Integer)


class MaltWhisky(Base):
    __tablename__ = "malt_whisky"

    # columns
    name = Column(String(36), primary_key=True)
    brewery_name = Column(String(36))
    brewery_location = Column(String(36))
    master_name = Column(String(36), ForeignKey("master.name"))
    # relationship
    brewery = relationship("Brewery", backref="malt_whisky")
    master = relationship("Master", backref="malt_whisky")
    bar = relationship("Bar", backref="malt_whisky")

    __table_args__ = (
        ForeignKeyConstraint(
            ["brewery_name", "brewery_location"], ["brewery.name", "brewery.location"]
        ),
    )


class BlendedWhisky(Base):
    __tablename__ = "blended_whisky"

    # columns
    name = Column(String(36), primary_key=True)
    brewery_name = Column(String(36))
    brewery_location = Column(String(36))
    master_name = Column(String(36), ForeignKey("master.name"))
    # additional columns
    sub_brewery_name = Column(String(36))
    sub_brewery_location = Column(String(36))

    # relationship
    # 두 개의 relation이 동일한 Table, Brewery를 참조하므로, ForeignKey를 명시한다.
    brewery = relationship(
        "Brewery",
        backref="blended_whisky",
        foreign_keys=[brewery_name, brewery_location],
    )
    sub_brewery = relationship(
        "Brewery",
        backref="sub_blended_whisky",
        foreign_keys=[sub_brewery_name, sub_brewery_location],
    )
    master = relationship("Master", backref="blended_whisky")
    bar = relationship("Bar", backref="blended_whisky")

    __table_args__ = (
        ForeignKeyConstraint(
            ["brewery_name", "brewery_location"],
            ["brewery.name", "brewery.location"],
        ),
        ForeignKeyConstraint(
            ["sub_brewery_name", "sub_brewery_location"],
            ["brewery.name", "brewery.location"],
        ),
    )


class Bar(Base):
    __tablename__ = "bar"

    name = Column(String(36), primary_key=True)
    malt_whisky_name = Column(String(36), ForeignKey("malt_whisky.name"))
    blended_whisky_name = Column(String(36), ForeignKey("blended_whisky.name"))
    location = Column(String(36))
