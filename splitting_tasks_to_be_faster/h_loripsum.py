import threading
import requests

'''
The LoripsumThread constructor creates a thread which takes the following steps:
1) sends a GET request to the Loripsum API,
2) opens the file passed to it,
3) stores the response text from the GET request in the opened file
4) closes the file.
'''

class LoripsumThread(threading.Thread):
    lock = threading.Lock()

    def __init__(self, filename):
        threading.Thread.__init__(self)
        self.filename = filename

    def run(self):
        # make a get request
        response = requests.get("http://loripsum.net/api/1/short")
        print "Made response"
        # store response text in file
        LoripsumThread.lock.acquire()
        target = open(self.filename, 'a')
        try:
            target.write(response.text.encode('utf-8'))
        finally:
            target.close
            LoripsumThread.lock.release()
