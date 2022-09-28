#!/usr/bin/python
def uniq_add(my_list=[]):
    sum = 0
    for i in [*set(my_list)]:
        sum += i
    return sum
