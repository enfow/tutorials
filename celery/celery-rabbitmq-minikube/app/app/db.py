from typing import List, Any

import psycopg2
from psycopg2 import OperationalError


def postgres_url_parser(
    pg_url: str
):
    user_info, host_db_info = pg_url.split("@")
    user, passwd = user_info.split(":")
    host_info, database = host_db_info.split("/")
    host, port = host_info.split(":")

    return {
        "user": user,
        "password": passwd,
        "host": host,
        "port": port,
        "database": database,
    }


def create_connection(
    database="postgres",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
):
    connection = None
    try:
        connection = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def create_table_logs(conneciton):
    """cretae table logs.

    Notes:
        - Use hard coded table schema
    """

    # create table
    table_query = """
    CREATE TABLE IF NOT EXISTS logs (
      id SERIAL PRIMARY KEY,
      worker TEXT NOT NULL,
      result TEXT
    )
    """
    execute_query(conn, table_query)  # Query executed successfully


def insert_to_logs(connection, log: tuple):
    """
    example_log = ("worker-1", "3")
    """

    insert_query = (
        f"INSERT INTO logs (worker, result) VALUES {log}"
    )
    execute_query(connection, insert_query)


if __name__ == "__main__":

    # make connection
    conn = create_connection()
    # create table "logs"
    create_table_logs(conn)
    # insert example row to "logs"
    insert_to_logs(conn, log=("worker-1", "1"))
