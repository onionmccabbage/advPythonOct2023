from threading import Thread
import time
import timeit # timeit is a more accurate tool for masuring python times
import random

# Any python module can be profiled using cprofile
#                    -o is the output filename
# python -m cProfile -o profile_output 02_class_thread.py

# Thread is a means by which Python can access system threads
class MyClass(Thread):
    '''This class inherits from Thread. It can be invoked the same way as any Thread'''
    def __init__(self, n, t):
        Thread.__init__(self) # call the initializer of the parent class
        self.n = n # we could write get/set methods for n and t
        self.t = t
    # every Thread has a 'run' method that we can overwrite
    def run(self):
        '''When this (Thread) is invoked, thus run method will execute
        This makes the instance run on its own thread'''
        for i in range(0,10): # on average, half a second overall
            print(f'{self.n} is sleeping') # careful: printing takes significant time
            time.sleep(random.random()*0.1) # each iteration will be different

if __name__ == '__main__':
    # random.random()*0.1 will sleep between 0 and 0.1 second
    t1 = MyClass(1, 1) # this is effectively an instance of a Thread
    t2 = MyClass(2, 2) # this is effectively an instance of a Thread
    t3 = MyClass(3, 2) # this is effectively an instance of a Thread
    t4 = MyClass(4, 2) # this is effectively an instance of a Thread
    start = timeit.default_timer() # an accurate start time
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join() # this blocks the main thread until the sub thread joins back
    t2.join() 
    t3.join() 
    t4.join()
    end = timeit.default_timer() # timeit tries to eliminate time spent on non-python things
    print(f'Overall time was {end-start}')