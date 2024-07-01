

from basic.Basic import Basic
from pac.Pac import Pac
from tkupg.Tkupg import Tkupg
import time

def main():
    print("init")
    r = ""
    #---------------------------------------

    window = Tkupg.create_window()
    window.set_full_screen()
    window.set_size([1300, 750])
    window.set_background("red")
    painter = Tkupg.create_painter(window)
    painter.pack()
    poligon = Basic.random_point_ar(20, 
        [0,1000])
    painter.set_brush_with(5)
    print(poligon)
    painter.draw_poligon(poligon)
    window.start()

    #----------------------------------------
    print(r)

main()