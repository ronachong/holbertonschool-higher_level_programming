import Tkinter as tk

# description of View
class TaskView(tk.Toplevel): # inherit from Toplevel widget/Tinker class
    def __init__(self, master):
        if isinstance(master, tk.Tk) == False: # if master is not a tk root widget;
                                    # not sure if code needs more iteration.
                                    # do I use tk, or self, since self inherits from tk?
            raise Exception("master is not a tk.Tk()")

        # else
        tk.Toplevel.__init(self, master) # init attributes according to Toplevel..?
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)  # idk what this does.
                                                                # probably call protocol defined in Toplevel to destroy
                                                                # the master - but don't we need the old master...?

        # set private attributes
        self._title_var = self.StringVar() # type = tk.StringVar(), i.e. string widget
        self._title_label = self.Label(master, text=self._title_var) # type = tk.Label(), i.e. label widget

        # set public attributes
        self.toggle_button = self.Button(
            frame, text="reverse"
        ) # tk.Button, i.e. a button widget, text = Reverse?

        # pack widgets
        self._title_label.pack(side=RIGHT)
        self.toggle_button.pack(side=LEFT)

    # instance methods
    def update_title(self, title):
        # exception raising
        if type(title) != str:
            raise Exception("title is not a string")
        # probably update self.title_var; maybe more
        self._title_var.set(title)
        # if update_title is run, will the title_label text update as well? or does it need to be manually updated?
