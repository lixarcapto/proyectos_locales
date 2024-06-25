

from basic.Basic import Basic
from pac.Pac import Pac

def main():
    print("init")
    result = ""
    #---------------------------------------

    data = {
        "a":[1, 2, 3],
        "b":[1, 2, 3, 4, 5]
    }
    result = Pac.create_excel_dict(data, "file_excel")


    #----------------------------------------
    print(result)

main()