from __future__ import absolute_import, unicode_literals

from celery import shared_task


# @shared_task
# def create_task(task_type):
#     time.sleep(int(task_type) * 10)
#     return True

@shared_task
def add(x,y):
    return x+y