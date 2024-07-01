


from .WidgetElement import WidgetElement

class WidgetElementText(WidgetElement):

    def set_foreground(self, color):
        color = self.get_color(color)
        self.widget.config(fg=color)

    def set_font(self, font_name, size):
        self.widget.config(font=(font_name, size))

    def set_text(self, text):
        pass

    def add_text(self, text):
        pass

    def get_text(self):
        pass

    def extract_text(self):
        pass
