#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    converted = []
    final = []
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    # convert each string character to numbers and append them to a list
    for char in roman_string:
        for rom in list(roman.keys()):
            if char == rom:
                converted.append(roman[char])
    num = 0
    for i in range(len(converted)):
        if i != (len(converted) - 1) and converted[i] < converted[i + 1]:
            num += converted[i] * -1
        else:
            num += converted[i]
    return num
