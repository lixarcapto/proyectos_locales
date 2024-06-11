

# return float
def calculate_mid(array):
    sum_number = 0
    for e in array:
        sum_number += e
    result = sum_number / len(array)
    return result
