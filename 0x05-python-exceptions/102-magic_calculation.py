#!/usr/bin/python3

def magic_calculation(a, b):
    ret = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                ret = ret + (a ** b / i)
        except Exception:
            ret = b + a
            break
    return ret
