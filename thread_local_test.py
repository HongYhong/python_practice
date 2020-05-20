#thread_local_test.py
'''
import threading

class Student(object):
    def __init__(self,name):
        self.name = name

def process_student(name):
    std = Student(name)
    do_task1(std)
    do_task2(std)

def do_task1(std):
    print('i am %s.'%std.name)

def do_task2(std):
    print('print name:%s'%std.name)

if __name__ == "__main__":
    t1 = threading.Thread(target=process_student,args=('hong',))
    t2 = threading.Thread(target=process_student,args=('lin',))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

'''
'''
#method 2:

import threading

class Student(object):
    def __init__(self,name):
        self.name = name

grobaldict = {}

def process_student(name):
    std = Student(name)
    grobaldict[threading.current_thread()] = std
    do_task1()
    do_task2()

def do_task1():
    std = grobaldict[threading.current_thread()]
    print('i am %s'%std.name)
def do_task2():
    std = grobaldict[threading.current_thread()]
    print('print name:%s'%std.name)

if __name__ == "__main__":
    t1 = threading.Thread(target = process_student,args=('hong',))
    t2 = threading.Thread(target = process_student,args=('lin',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

'''

#method 3
#Threadlocal

import threading

local_student = threading.local()

def process_thread(name):
    local_student.name = name
    process_student()

def process_student():
    name = local_student.name
    print('Thread:%s,name:%s'%(threading.current_thread(),name))

if __name__ == "__main__":
    t1 = threading.Thread(target=process_thread,args=('hong',))
    t2 = threading.Thread(target=process_thread,args=('len',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()