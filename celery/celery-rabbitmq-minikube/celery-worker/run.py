import os
from celery import Celery
from celery.bin import worker

from common_task.tasks import add, sleep_three


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
    "celery-worker"
)

print("###############################")
print("BROKER_URL: ", CELERY_BROKER_URL)
print("QUEUE: ", QUEUE)
print("BACKEND: ", CELERY_RESULT_BACKEND)
print("###############################")
print()


def make_celery():
    return Celery(
        "worker-name",
        backend=CELERY_RESULT_BACKEND,
        broker=CELERY_BROKER_URL,
    )


if __name__ == "__main__":

    app = make_celery()
    app.autodiscover_tasks(packages=['common_task'])

    worker = app.Worker(
        include=["common_task"],
        loglevel="INFO",
        queues=QUEUE
    )
    worker.start()
