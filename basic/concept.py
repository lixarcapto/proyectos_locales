


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

def main():
    print("init")
    r = ""
    #---------------------------------------

    
    
    #----------------------------------------
    print(r)

main()
