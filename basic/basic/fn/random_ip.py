


from .randint_array import*
from .sum_array import*

def random_ip():
    quantity = 4
    array = randint_array(quantity, [0, 255])
    text = sum_array(array, ".")
    return text