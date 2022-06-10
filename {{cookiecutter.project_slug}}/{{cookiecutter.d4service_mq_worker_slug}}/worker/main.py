import os
from celery import Celery

celery = Celery(
    __name__,
    broker=os.getenv("D4SERVICE_MQ_URI"),
    backend=os.getenv("D4SERVICE_MQ_DB_URI")
)


@celery.on_after_configure.connect
def add_periodic(**kwargs):
    celery.add_periodic_task(30.0, worker.s('hello123'), name='add every 30')


@celery.task
def worker(mytext):
    import time
    time.sleep(15)
    return str(mytext) * 3
