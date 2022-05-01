"""runner for univiersity example."""

from model import Base

from sqlalchemy import create_engine

LOCAL_POSTGRES_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/postgres"

engine = create_engine(url=LOCAL_POSTGRES_URL)

Base.metadata.create_all(engine)  # all tables are created.
