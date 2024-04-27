from utils import *


class SignInMenu(Scene):
    def __init__(self, parent):
        super().__init__(parent)
        self.name_label = Label(parent, text="Username:")
        self.name_entry = Entry(parent)
        self.email_label = Label(parent, text="Password:")
        self.pass_entry = Entry(parent)
        self.add_button = Button(parent, text="Sign in")

    def show(self):
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.email_label.grid(row=1, column=0)
        self.pass_entry.grid(row=1, column=1, padx=10, pady=10)
        self.add_button.grid(row=4, column=1, sticky=W + E, pady=20)

    def hide(self):
        self.name_label.grid_remove()
        self.name_entry.grid_remove()
        self.email_label.grid_remove()
        self.pass_entry.grid_remove()
        self.add_button.grid_remove()
