import Tkinter as tk

# description of View
class TaskView(tk.Toplevel): # inherit from Toplevel widget/Tinker class
    def __init__(self, master):
        if isinstance(master, tk.Tk) == False: # if master is not a tk root widget;
            raise Exception("master is not a tk.Tk()")

        # else
        tk.Toplevel.__init__(self, master) # init attributes according to Toplevel..?
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)  # idk what this does.
                                                                # probably call protocol defined in Toplevel to destroy
                                                                # the master - pass self as parent as a result.

        # set private attributes
        self.__title_var = tk.StringVar() # string widget
        self.__title_label = tk.Label(self, textvariable=self.__title_var) # label widget

        # set public attributes
        self.toggle_button = tk.Button(self, text="reverse") # tk.Button, i.e. a button widget, text = Reverse?

        # pack widgets
        self.toggle_button.pack(side=tk.LEFT)
        self.__title_label.pack(side=tk.RIGHT)

    # instance methods
    def update_title(self, title):
        # exception raising
        if type(title) != str:
            raise Exception("title is not a string")
        self.__title_var.set(title)
