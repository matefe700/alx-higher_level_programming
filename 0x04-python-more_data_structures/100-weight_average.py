#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) is 0:
        return 0
    a = sum(map(lambda x: x[0] * x[1], my_list))
    b = sum(map(lambda x: x[1], my_list))
    return a / b
