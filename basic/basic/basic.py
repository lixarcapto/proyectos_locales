

from .svc.random_bool import*
from .svc.random_choice import*
from .svc.random_without import*
from .svc.random_probability import*

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