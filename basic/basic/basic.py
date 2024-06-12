

# funtions
from .fn.random_bool import*
from .fn.random_choice import*
from .fn.random_without import*
from .fn.random_probability import*
from .fn.repeat import*
from .fn.map_upg import*
from .fn.init_array import*
from .fn.calculate_mid import*
from .fn.deep import*
from .fn.key_by_index import*
from .fn.get_keys import*
from .fn.in_range import*
from .fn.part_from_percent import*
from .fn.percent_from_part import*
from .fn.total_from_part import*
from .fn.valid_string import*
from .fn.randint_array import*
from .fn.set_in_range import*
from .fn.sum_in_range import*
from .fn.dict_to_array import*
from .fn.valid_index import*
from .fn.sum_array import*
from .fn.percent_to_index import*
from .fn.fuse import*
from .fn.is_error import*
from .fn.random_without_repeat import*
from .fn.random_ip import*
from .fn.missing_numbers import*

# modules
from .mod.iterator.Iterator import Iterator
from .mod.switch.Switch import Switch
from .mod.counter_call.CounterCall import CounterCall

# constants
from .const.abc_tuple import*
from .const.number_tuple import*
from .const.animal_array import*
from .const.vegetable_dict import*

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
    
    def get_vegetable_dict():
        return VEGETABLE_DICT
    
    def init_array(range, value = None):
        return init_array(range, value)
    
    def calculate_mid(array):
        return calculate_mid(array)
    
    def deep(array) -> int:
        return deep(array)
    
    def key_by_index(dict, index: int) \
        -> str:
        return key_by_index(dict, int)
    
    # return string_list
    def get_keys(dict) -> list:
        return get_keys(dict)
    
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
        return in_range(number, range)
    
    def part_from_percent(percent: int, 
        total: int) -> float:
        return part_from_percent(percent, 
            total)
    
    def percent_from_part(part: int, 
        total: int)-> float:
        return percent_from_part(part, 
            total)
    
    def total_from_part(percent, 
        part: int) -> float:
        return total_from_part(percent, 
            part)
    
    """
    function to validate the sent string; 
    this validates if the string is a 
    string, is not empty and is greater 
    than the minimum (optional)
    """
    def valid_string(data: str, 
             min_size = -1,
             is_strict = False):
        valid_string(data, min_size)

    def randint_array(size: int, 
        range_arr: list) -> list:
        return randint_array(int, range_arr)
    
    # return number
    def set_inrange(value: int, range_arr: list):
        return set_inrange(value, range_arr)
    
    # return number
    def sum_in_range(value_a, value_b, 
                    range_arr):
        return sum_in_range(value_a, 
            value_b, range_arr)
    
    def dict_to_array(dict) -> list:
        return dict_to_array(dict)
    
    # not return
    def valid_index(index: int, leng: int):
        return valid_index(index, leng)
    
    # return element type
    def sum_array(array):
        return sum_array(array)
    
    def percent_to_index(percent, limit):
        return percent_to_index(percent, 
                    limit)
    
    def fuse(array_a, array_b) -> list:
        return fuse(array_a, array_b)
    
    def is_error(value):
        return is_error(value)
    
    # return int
    def random_without_repeat(range_arr, 
        repeated_int_ar,
        is_exclusive = False):
        return random_without_repeat(
            range_arr, 
            repeated_int_ar,
            is_exclusive)
    
    def random_ip():
        return random_ip()
    
    def missing_numbers(number_list):
        return missing_numbers(number_list)
    
    def switch():
        return Switch()
    
    def counter_call(limit: int):
        return CounterCall(limit)