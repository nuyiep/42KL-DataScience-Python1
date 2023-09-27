import numpy as np


def error_handling(family: list, start: int, end: int) -> list:
    '''
        Check if lists are not a list & if are the same size
    '''
    if (isinstance(family, list) is False):
        print("Error: List are not a list. It's a ", end='')
        print(type(family))
        exit()
    first_row_length = len(family[0])
    equal_row_length = True
    for row in family:
        if (len(row) != first_row_length):
            equal_row_length = False
            break
    if equal_row_length is False:
        print("Error: List rows are not of equal length")
        exit()


def slice_me(family: list, start: int, end: int) -> list:
    '''Using the slicing method'''
    error_handling(family, start, end)
    np_family = np.array(family)
    print("My shape is : ", end='')
    print(np.shape(np_family))
    np_new_shape = np_family[start:end]
    print("My new shape is: ", end='')
    print(np.shape(np_new_shape))
    family = np_new_shape.tolist()
    return (family)
