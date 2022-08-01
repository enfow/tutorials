import os
import time
import celery

from common_task.tasks import add, sleep_three
from db import *


CELERY_RESULT_BACKEND = os.getenv(
    "CELERY_RESULT_BACKEND",
    "rpc://"
)
CELERY_BROKER_URL = os.getenv(
    "CELERY_BROKER_URL",
    "amqp://guest:guest@localhost:5672"  # for local
)
QUEUE = os.getenv(
    "QUEUE",
    "celery-worker"  # for local
)
POSTGRES_URL = os.getenv(
    "POSTGRES_URL",
    "postgres:1234@localhost:5432/postgres"
)

print("########################################")
print("CELERY BROKER_URL: ", CELERY_BROKER_URL)
print("TASK QUEUE NAME: ", QUEUE)
print("CELERY BACKEND: ", CELERY_RESULT_BACKEND)
print("POSTGRES_URL: ", POSTGRES_URL)
print("########################################")

app = celery.Celery(
    "celery-app-name",
    backend=CELERY_RESULT_BACKEND,
    broker=CELERY_BROKER_URL,
    include=["common_task"]
)

def add_wrapper(x, y):
    return add.apply_async(
        args=[x, y],
        queue=QUEUE,
        ignore_result=True,  # never wait result
    )

if __name__ == "__main__":
    print("START")

    pg_conn_info = postgres_url_parser(pg_url=POSTGRES_URL)
    conn = create_connection(
        # **pg_conn_info
    )

    while True:
        for count in range(1,4):  # count 3
            time.sleep(1)
            print(count)
        print("BAMMM💣💣💣💣💣")
        result = add_wrapper(1,2)
        print("RESULT: ", result.get())
