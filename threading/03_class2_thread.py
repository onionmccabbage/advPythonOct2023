from threading import Thread
import time
import random
from typing import Any

class MyClass: # implicitly inherits from object
    '''This class does not inherit from Thread
    In order for a class to be invoked as a thread we must provide a __call__ method
    '''
    def __call__(self, n): # __call__ lets us target this class from a Thread
        for i in range(1, 50):
            # print(f'{n} is sleeping')
            time.sleep(random.random()*0.1)

if __name__ == '__main__':
    start = time.time()
    c1 = MyClass() # just a normal instanceof a class
    # we can create a large quantity of threads
    my_threads_l = []
    # Very large quantities of threads will be restricted by
    # the limitations of the hardware and operating system
    for _ in range(0, 1024):
        my_threads_l.append(Thread(target=c1, args=(_,)))
    # we will start all the threads
    for item in my_threads_l:
        item.start()
    for item in my_threads_l:
        item.join() # careful - make sure all the threads are started before joining
    end = time.time()
    print(f'total time: {end-start}')