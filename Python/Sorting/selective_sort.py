import random
import matplotlib
import matplotlib.pyplot as plt

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

def selective_sort(range_values):
    xarray = []

    for index in range(range_values):
        xarray.append(index)

    array = random_data(range_values)

    for i in range(len(array)):
        min = array[i]
        index = -1
        
        for j in range(i, (len(array))):
            if array[j] < min:
                min = array[j]
                index = j

        if index != -1:
            array[index] = array[i]	
            array[i] = min

        plt.cla()
        plt.plot(xarray, array, color = 'blue')	
        plt.scatter(xarray[i], array[i], color = 'red')
        plt.scatter(index, array[index], color = 'red')
        plt.pause(0.0001)


    plt.plot(xarray, array)
    plt.show()

range_values = 100
selective_sort(range_values)
