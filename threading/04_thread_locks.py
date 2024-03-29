import threading
import time
import random

# All threads for a particular execution share the same resources
# There is ONE copy of Python, ONE set of data (memory, DB, I/O etc)
# Each threead has its own heap of memory once running
# we an lock shared resources to make them 'thread safe'

counter = 1
lock = threading.Lock() # we can use this to lock access to resources

def workerA():
    'this worker will access a global counter to increment it'
    global counter # we now have access to the global asset
    lock.acquire() # we now have exclusive access to the lock
    try:
        while counter <10:
            counter += 1
            print(f'Worker A is incrementing the counter to {counter}')
    except Exception as e:
        print(f'Something went wrong {e}')
    finally:
        lock.release() # release so any other threads might use it

def workerB():
    'this worker will access a global counter to decrement it'
    global counter 
    lock.acquire() # we now have exclusive access to the lock
    try:
        while counter >-10:
            counter -= 1
            print(f'Worker B is decrementing the counter to {counter}')
    except Exception as e:
        print(f'Something went wrong {e}')
    finally:
        lock.release() # release so any other threads might use it

if __name__ == '__main__':
    # normally these will act procedurally (one after the other)
    # workerB()
    # workerA()
    # try with threads
    t1 = threading.Thread(target=workerA)
    t2 = threading.Thread(target=workerB)
    # both threads will try to alter the counter
    t1.start() # whichever thread starts first will get first dibs on the lock
    t2.start()
    t1.join()
    t2.join()