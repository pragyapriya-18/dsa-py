import time
start=time.perf_counter()
def selectionSort(array):
    n = len(array)
    for i in range(n):
        minimum = i

        for j in range(i + 1, n):
            if (array[j] < array[minimum]):
                minimum = j

        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp

    return array

array = [13, 4, 9,45,12]
print("sortedlist =",selectionSort(array))
end=time.perf_counter()
print("the time is:",end-start)

# Install matplotlib using "pip install matplotlib"
# Plot graph

import matplotlib.pyplot as plt
import numpy as np
x = [5, 6, 7, 8]

y = [2.46, 2.63, 2.54, 2.25]


plt.plot(x, y)
plt.xlabel('x axis(no of input)')
plt.ylabel('y axis(time)')
plt.title('Selection Complexity')
plt.show()