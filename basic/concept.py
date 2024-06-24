


from basic.Basic import Basic
import random

# para basic_things
def random_choice(array:list):
    if(type(array) == dict):
        k = random.choice(array)
        return array[k]
    elif(type(array) == list):
        return random.choice(array)
    raise Exception("unsupported tipe array")

def dothis():
    a = 0
    return a


def main():
    print("init")
    r = ""
    #---------------------------------------

    print(dothis.__name__)
    
    #----------------------------------------
    print(r)

main()
