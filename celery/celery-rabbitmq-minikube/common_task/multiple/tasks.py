import os
import time
import celery

# define shared tasks
@celery.shared_task(name="multiple")
def multiple(x, y):
    result = x * y
    return result
