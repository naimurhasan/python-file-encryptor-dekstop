from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

import tkinter as tk
from tkinter import filedialog

import encryptor


class HomeScreen(Widget):

    def pop_open_up(self):
        root = tk.Tk()
        root.withdraw()

        path = filedialog.askopenfilename()

        # pass
        # path = filechooser.open_file(title="Pick a file...")
        encryptor.encrypt_the_file(path)


class VideoEncryptorApp(App):
    def build(self):
        Builder.load_string("""
<HomeScreen>:
    
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height
    
        Label:
            text: "Encrypt Anything!"
            font_size: 25

        Button:
            text: "Encrypt"
            font_size: 20
            on_press: root.pop_open_up()

        """)
        return HomeScreen()


if __name__ == '__main__':
    VideoEncryptorApp().run()
