import threading

class ReverseStrThread(threading.Thread):
    lock = threading.Thread.lock()
    sentence = ""
    
    def __init__(self, word):
        if type(word) != str: raise Exception("word is not a string")
        threading.Thread.__init__(self)
        self.word = word

    def run(self):
        ReverseStrThread.lock.acquire()
        ReverseStrThread.sentence += self.word[::-1] + " "
        ReverseStrThread.lock.release()
