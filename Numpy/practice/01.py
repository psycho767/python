#Create a 1D NumPy array containing numbers 10 to 50.

import numpy as np


numbers = []
for i in range(10, 51, 10):
    numbers.append(i)

arr = np.array(numbers)
print(arr)