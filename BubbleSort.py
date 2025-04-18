import time  

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1): 
        for j in range(0, n-i-1):  
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]

start = time.perf_counter() 
bubbleSort(arr)
end = time.perf_counter() 
print("Sorted array is:", arr)
print(f"Time taken: {end - start:.6f} seconds") 

# Install matplotlib using "pip install matplotlib"
# Plot graph

import matplotlib.pyplot as plt
import numpy as np
x = [5, 6, 7, 8]

y = [2.55, 2.63, 2.54, 2.25]


plt.plot(x, y)
plt.xlabel('x axis(no of input)')
plt.ylabel('y axis(time)')
plt.title('Bubble Complexity')
plt.show()

