from tkinter import *


class SceneManager:
    def __init__(self, root):
        self.root = root
        self.scenes = {}

    def add_scene(self, name, scene):
        self.scenes[name] = scene

    def show_scene(self, name):
        for scene_name, scene in self.scenes.items():
            if scene_name == name:
                scene.show()
            else:
                scene.hide()


class Scene(Frame):
    def __init__(self, parent):
        super().__init__(parent)
