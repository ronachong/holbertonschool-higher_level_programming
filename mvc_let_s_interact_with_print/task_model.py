class TaskModel:

    def __init__(self, title):
        if title == "" or type(title) != str:
            raise Exception("title is not a string")

        self.__title = title
        self.callback_title = null # callback_title is assigned its value by set_callback_title.

    # magic methods
    def __str__(self):
        print self.__title

    # getter method
    def get_title(self):
        return self.__title

    # setter method
    def set_callback_title(self, value):
    # set_callback_title assigns a value to self.callback_title
        self.__callback_title = value

    # other methods
    def toggle(self):
    # toggle_self reverses the value of title and calls the callback assigned to self.callback_title
        self.__title = self.__title[::-1] # uses string slicing to step backwards thru string

        # if self.__callback_title is set:
        if self.__callback_title != null:
            self.__callback_title(self.__title)
