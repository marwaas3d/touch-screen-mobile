from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.core.window import Window
import random


class DrawingPad(Widget):

    def color_for_touch(self, touch):
        if 'color' not in touch.ud:
            random.seed(touch.uid)
            touch.ud['color'] = (
                random.random(),
                random.random(),
                random.random()
            )
        return touch.ud['color']

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.color_for_touch(touch))
            d = 40  # circle diameter
            x, y = touch.pos
            touch.ud['circle'] = Ellipse(
                pos=(x - d/2, y - d/2),
                size=(d, d)
            )
            touch.ud['line'] = Line(
                points=[x, y],
                width=2
            )

    def on_touch_move(self, touch):
        if 'line' in touch.ud:
            touch.ud['line'].points += touch.pos


class TouchDrawApp(App):

    def build(self):
        Window.clearcolor = (0.09, 0.09, 0.11, 1)  # dark background
        return DrawingPad()


if __name__ == "__main__":
    TouchDrawApp().run()