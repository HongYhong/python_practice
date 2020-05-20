import time,threading

lock = threading.Lock()
balance = 0

def change(n):
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()
t1 = threading.Thread(target=run_thread,args = (5,))
t2 = threading.Thread(target=run_thread,args = (8,))

t1.start()
t2.start()
t1.join()
t2.join()

print(balance)