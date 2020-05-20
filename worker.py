#worker.py

from multiprocessing.managers import BaseManager 
import queue,time
from multiprocessing import freeze_support

class QueueManager(BaseManager):
    pass

def worker():
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    manager = QueueManager(address=('127.0.0.1',5000),authkey=b'abc')

    manager.connect()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('task:calculating %d*%d=...'%(n,n))
            r = '%d * %d = %d'%(n,n,n*n)
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print('the task queue is empty.')

    print('worker exit.')

if __name__ == "__main__":
    freeze_support()
    worker()



