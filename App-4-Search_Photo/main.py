from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def get_image_link(self):
        # get user query from text input
        query = self.manager.current_screen.ids.user_query.text
        # get wikipedia page and the first image link
        page = wikipedia.page(query)
        return page.images[0]

    def download_image(self):
        # download the image
        req = requests.get(self.get_image_link())
        file_path = 'images/image.png'
        with open(file_path, 'wb') as file:
            print(file.readable())
            file.write(req.content)

        return file_path

    def set_image(self):
        # set the image in the image widget
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
