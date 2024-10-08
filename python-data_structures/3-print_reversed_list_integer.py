#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for i in range(len(my_list) - 1, -1, -1):
        if isinstance(my_list[i], int):
            print("{:d}".format(my_list[i]))
        else:
            raise ValueError("List contains non-integer value")
