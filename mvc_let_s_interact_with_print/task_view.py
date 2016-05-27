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
                                                                # the master - but don't we need the old master...?

        # set private attributes
        self._title_var = tk.StringVar() # type = tk.StringVar(), i.e. string widget
        self._title_label = tk.Label(master, text=self._title_var) # type = tk.Label(), i.e. label widget

        # set public attributes
        self.toggle_button = tk.Button(master, text="reverse", command=self.master.destroy) # no command parameter yet # tk.Button, i.e. a button widget, text = Reverse?

        # pack widgets
        self.toggle_button.pack(side=tk.LEFT)
        print "Packed button to left."
        self._title_label.pack(side=tk.RIGHT)
        print "Packed button to right."

    # instance methods
    def update_title(self, title):
        # exception raising
        if type(title) != str:
            raise Exception("title is not a string")
        # probably update self.title_var; maybe more
        self._title_var.set(title)
        # if update_title is run, will the title_label text update as well? or does it need to be manually updated?
