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
    num = converted[0]
    count = 1
    # if the converted list lenght is 1 return the value
    if len(converted) == 1:
        return converted[0]
    """if the converted list have continuous duplicate values,
    add them and remove the duplicate value"""
    for i in range(1, len(converted)):
        if num == converted[i]:
            count += 1
            if i + 1 == len(converted):
                final.append(num * count)
                break
            continue
        final.append(num * count)
        num = converted[i]
        count = 1
        if i + 1 == len(converted):
            final. append(num)

    # add the list values to find the final converted number
    for i in range(len(final) - 1):
        if (final[i] < final[i + 1]):
            final[i] = -1 * final[i]
    ans = 0
    for i in final:
        ans += i
    return ans
