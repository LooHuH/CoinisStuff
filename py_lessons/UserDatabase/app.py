from tkinter import *
from utils import *

window = Tk()
window.title('User Database')
window.geometry('400x300')

frame = Frame(window)

menubar = Menu(window)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label="Sign in", command=sign_in)
file_menu.add_command(label="Sign up", command=sign_up)
menubar.add_cascade(label="Options", menu=file_menu)

frame.pack(expand=True)

window.config(
    menu=menubar
)
window.mainloop()
