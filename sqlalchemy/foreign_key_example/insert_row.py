"""Insert default values to university database."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config import LOCAL_POSTGRES_URL
from model import *

engine = create_engine(url=LOCAL_POSTGRES_URL)

with Session(engine) as session:
    # test 1
    sin_an = School(name="sin-an", address="jinju-si", type="elementary")

    woo = Student(
        name="woo",
        grade=4,
        school_name="sin-an",
    )

    session.add(sin_an)
    session.commit()
    session.add(woo)
    session.commit()

    # test 2
    coffee = Coffee(name="AA", origin="kenya")
    cafe = Cafe(
        name="starbucks",
        address="seattle",
        coffee_name="AA",
    )
    guest = Guest(name="Obama", cafe_name="starbucks")

    # [Error]
    # session.add_all([
    #     coffee, cafe, guest
    # ])

    session.add(coffee)
    session.commit()
    session.add(cafe)
    session.commit()
    session.add(guest)
    session.commit()

    # test 3
    brewery = Brewery(name="balvenie", location="speyside")
    sub_brewery = Brewery(name="glenlivet", location="speyside")
    master1 = Master(
        name="david stewart",
        age=60,
    )
    master2 = Master(
        name="blended_master",
        age=60,
    )
    malt_whisky = MaltWhisky(
        name="balvenie", brewery_name="balvenie", master_name="david stewart"
    )
    blended_whisky = BlendedWhisky(
        name="blended",
        brewery_name="balvenie",
        sub_brewery_name="glenlivet",
        master_name="blended_master",
    )
    bar = Bar(
        name="drink",
        malt_whisky_name="balvenie",
        blended_whisky_name="blended",
        location="seoul",
    )
    session.add_all([brewery, sub_brewery])
    session.commit()
    session.add(master1)
    session.add(master2)
    session.commit()
    session.add(malt_whisky)
    session.add(blended_whisky)
    session.commit()
    session.add(bar)
    session.commit()
