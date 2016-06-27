import threading
sumx = 0

class Sum:
    lock = threading.Lock()
    
    def __init__(self, nb_threads, numbers):
        if type(nb_threads) != int: raise Exception("nb_threads is not an integer")
        check_type(numbers)
        self.numbers = numbers
        
        # Sum instance calculates sum with nb_threads number of threads.
        global sumx
        sumx = 0
        subset_size = len(numbers)/nb_threads
        index1 = 0
        index2 = subset_size
        
        for x in range(nb_threads):
            if x == range(nb_threads)[-1]: index2 += len(numbers) - index2
            subset = self.numbers[index1:index2]
            thread = SumThread(subset)
            thread.start()
            index1 += subset_size
            index2 += subset_size

        
    def isComputing(self):
        if threading.active_count() != 1: return True
        # else
        return False

    def __str__(self):
        global sumx
        return str(sumx)

class SumThread(threading.Thread):
    def __init__(self, numbers):
        check_type(numbers)
        threading.Thread.__init__(self)
        self.numbers = numbers
        
    def run(self):
        global sumx
        Sum.lock.acquire()
        for x in self.numbers:
            sumx += x
        Sum.lock.release()
            
def check_type(numbers):
    if type(numbers) != list: raise Exception("numbers is not an array of integers")
    for number in numbers:
        if type(number) != int:
            raise Exception("numbers is not an array of integers")
