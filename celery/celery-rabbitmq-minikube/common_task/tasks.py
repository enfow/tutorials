import os
import time
import celery

# define shared tasks
@celery.shared_task(name="add")
def add(x, y):
    result = x + y
    return result


@celery.shared_task(name="sleep_three")
def sleep_three():
    time.sleep(3)
    return True
