import numpy as np

arr = np.array([1,2,3,4])
print(arr.ndim)

arr1 = np.array([
    [1,2,3] ,[4,5,6]
])
print(arr1.ndim)

arr2 = np.array([
    [
        [1,2],[3,4]
    ],
    [
        [5,6],[7,8]
    ]
])

print(arr2.ndim)