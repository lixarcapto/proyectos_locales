

"""
    Funcion que extrae una letra del string en
    una posicion especifica usando slicing.
"""
# char
def charat(string:str, index:int) -> str:
    if(not index < len(string)):
        raise Exception("string out of range " \
            + "index " + str(index) \
            + " of leng " + str(len(string)))
    return string[index:index + 1]