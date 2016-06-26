class OrderedArray

class OrderedArrayThread(threading.Thread):
    def __init__(self, number):
        if type(number) != integer: raise Exception("number is not an integer")
        self.number = number

    def run(self):
        OrderedArray.list.insert(i, self.number) # i not yet defined
