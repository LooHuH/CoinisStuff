from tkinter import *
from utils import *

from main_menu import *
from sign_in_menu import *
from sign_up_menu import *


window = Tk()
window.title('User Database')
window.geometry('400x300')


def sign_in():
    scene_manager.show_scene('sign_in_menu')


def sign_up():
    scene_manager.show_scene('sign_up_menu')


menubar = Menu(window)
file_menu = Menu(menubar, tearoff=False)

file_menu.add_command(label="Sign in", command=sign_in)
file_menu.add_command(label="Sign up", command=sign_up)
menubar.add_cascade(label="Options", menu=file_menu)

scene_manager = SceneManager(window)
scene_manager.add_scene('main_menu', MainMenu(window))
scene_manager.add_scene('sign_in_menu', SignInMenu(window))
scene_manager.add_scene('sign_up_menu', SignUpMenu(window))
scene_manager.show_scene("sign_in_menu")

window.config(
    menu=menubar
)

if __name__ == '__main__':
    window.mainloop()
