import matplotlib
import matplotlib.pyplot as plt
import data_generator as gen

def selective_sort(range_values):
    xarray = []

    for index in range(range_values):
        xarray.append(index)

    array = gen.random_data(range_values)

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
