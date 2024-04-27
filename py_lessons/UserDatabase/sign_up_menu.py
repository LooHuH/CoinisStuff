from utils import *


class SignUpMenu(Scene):
    def __init__(self, parent):
        super().__init__(parent)
        self.name_label = Label(parent, text="Sign up")
        self.name_label = Label(parent, text="Username:")
        self.name_entry = Entry(parent)
        self.email_label = Label(parent, text="Email:")
        self.email_entry = Entry(parent)
        self.pass_label = Label(parent, text="Password:")
        self.pass_entry = Entry(parent)
        self.photo_label = Label(parent, text="Photo:")
        self.add_photo = Button(parent, text="Add photo")
        self.add_button = Button(parent, text="Sign up")

    def show(self):
        self.name_label.grid(row=0, column=1)
        self.name_label.grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.email_label.grid(row=2, column=0)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)
        self.pass_label.grid(row=3, column=0)
        self.pass_entry.grid(row=3, column=1, padx=10, pady=10)
        self.photo_label.grid(row=4, column=0)
        self.add_photo.grid(row=4, column=1, sticky=W + E, padx=10)
        self.add_button.grid(row=5, column=1, sticky=W + E, pady=20)

    def hide(self):
        self.name_label.grid_remove()
        self.name_label.grid_remove()
        self.name_entry.grid_remove()
        self.email_label.grid_remove()
        self.email_entry.grid_remove()
        self.pass_label.grid_remove()
        self.pass_entry.grid_remove()
        self.photo_label.grid_remove()
        self.add_photo.grid_remove()
        self.add_button.grid_remove()
