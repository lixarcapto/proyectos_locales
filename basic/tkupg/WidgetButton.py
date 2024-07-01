

from .WidgetElementText import WidgetElementText
import tkinter as tk

class WidgetButton(WidgetElementText):

    def __init__(self, window_tk):
        self.widget = tk.Button(window_tk.widget)

    def set_text(self, string):
        self.widget.config(text=string)

    def add_listener(self, function):
        self.widget.config(command=function)
