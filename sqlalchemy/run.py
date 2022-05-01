import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine, text
from sqlalchemy.orm import Session, declarative_base, sessionmaker


def table_exist(engine: sqlalchemy.engine.Engine, table_name: str) -> bool:
    """check table exsists on the database."""
    return sqlalchemy.inspect(engine).has_table(table_name)


# Database URLs: https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls
# [DIALECT]+[DRIVER]://[ID]:[PW]@[HOST]:[PORT]/[DATABASE]
URL = "postgresql+psycopg2://postgres:1234@localhost:5432/postgres"


# Create Engine
engine = create_engine(URL)


# Create TABLE `test_table` with Connection
table_name = "test_table"
with engine.connect() as conn:
    if not table_exist(engine, table_name):
        conn.execute(text(f"CREATE TABLE {table_name} (x int, y int)"))
    conn.execute(
        text(f"INSERT INTO {table_name} (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 2}],
    )


# Insert new row with Session
with Session(engine) as session:
    session.execute(
        text(f"INSERT INTO {table_name} (x, y) VALUES (:x, :y)"),
        [{"x": 3, "y": 3}, {"x": 4, "y": 4}],
    )
    session.commit()


# With Session, ORM-Mapped Class can be used.
Base = declarative_base()


class User(Base):
    """User ORM-Mappled Class."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"


Base.metadata.create_all(engine)  # CREATE TABLE users

with Session(engine) as session:
    david = User(name="David")
    john = User(name="John")

    session.add_all([david, john])

    session.commit()

"""
postgres=# SELECT * FROM users;
 id | name
----+-------
  1 | David
  2 | John
(2 rows)

"""


# make session with sessionmaker
# sessionmaker is "a configurable Session factory".
Session = sessionmaker(bind=engine)  # Session is sessionmaker
# print(type(Session))  # <class 'sqlalchemy.orm.session.sessionmaker'>

# option 1)
session = Session()  # invokes sessionmaker.__call__()
first_user = session.query(User).first()
print("first user is ", first_user)  # id: 1, name: David
session.close()

# option 2)  * recommended *
with Session() as session:
    first_user = session.query(User).first()
    print("first user is ", first_user)  # id: 1, name: David
