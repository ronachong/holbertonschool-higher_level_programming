import threading
import sys

class StrLenThread(threading.Thread):
    def __init__(self, word):
        if type(word) != str: raise Exception("word is not a string")
        threading.Thread.__init__(self)
        self.word = word

    def run(self):
        global total_str_length
        total_str_length += len(self.word)

total_str_length = 0
words = sys.argv[1].split(" ")
str_length_threads = []

total_str_length = len(words) - 1 # store number of spaces in input into total_str_length 
for word in words:
    thread = StrLenThread(word) # create thread
    str_length_threads += [thread] # add thread to list of threads
    thread.start() # run thread

# use t.join to wait until all threads are done
for t in str_length_threads:
    t.join()

# print total_str_length, which should now have all the chars from words in addn to spaces    
print total_str_length
