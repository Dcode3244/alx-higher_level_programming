#!/usr/bin/python3
def square_matrix_map(my_list=[]):
    return list(map(lambda x: list(map(lambda y: y ** 2, x)), my_list.copy()))
