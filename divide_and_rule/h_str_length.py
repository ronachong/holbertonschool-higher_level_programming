import threading

class StrLengthThread(threading.Thread):
    total_str_length = 0
    
    def __init__(self, word):
        if type(word) != str: raise Exception("word is not a string")
        threading.Thread.__init__(self)
        self.word = word

    def run(self):
        StrLengthThread.total_str_length += len(self.word)
