from threading import Thread
import time
import random

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
            print(f'{self.n} us sleeping for {self.t}')
            time.sleep(self.t)

if __name__ == '__main__':
    # random.random()*0.1 will sleep between 0 and 0.1 second
    t1 = MyClass(1, random.random()*0.1) # this is effectively an instance of a Thread
    start = time.time()
    t1.start()

    end = time.time()
    print(f'Overall time was {end-start}')