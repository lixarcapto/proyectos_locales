

from .WidgetBase import WidgetBase
import tkinter

class WidgetWindow(WidgetBase):

    def __init__(self):
        self.widget = tkinter.Tk()

    """
        Funcion para congirar la pantalla como
        fullscreen.
    """
    def set_full_screen(self):
        self.widget.attributes( "-fullscreen", True )
        self.widget.bind( "<F11>", self.toggle_full_screen )
        self.widget.bind( "<Escape>", self.quit_full_screen )

    def set_text(self, text):
        self.widget.title(text)

    def set_size(self, range):
        self.widget.pack_propagate(False)
        geometry = f"{range[0]}x{range[1]}"
        self.widget.geometry(geometry)

    def start(self):
        self.widget.mainloop()

    def toggle_full_screen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.widget.attributes("-fullscreen", self.fullScreenState)

    def quit_full_screen(self, event):
        self.fullScreenState = False
        self.widget.attributes("-fullscreen", self.fullScreenState)
