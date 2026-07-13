import numpy as np
arr = np.array([1,2,3,4,5], ndmin = 5)
print(arr)
print("number of dimensions: "  , arr.ndim)
"""
here ndim is used after the array is created. It tells you how many dimensions the array actually has
and ndimn is used while creating an arry . It tells Numpy the minimum number of dimensions you want.

"""