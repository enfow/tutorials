from typing import List, Any

import psycopg2
from psycopg2 import OperationalError


def create_connection(
    db_name="postgres",
    db_user="postgres",
    db_password="1234",
    db_host="localhost",
    db_port="5432"
):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
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
