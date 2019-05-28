import random

def random_data(range_values):
    array = []

    for index in range(range_values):
        array.append(random.randint(0, 100))

    return array

def linear_data(range_values):
    array = []
    i = range_values

    while i > 0:
        array.append(i)
        i = i -1

    return array