

import time

"""
    Funcion de repeticion temporal de una
    funcion en el hilo actual. No crea
    un nuevo hilo.
"""
def repeat(repetition: int, 
           seconds: int, 
           function):
    if(type(repetition) != int 
       or type(seconds) != int ):
        raise Exception("input is not integer")
    for i in range(repetition):
        time.sleep(seconds)
        function()
