

from basic.basic import Basic

def map_test():
    print("map_test")
    array = ["a", ["a, a, a"], "a"]
    array = Basic.map(array, 
        lambda e: e + " sum b")
    print(array)
    #
    dict = {"a":0, "b":0, "c":0}
    dict = Basic.map(dict, 
        lambda e: e + 1)
    print(dict)