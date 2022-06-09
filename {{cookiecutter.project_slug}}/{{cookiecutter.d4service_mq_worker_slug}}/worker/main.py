import os
from celery import Celery

celery = Celery(
    __name__,
    broker=os.getenv("D4SERVICE_MQ_URI"),
    backend=os.getenv("D4SERVICE_MQ_DB_URI")
)


@celery.task
def worker(mytext):
    import time
    time.sleep(15)
    return str(mytext) * 3
