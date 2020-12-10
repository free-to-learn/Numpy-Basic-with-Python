# Numerical operations on arrays

# Basic operations

import numpy as np
import matplotlib.pyplot as plt


a = np.array([1, 2, 3, 4])
print(a + 1,"We are Add 1 to existing array")
print(2**a,"We are Exp to Existing array")

# All arithmetic operates elementwise:
b = np.ones(4) + 1
print(a - b)
print(a * b)

j = np.arange(5)
print(2**(j + 1) - j)



# These operations are of course much faster than if you did them in pure python:
a = np.arange(10000) # this from numpy
%timeit a+1 # Time Taken to Run the Cell



# This is From Python
l = range(10000)
%timeit [i+1 for i in l]





# Task
"""
1. Create Two Arrays A and B Should be Only 1D
2. Perfome All Operators in Python
3. Create Two Arrays A and B Should be Only 2D


