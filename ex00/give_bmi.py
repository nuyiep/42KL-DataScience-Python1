
import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    '''
        BMI formula- weight (kg) / height^2 (m)
    '''
    try:
        if (len(height) == 0 or len(weight) == 0):
            raise Exception("Empty list")
        if (len(height) != len(weight)):
            raise Exception("List of height and weight must be same size")
        types = (int, float)
        np_height = np.array(height)
        np_weight = np.array(weight)
        assert np_height.dtype in types, "Height must be int or float"
        assert np_weight.dtype in types, "Weight must be int or float"
        np_height_squared = np.square(np_height)
        bmi = np_weight/np_height_squared
        array_list = list(bmi)
        return (array_list)
    except Exception as e:
        print(e)
        exit()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
        True if above the limit
    '''
    try:
        bmi_numpy_array = np.array(bmi)
        assert isinstance(limit, int), "Limit must be an integer"
        bmi = list(bmi_numpy_array > limit)
        return (bmi)
    except Exception as e:
        print(e)
        exit()
