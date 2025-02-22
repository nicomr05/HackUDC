#!/usr/bin/python
import kivy
kivy.require("2.3.1")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock


class Login(GridLayout):
    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class NotifApp(App):
    def callback(self, dt):
        print("call", dt)
    event = Clock.schedule_interval(callback, 1/30)

    def build(self):
        Label(text="holaa :P")
        return Login()


if __name__ == "__main__":
    NotifApp().run()
