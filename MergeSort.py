def   mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left) 
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                   myList[k] = left[i]
                   i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList)

# Install matplotlib using "pip install matplotlib"
# Plot graph

import matplotlib.pyplot as plt
import numpy as np
x = [5, 6, 7, 8]

y = [2.46, 2.63, 2.54, 2.25]


plt.plot(x, y)
plt.xlabel('x axis(no of input)')
plt.ylabel('y axis(time)')
plt.title('Merge Complexity')
plt.show()