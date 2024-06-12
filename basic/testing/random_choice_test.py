

from basic.Basic import Basic

def random_choice_test():
    print("random_choice_test")
    names_arr = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Emily",
    "Frank",
    "Grace",
    "Helen",
    "Ian",
    "Julia"
    ]
    for i in range(10):
        print(Basic.random_choice(names_arr))