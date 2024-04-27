import tkinter as tk

class SceneManager:
    def __init__(self, root):
        self.root = root
        self.scenes = {}

    def add_scene(self, name, scene):
        self.scenes[name] = scene
        scene.pack_forget()  # Скрываем сцену при добавлении

    def show_scene(self, name):
        for scene_name, scene in self.scenes.items():
            if scene_name == name:
                scene.pack(fill="both", expand=True)  # Отображаем сцену
            else:
                scene.pack_forget()  # Скрываем неактивные сцены

class Scene(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

class MainMenuScene(Scene):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="Это главное меню")
        label.pack(padx=20, pady=20)

class SettingsScene(Scene):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="Это меню настроек")
        label.pack(padx=20, pady=40)

class HelpScene(Scene):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="Это меню помощи")
        label.pack(padx=20, pady=640)

def main():
    root = tk.Tk()
    root.title("Мое приложение")
    root.geometry('1000x1000')

    scene_manager = SceneManager(root)

    main_menu_scene = MainMenuScene(root)
    settings_scene = SettingsScene(root)
    help_scene = HelpScene(root)

    scene_manager.add_scene("main_menu", main_menu_scene)
    scene_manager.add_scene("settings", settings_scene)
    scene_manager.add_scene("help", help_scene)

    scene_manager.show_scene("settings")

    root.mainloop()

if __name__ == "__main__":
    main()
