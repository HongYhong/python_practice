import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

if __name__ == "__main__":
    cpu_count = multiprocessing.cpu_count() * 2
    p = multiprocessing.Pool()
    for i in range(cpu_count):
        p.apply_async(loop)
    p.close()
    p.join()
    print('All subprocess are done.')