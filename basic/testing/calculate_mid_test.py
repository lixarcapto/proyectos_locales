
from basic.Basic import Basic

def calculate_mid_test():
    print("calculate_mid_test")
    array = [2, 3, 3, 5, 7, 10]
    print("the right result is 5")
    mid = Basic.calculate_mid(array)
    tx = "the mid of 2, 3, 3, 5, 7, 10 is 5;\n"
    print(f"{tx} the result is {mid}")
    