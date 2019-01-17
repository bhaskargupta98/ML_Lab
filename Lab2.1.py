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
matrix1 = np.zeros((row1, col1))
for i in range(row1):
    for j in range(col1):
        matrix1[i][j] = matrix[i][j]
print(matrix1)
