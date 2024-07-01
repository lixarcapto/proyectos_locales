


from .WidgetWindow import WidgetWindow
from .WidgetInput import WidgetInput
from .WidgetButton import WidgetButton
from .WidgetLabel import WidgetLabel
from .painter.Painter import Painter

class Tkupg:

    def create_window():
        return WidgetWindow()

    def create_input(window):
        return WidgetInput(window)

    def create_button(window):
        return WidgetButton(window)

    def create_label(window):
        return WidgetLabel(window)

    def create_painter(window):
        return Painter(window)
