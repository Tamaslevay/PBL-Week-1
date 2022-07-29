# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

" List of constants"

L = 1 #mm
d = 5 #um
k = 200 #W/mK
h = 1000 #W/m^2K
Ta = 293.15 #K
T0 = 353.15 #K
T4 = 343.15 #K
P = 15.71 #um
A = 19.63 #um
beta = (h*P/(k*A))**(1/2)
deltax = 0.25 #m
sigma = -2-beta**2*(deltax)**2


from numpy import diag, array

maindiag = array([1,sigma,sigma,sigma,1])
upperdiag = array([0,1,1,1])
lowerdiag = array([1,1,1,0])

matrix1 = diag(maindiag, 0)
matrix2 = diag(upperdiag,+1)
matrix3 = diag(upperdiag,-1)
print(matrix1)
print("")
print(matrix2)
print("")
print(matrix3)

matrix = matrix1 + matrix2 + matrix3
print("")
print(matrix)
