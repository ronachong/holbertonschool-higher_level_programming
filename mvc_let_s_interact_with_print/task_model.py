class TaskModel:

    def __init__(self, title):
        if title = "" or type(title) != str:
            raise Exception("title is not a string")
        
        self.__title = title

    def __callback_title(self): # should this be an attribute like self.__callback_title = def, or something similar to that,
        # or should it be like this, a definition of a private method?
        # later on set_callback_title seems to exist to change what self.__callback_title is, but how does it accomplish that?
        [..]
        
    # magic methods
    def __str__(self):
        print self.__title
        
    # getter method
    def get_title(self):
        return self.__title

    # setter method
    def set_callback_title(self, value):
        # what does this function do? set the callback that deals with title?
        # not sure what to put here; self.__callback_title = value, or some more circuitous operation

    # other methods
    def toggle_self:
        self.__title = self.__title[::-1] # uses string slicing to step backwards thru string

        # if self.__callback_title is set:
        if self.__callback_title != ??:
            self.__callback_title(self.__title)
