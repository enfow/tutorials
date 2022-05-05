"""runner for univiersity example."""

from model import Base

from sqlalchemy import create_engine
from config import LOCAL_POSTGRES_URL

engine = create_engine(url=LOCAL_POSTGRES_URL)

Base.metadata.create_all(engine)  # all tables are created.
