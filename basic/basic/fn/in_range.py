


"""
    Function to identify if the input 
    number is contained within the 
    sending range.
    Ex:
        code: print(in_range(5, [4, 6]))
        output: True
"""
def in_range(number: int, range: list)\
        -> bool:
    if(not type(number) == int
    and not type(number) == float):
        raise Exception(f"is not a number {number}")
    if(number >= range[0]
    and number <= range[1]):
        return True
    return False
