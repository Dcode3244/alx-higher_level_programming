#!/usr/bin/python3
"""
a module that prints a text with 2 new lines after
each of these characters: (. ? and :)

"""


def text_indentation(text):
    """ prints a text with 2 new lines after each of these
        characters (. ? :)

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1
        if i == len(text):
            return

    while (i < (len(text))):
        if text[i] == ' ':
            i = is_space(text, i)
        if i == len(text):
            return
        if (text[i] in '.:?' or text[i] == '\n'):
            if text[i] in '.:?':
                print(text[i])
            print()
            i += 1
            continue
        print("{}".format(text[i]), end="")
        i += 1


def is_space(text, i):
    """ if a text character is space, checks if the space is
    at the end of a line, if not makes sure the space is printed,
    else moves the index to the next character

    Args:
        text (str): the text string
        i (int): index of the string
    Return:
        index value to be printed
    """

    if (text[i] == ' ' and
            (text[i - 1] in '.:?' or text[i - 1] == '\n')):
        while text[i] == ' ':
            i += 1
            if i == len(text):
                return i
        return i

    if text[i] == ' ':
        j = i
        while j < len(text):
            if text[j] == ' ':
                j += 1
            else:
                break
        if j == len(text):
            return j
        if text[j] == '\n':
            return j
        return i

    return i
