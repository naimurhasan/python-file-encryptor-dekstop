from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup


class MyPopup(Popup):
    pass


class HomeScreen(Widget):

    def pop_open_up(self):
        pops = MyPopup()
        pops.open()


class VideoEncryptorApp(App):
    def build(self):
        return HomeScreen()


if __name__ == '__main__':
    VideoEncryptorApp().run()
