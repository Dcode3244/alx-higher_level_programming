#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    list_len = 0
    try:
        for i in range(x):
            list_len += 1
            print(my_list[i], end="")
        print()
        return list_len
    except IndexError:
        print()
        return list_len - 1
