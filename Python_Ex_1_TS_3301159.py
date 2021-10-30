#!/usr/bin/env python
# coding: utf-8

# Applications of Accelerators Lecture
# Python Exercise 1
# Tugce Sirkecioglu 3301159
# October 2021

# Write a function in Python code that adds 2+2 and returns the result.

def add(x, y):
    result = x + y
    return result
print(add(2,2))

# Write a function in Python code that multiples two 3x3 Matrices (ndarray) and returns the result.

import numpy as np

A = np.array([[1, -7, 2], [3, 8, 13], [-4, -15, -17]])
B = np.array([[3, 19, 5], [-12, 1, 7], [5, -10, 8]])

print(np.dot(A,B))
