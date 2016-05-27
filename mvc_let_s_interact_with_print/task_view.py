import Tkinter as tk

# description of View
class TaskView(tk.Toplevel): # inherit from Toplevel widget/Tinker class
    __init__(self, master):
        if master is not tk.Tk(): # not sure if this code needs more iteration
            raise Exception("master is not a tk.Tk()")

        # else
        tk.Toplevel.__init(self, master) # init attributes according to Toplevel..?
        self.protocol('WM_DELETE_WINDOW', self.master.destroy) # idk what this does.
        # probably call protocol defined in Toplevel to destroy the master - but don't
        # we need the old master...?

        # private attributes
        self._title_var = ?? # type = tk.StringVar(), i.e. string widget
        self._title_label = ?? # type = tk.Label(), i.e. label widget

        # public attributes
        self.toggle_button = ?? # tk.Button, i.e. a button widget, text = Reverse? and left

    # instance methods
    def update_title(self, title):
        # exception handling
        # probably update self.title_var; maybe more
