class TaskModel:

    def __init__(self, title):
        if title == "" or type(title) != str:
            raise Exception("title is not a string")

        self.__title = title
        self.__callback_title = None # callback_title is assigned its value by
        # set_callback_title.

    def __str__(self):
        return self.__title

    def get_title(self):
        return self.__title

    def set_callback_title(self, value):
    # set_callback_title assigns a value to self.callback_title
        self.__callback_title = value

    def toggle(self):
    # toggle_self reverses the value of title and calls the callback assigned to
    # self.callback_title
        self.__title = self.__title[::-1] # use string slicing
        # if self.__callback_title is set:
        if self.__callback_title != None:
            self.__callback_title(self.__title)
