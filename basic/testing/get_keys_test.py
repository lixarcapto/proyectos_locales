

from basic.Basic import Basic

def get_keys_test():
    print("get_keys_test")
    dict = Basic.get_vegetable_dict()
    keys_arr = Basic.get_keys(dict)
    print(keys_arr)