import Tkinter as tk
from task_model import TaskModel
from task_view import TaskView # this is imported in main, redundant here?

class TaskController:

    # define constructor
    def __init__(self, master, model):
        # raise exceptions
        if isinstance(master, tk.Tk) == False:
            raise Exception("master is not a tk.Tk()")
        if isinstance(model, TaskModel) == False:
            raise Exception("model is not a TaskModel")

        # set private attributes
        self.__model = model
        self.__view = TaskView(master)
        self.__view.update_title(self.__model.get_title()) # set title for view according to model

        # link all callbacks from model to update view
        self.__model.set_callback_title(self.__view.update_title)
        # self.__view.update_title(self.__model.get_title())

        # link view button to update model (link model callback to view)
        self.__view.toggle_button.configure(command=self.__model.toggle)
