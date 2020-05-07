#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    mul = 1
    div = 0
    result = 0
    for idx in my_list:
        for x in idx:
            mul *= x
        div += idx[-1]
        result += mul
        mul = 1
    result /= div
    return result
