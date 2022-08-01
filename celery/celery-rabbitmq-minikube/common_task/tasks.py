import os
import time
import celery
import pika

# define shared tasks
@celery.shared_task(name="add")
def add(x, y):
    result = x + y

    return {
        "result": result,
        "worker": os.getpid()
    }


@celery.shared_task(name="sleep_three")
def sleep_three():
    time.sleep(3)
    return True

def insert_to_queue(queue: str, data: dict)
    # connection
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
    )
    channel = connection.channel()
    channel.basic_publish(
        exchange='',
        routing_key=queue,
        body=b'Test message.'
    )
    connection.close()
