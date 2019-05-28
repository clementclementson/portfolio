import matplotlib
import matplotlib.pyplot as plt
import data_generator as gen

def quicksort(array, xarray, l, r):
    if l >= r:
        return

    pivot = array[r]
    cnt = l

    for i in range(l, r + 1):
        if array[i] <= pivot:
            temp = array[i]
            array[i] = array[cnt]
            array[cnt] = temp
            cnt = cnt + 1

        plt.cla()
        plt.plot(xarray, array, color = 'blue')
        plt.scatter(xarray[i], array[i], color = 'red')
        plt.scatter(xarray[cnt], array[cnt], color = 'red')
        plt.pause(0.001)

    quicksort(array, xarray, l, cnt - 2)
    quicksort(array, xarray, cnt, r)

range_values = 100
xarray = []

for index in range(range_values):
    xarray.append(index)

array = gen.random_data(range_values)
quicksort(array, xarray, 0, (len(array) - 1))
plt.plot(xarray, array)
plt.show()