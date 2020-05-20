#task_master.py

from multiprocessing.managers import BaseManager,queue

from multiprocessing import freeze_support

import random,time

task_quene = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

def gettask():
    return task_quene

def getresult():
    return result_queue

def taskmaster():
    QueueManager.register('get_task_queue',callable=gettask)
    QueueManager.register('get_result_queue',callable=getresult)

    manager = QueueManager(address=('127.0.0.1',5000),authkey=b'abc')

    manager.start()

    task = manager.get_task_queue()

    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0,1000)
        print('put task %d'%n)
        task.put(n)

    for i in range(10):
        r = result.get(timeout=10)
        print('result is %s'%r)

    manager.shutdown()
    print('master quit.')

if __name__ == '__main__':
    freeze_support()
    taskmaster()