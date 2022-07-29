# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

" List of constants"

L = 1*10**(-3) #m
d = 5*10**(-6) #m
k = 200 #W/mK
h = 1000 #W/m^2K
Ta = 293.15 #K
T0 = 353.15 #K
T4 = 343.15 #K
P = 15.71*10**(-6) #um
A = 19.63*10**(-6) #um
beta = (h*P/(k*A))**(1/2)
deltax = 0.25*10**(-3) #m
sigma = -2-beta**2*(deltax)**2


from numpy import diag, array

"Forming vectors for diagonals"

maindiag = array([1,sigma,sigma,sigma,1])
upperdiag = array([0,1,1,1])
lowerdiag = array([1,1,1,0])

"Forming diagonal matrices"

matrix1 = diag(maindiag, 0)
matrix2 = diag(upperdiag,+1)
matrix3 = diag(upperdiag,-1)

"Adding the diagonal matrices"

matrix = matrix1 + matrix2 + matrix3
print("")
print(matrix)

