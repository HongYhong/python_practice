from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('task %s start...'%name)
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task %s runs %0.2f seconds'%(name,end - start))

if __name__ == "__main__":
    print('parent process(%s) start...'%os.getpid())
    p = Pool(8)
    for i in range(9):
        p.apply_async(long_time_task,args=(i,))
    p.close()
    p.join()
    print('All subprocess is done.')
