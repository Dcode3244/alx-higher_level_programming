#!/usr/bin/python3
''' defines a funcion to find a peak in a list of unsorted integers '''


def find_peak(list_of_integers):
    ''' a function to find a peak in a list of unsorted integers '''
    if not list_of_integers or len(list_of_integers) == 0:
        return (None)

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    if len(list_of_integers) == 2:
        return (max(list_of_integers))

    half = int(len(list_of_integers) / 2)
    peak = list_of_integers[half]

    if peak > list_of_integers[half - 1] and peak > list_of_integers[half + 1]:
        return peak

    elif peak < list_of_integers[half - 1]:
        return find_peak(list_of_integers[:half])
    else:
        return find_peak(list_of_integers[half + 1:])
