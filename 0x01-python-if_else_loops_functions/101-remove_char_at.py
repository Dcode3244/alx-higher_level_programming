#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    for c in range(len(str)):
        if c == n:
            continue
        string += str[c]
    return string
