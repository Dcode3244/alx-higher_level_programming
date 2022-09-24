#!/usr/bin/python3
def multiple_returns(sentence):
    strlen = len(sentence)
    if strlen == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return strlen, first_char
