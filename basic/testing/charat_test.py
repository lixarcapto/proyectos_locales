

from basic.Basic import Basic
import random

def charat_test():
    print("charat_test")
    txt = "sometimes the heart sees what "
    txt += "is invisible to the eye"
    result_arr = []
    i:int = 0
    char:str = ""
    for i in range(10):
        i = random.randint(0, len(txt))
        char = Basic.charat(txt, i)
        result_arr.append(char)
    print(f"result char {result_arr}")