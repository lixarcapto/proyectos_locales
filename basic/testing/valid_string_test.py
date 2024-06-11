

from basic.basic import Basic

def valid_string_test():
    print("\nvalid_string_test\n")
    Basic.valid_string(0, 0, False)
    Basic.valid_string("", 0, False)
    Basic.valid_string("texto", 6, False)
