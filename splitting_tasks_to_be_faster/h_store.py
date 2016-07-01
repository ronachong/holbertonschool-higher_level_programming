import threading
import time
import random

class Store:
    lock = threading.Lock()
    def __init__(self, item_number, person_capacity):
        self.item_number = item_number
        self.person_capacity = person_capacity
        # create a semaphore which will block if a number of tasks equal to person_capacity acquire it
        self.semaphore = threading.BoundedSemaphore(person_capacity)

    def enter(self):
        # acquire semaphore to model person entering store
        self.semaphore.acquire()


    def buy(self):
        time.sleep(random.randrange(5,10))
        Store.lock.acquire()
        try:
            if self.item_number > 0:
                # have user buy the item
                self.item_number -= 1
                bought = True
            else:
                bought = False
        finally:
            Store.lock.release()
        # release semaphore to model person leaving store
        self.semaphore.release()
        return bought
