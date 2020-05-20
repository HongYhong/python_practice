from multiprocessing import Process
import os

def run_proc(name):
    print('child process name:%s pid:%s'%(name,os.getpid()))

if __name__ == "__main__":
    print('parent process(%s) start...'%os.getpid())
    p = Process(target = run_proc,args = ('test',))
    print('child process will start...')
    p.start()
    print('child process end.')