


def count_keys(keys_array:list[str])\
 ->dict[int]:
    dict = {}
    for e in keys_array:
        if(not e in dict):
            dict[e] = 1
        else:
            dict[e] += 1
    return dict