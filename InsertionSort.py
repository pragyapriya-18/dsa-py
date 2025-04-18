import time
start=time.perf_counter()

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key

arr = [9, 5, 1, 4, 3]
insertionSort(arr)
print('Sorted Array in Ascending Order:')
print(arr)
end=time.perf_counter()
print("the time is:",end-start)

# Install matplotlib using "pip install matplotlib"
# Plot graph

import matplotlib.pyplot as plt
import numpy as np
x = [5, 6, 7, 8]

y = [5.46, 2.63, 5.54, 4.25]


plt.plot(x, y)
plt.xlabel('x axis(no of input)')
plt.ylabel('y axis(time)')
plt.title('Insertion Complexity')
plt.show()