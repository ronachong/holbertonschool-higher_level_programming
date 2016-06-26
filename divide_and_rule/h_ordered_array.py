import threading

class OrderedArray:
    list = []
    lock = threading.Lock()
    
    def __init__(self):
        pass

    def add(self, number):
        if type(number) != int: raise Exception("number is not an integer")
        thread = OrderedArrayThread(number)
        thread.start()

    def isSorting(self):
        if threading.active_count() != 1: return True
        #else
        return False

    def __str__(self):
        return str(OrderedArray.list)


class OrderedArrayThread(threading.Thread):
    def __init__(self, number):
        if type(number) != int: raise Exception("number is not an integer")
        threading.Thread.__init__(self)
        self.number = number

    def run(self):
        OrderedArray.lock.acquire()
        i = 0
        for x in OrderedArray.list:
            if x > self.number:
                OrderedArray.list.insert(i, self.number)
                OrderedArray.lock.release()
                return
            i += 1

        # ELSE: all values in list were smaller, or there were no values; append at end.
        OrderedArray.list.append(self.number)
        OrderedArray.lock.release()

