# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:50:41 2019

@author: Student
"""
#Create a 2d matrix of user defined size, fill it with random numbers between 0 and 255, then write a program to resize it to smaller size by extracting at user defined location
import numpy as np
import random
rows = int(input("Enter the number of rows in the matrix: "))
col = int(input("Enter the number of col in the matrix: "))
matrix = np.zeros((rows,col))
for i in range(rows):
    for j in range(col):
        matrix[i][j] = random.randint(0,255)
print(matrix)
row1 = int(input("Enter the number of rows from begg: "))
col1 = int(input("Enter the number of cols from begg "))
a = int(input("Enter the final row"))
b = int(input("Enter the final col"))
matrix1 = np.zeros((a-row1, b-col1))
for i in range(a-row1):
    for j in range(b-col1):
        matrix1[i][j] = matrix[i+row1][j+col1]
print(matrix1)
