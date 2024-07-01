


from .WidgetBase import WidgetBase
import tkinter as tk

class WidgetElement(WidgetBase):

    def __init__(self, widget):
        self.widget = widget.widget

    def set_size(self, range):
        self.widget.pack_propagate(False)
        self.widget.config(height= range[0],
            width= range[1])

    def set_location(self, point_ar):
        #self.widget.config(anchor='center')
        #self.widget.pack_propagate(False)
        self.widget.place(y = point_ar[0],
            x = point_ar[1])

    def pack(self):
        self.widget.pack(fill=tk.BOTH, 
            expand=True)

    def grid(self, row, column):
        self.widget.grid(
            row,
            column,
            columnspan = 3,
            sticky ='nsew',
            padx=10,
            pady=10
        )
