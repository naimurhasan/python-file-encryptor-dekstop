from kivy.app import App
from kivy.uix.widget import Widget
from plyer import filechooser

import encryptor


class HomeScreen(Widget):

    def pop_open_up(self):
        path = filechooser.open_file(title="Pick a file...",
                                     # filters=[("Comma-separated Values", "*.csv")]
                                     )
        # file name = first file from list, split by \, last item
        # file_name = path[0].split('\\')[-1]
        encryptor.encrypt_the_file(path[0])


class VideoEncryptorApp(App):
    def build(self):
        return HomeScreen()


if __name__ == '__main__':
    VideoEncryptorApp().run()
