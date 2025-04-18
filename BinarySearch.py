# Binary Search in python 

def binarySearch(array, x, low, high):
    if low<= high:
        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)

        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")

# Install matplotlib using "pip install matplotlib"
# Plot graph

import matplotlib.pyplot as plt
import numpy as np
x = [5, 6, 7, 8]

y = [4.46, 2.55, 2.01, 3.25]


plt.plot(x, y)
plt.xlabel('x axis(no of input)')
plt.ylabel('y axis(time)')
plt.title('Binary Complexity')
plt.show()
