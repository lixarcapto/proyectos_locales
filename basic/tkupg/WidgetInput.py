


from .WidgetElementText import WidgetElementText
import tkinter as tk

class WidgetInput(WidgetElementText):

    def __init__(self, window_tk):
        self.widget = tk\
            .Text(window_tk.widget)

    def set_text(self, text):
        self.widget.delete("1.0", tk.END)
        self.widget.insert(tk.END, text)

    def add_text(self, text):
        self.widget.insert(tk.END, text)

    def get_text(self):
        return self.widget.get("1.0", tk.END)

    def extract_text(self):
        text = self.widget.get("1.0", tk.END)
        self.widget.delete("1.0", tk.END)
        return text
