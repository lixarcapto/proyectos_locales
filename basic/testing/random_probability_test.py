

from basic.basic import Basic

def random_probability_test():
    print("random_probability_test")
    r = 0
    for i in range(101):
        r = Basic.random_probability(i)
        print(f"{i}% result in {r}")