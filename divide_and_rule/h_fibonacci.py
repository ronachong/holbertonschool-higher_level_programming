import threading

class FibonacciThread(threading.Thread):    
    def __init__(self, number):
        threading.Thread.__init__(self)
        if type(number) != int: raise Exception("number is not an integer")
        self.__number = number
    
    def run(self):
        print str(self.__number) + ' => ' +  str(fibonacci2(self.__number))

def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    else: return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci2(n):
    fib = 0; a = 0; b = 1
    while n > 1:
        fib = a + b
        a = b; b = fib; n -= 1
    return fib
