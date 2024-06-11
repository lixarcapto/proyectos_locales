

# funtions
from .fn.random_bool import*
from .fn.random_choice import*
from .fn.random_without import*
from .fn.random_probability import*
from .fn.repeat import*
from .fn.map_upg import*
from .fn.init_array import*
from .fn.calculate_mid import*
# modules
from .mod.iterator.Iterator import Iterator
# constants
from .const.abc_tuple import*
from .const.number_tuple import*
from .const.animal_array import*

class Basic:

    def random_bool() -> bool:
        return random_bool()
    
    def random_choice(array):
        return random_choice(array)
    
    def random_without(range: int, 
        repeated_int_ar: list,
        is_exclusive:bool = False
        ) -> int:
        return random_without(
            range, 
            repeated_int_ar, 
            is_exclusive
        )
    
    def random_probability(porcentage: int)\
          -> bool:
        return random_probability(porcentage)
    
    def repeat(repetition: int, 
           seconds: int, 
           function):
        repeat(repetition, 
           seconds, 
           function)
        
    # return array or dict
    def map(array, function):
        return map_upg(array, function)
    
    def iterator(array, 
                 is_cycle = False):
        return Iterator(array, is_cycle)
    
    def get_abc_tuple():
        return ABC_TUPLE
    
    def get_number_tuple():
        return NUMBER_TUPLE
    
    def get_animal_array():
        return ANIMAL_ARRAY
    
    def init_array(range, value = None):
        return init_array(range, value)
    
    def calculate_mid(array):
        return calculate_mid(array)
    
