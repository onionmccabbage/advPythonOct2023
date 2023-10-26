# we will write a 'TicketSeller' class
# Several instances will then sell a discrete number of tickets
# we will report how many each ticket seller sold
# (or DB or file or API... any i/o bound operation)

import threading # we will need Thread and Lock
import sys
import time
import random

ticketsAvailable = 100

class TicketSeller(threading.Thread):
    ticketsSold = 0
    def __init__(self, lock): # we will allow each ticket seller access to the global lock
        threading.Thread.__init__(self)
        self.__lock = lock
        print('Ticket seller started selling tickets')
    def run(self):
        global ticketsAvailable # or a DB or file or....
        running = True
        while running:
            self.randomDelay() # pause for a moment
            self.__lock.acquire()
            if ticketsAvailable <=0:
                running = False
            else:
                ticketsAvailable -= 1
                self.ticketsSold += 1
                print(f'Sold a ticket, {ticketsAvailable} remaining')
            self.__lock.release() # pnly hang on to the lock for the shortest time
        print(f'Sold {self.ticketsSold}')
    def randomDelay(self):
        time.sleep(random.randint(0,4)/4) # 0, 0.25, 0.5 0.75

if __name__ == '__main__':
    lock = threading.Lock()
    sellers_l = []
    # we shoudl balance the likely numer of assets with the reasonable number of threads
    if len(sys.argv)>1:
        numThreads = int(float( sys.argv[1] ))
    else:
        numThreads = 4
    
    for _ in range(0, numThreads):
        seller = TicketSeller(lock)
        sellers_l.append(seller)
        seller.start()
    for s in sellers_l:
        s.join()