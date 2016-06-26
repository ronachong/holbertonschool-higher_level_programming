import threading

class ReverseStrThread(threading.Thread):
    sentence = ""
    
    def __init__(self, word):
        if type(word) != str: raise Exception("word is not a string")
        threading.Thread.__init__(self)
        self.word = word

    def run(self):
        ReverseStrThread.sentence += self.word[::-1] + " "
    
