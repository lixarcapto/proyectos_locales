

from .in_deps import*

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
    
    """
    Function that calculates the 
    average of the numbers in 
    the sent array.
    """
    def calculate_mid(array:list)->float:
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
    
    def probability():
        return Probability()
    
    # return int
    def compare_strings(strig_primal, 
            string_to_compare):
        return compare_strings(strig_primal, 
            string_to_compare)
    
    def related_dict(similar_percent: int = 70):
        return RelatedDict(similar_percent)
    
    # return char
    def charat(string:str, index:int) -> str:
        return charat(string, index)
    
    def cut_from(string: str, caracter: str)\
    -> str:
        return cut_from(string, caracter)
    
    def cut_until(string: str, caracter: str)\
    -> str:
        return cut_until(string, caracter)
    
    # return string_array
    def divide_string(index:int, string:str)\
        -> list:
        return divide_string(index, string)
    
    # return string
    def next_word(text: str, searched_string: str):
        return next_word(text, 
            searched_string)
    
    def get_between(base:str, start:str,
        end:str) -> str:
        return get_between(base, start, end)
    
    def insert_string(index:int, base_string:str, 
        new_string:str) -> str:
        return insert_string(index,
            base_string, new_string)
    
    def normalize(text: str) -> str:
        return normalize(text)
    
    def split_by(string, dividers_arr: list):
        return split_by(string, dividers_arr)
    
    def simil_search(array:list, element:str, 
        required_percent:int) -> str:
        return simil_search(array, element, 
                required_percent)
    
    def get_description(string,
        separator_string, range_string_array):
        return get_description(
            string,
            separator_string, 
            range_string_array
            )
    
    """
    Function that converts the elements of 
    an array into the keys of a dictionary; 
    with the data sent as an element.
    EXAMPLE:
        array = ['a', 'b', 'c', 'd', 'e']
        result:list = Basic.array_to_dict(array)
        print(result)
    OUTPUT:
        {'a': None, 'b': None, 'c': None, 
        'd': None, 'e': None}
    """
    def array_to_dict(array:list, 
    data_type = None)->dict:
        return array_to_dict(array, 
            data_type)