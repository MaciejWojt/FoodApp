import base
import random
import sys
import os
from kivy.app import App
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color

Window.clearcolor = (1, 1, 0, 1)
Window.size = (1366, 768) #only for desktop, not mobile!
Window.fullscreen = True
def show_popup():
    show = P1()
    
    popupWindow = ModalView(size_hint=(None, None), size=(800, 1600))

    popupWindow.add_widget(show)
    
    popupWindow.open()

class P1(FloatLayout):
    pass

class MainWindow(Screen):
    pass

class FoodWindow(Screen):
    pass

class AuthorWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class Pulser(Widget):
    bg_color = ObjectProperty([1, 1, 0, 1])

    def __init__(self, **kwargs):
        super(Pulser, self).__init__(**kwargs)
        Clock.schedule_once(self.start_pulsing, 1)

    def start_pulsing(self, *args):
        anim = Animation(bg_color=[1,1,0,1],duration = 2) + Animation(bg_color=[1,.5,0,1],duration = 2)
        anim.repeat = True
        anim.start(self)

class FoodApp(App):
    def build(self):
        kv = Builder.load_file("look.kv")
        return kv

    def btn(self):
        show_popup()

    def btn_help(self):
         os.execv(sys.executable, ['python'] + sys.argv)
         
    def quit(self):
        os.sys.exit()

    def rand_food(self):
        T = list(base.call_keys())
        i = T.index(random.choice(T))
        return T[i], base.call_base(T[i])

    link, recipe = rand_food(True)
    link = "photos/" + link

if __name__ == "__main__":
    FoodApp().run()