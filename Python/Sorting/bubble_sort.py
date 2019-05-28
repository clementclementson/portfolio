import matplotlib
import matplotlib.pyplot as plt
import data_generator as gen

def bubble_sort(range_values):
    xarray = []

    for index in range(range_values):
        xarray.append(index)

    array = gen.random_data(range_values)

    for i in range(len(array) - 1):
        for j in range(0, (len(array) - i - 1)):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                
                plt.cla()
                plt.plot(xarray, array, color = 'blue')	
                plt.scatter(xarray[j], array[j], color = 'red')
                plt.scatter(xarray[j+1], array[j+1], color = 'red')
                plt.pause(0.0001)

    plt.plot(xarray, array)
    plt.show()



range_values = 100
bubble_sort(range_values)
