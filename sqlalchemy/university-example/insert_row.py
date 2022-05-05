"""Insert default values to university database."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config import LOCAL_POSTGRES_URL
from model import Student

engine = create_engine(url=LOCAL_POSTGRES_URL)

with Session(engine) as session:
    david = Student(name="david", dept_name="political-science", tot_cred=19)
    session.add(david)
    session.commit()
