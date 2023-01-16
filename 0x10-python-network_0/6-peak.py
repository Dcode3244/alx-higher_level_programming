#!/usr/bin/python3
''' defines a funcion to find a peak in a list of unsorted integers '''


def find_peak(list_of_integers):
    ''' a function to find a peak in a list of unsorted integers '''
    nums = list_of_integers
    if len(nums) == 0:
        return (None)
    if len(nums) == 1:
        return nums[i]

    for i in range(len(list_of_integers) - 1):
        if (nums[i + 1] < nums[i]):
            return (nums[i])

    return (nums[i])
