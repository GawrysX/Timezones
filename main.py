from datetime import datetime
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.properties import ListProperty
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import pytz


class Label(Label):
    background_color = ListProperty([1, 1, 1, 1])

    def __init__(self, **kwargs):
        self.background_color = kwargs.pop('background_color', (1, 1, 1, 1))
        self.color = kwargs.pop('color', (0,0,0,1))
        super(Label, self).__init__(**kwargs)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.background_color)
            Rectangle(pos=self.pos, size=self.size)


class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.label1 = Label(background_color=(1, 0, 0, 1))
        self.add_widget(self.label1)

        self.label2 = Label(background_color=(0, 1, 0, 1))
        self.add_widget(self.label2)

        self.label3 = Label(background_color=(0, 0, 1, 1))
        self.add_widget(self.label3)

        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, *args):
        poland_tz = pytz.timezone("Europe/Warsaw")
        poland_time = datetime.now(poland_tz)
        self.label1.text = f"Poland Time : {poland_time.strftime('%Y-%m-%d %H:%M:%S')}"

        singapore_tz = pytz.timezone("Asia/Singapore")
        singapore_time = datetime.now(singapore_tz)
        self.label2.text = f"Singapore Time : {singapore_time.strftime('%Y-%m-%d %H:%M:%S')}"

        newyork_tz = pytz.timezone("America/New_York")
        newyork_time = datetime.now(newyork_tz)
        self.label3.text = f"New York Time : {newyork_time.strftime('%Y-%m-%d %H:%M:%S')}"


class TimeApp(App):
    def build(self):
        return MyLayout()


root = TimeApp()
root.run()
