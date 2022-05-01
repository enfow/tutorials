"""runner for univiersity example."""

from sqlalchemy import create_engine

from model import Base

LOCAL_POSTGRES_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/postgres"

engine = create_engine(url=LOCAL_POSTGRES_URL)

Base.metadata.create_all(engine)
