

from basic.Basic import Basic
from pac.Pac import Pac

def main():
    print("init")
    result = ""
    #---------------------------------------

    result = Pac.read_xlsx_nested("file")


    #----------------------------------------
    print(result)

main()