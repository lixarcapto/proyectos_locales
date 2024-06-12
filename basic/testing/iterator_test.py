
from basic.Basic import Basic

def iterator_test():
    print("iterator_test")
    animal_arr = Basic.get_animal_array()
    iterator = Basic.iterator(animal_arr)
    for i in range(10):
        iterator.next()
        print(iterator.get())