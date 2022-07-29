# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from numpy import diag, array, transpose, linalg, pi, sinh
import matplotlib.pyplot as plt

print("")

" List of constants"

L = 0.001 #m
d = 5*10**(-6) #m
k = 200 #W/mK
h = 1000 #W/m^2K
Ta = 293.15 #K
T0 = 353.15 #K
T4 = 343.15 #K
P = pi*d #m
A = 1.963*10**(-11) #m
beta = (h*P/(k*A))**(1/2)
deltax = L/4 #m
sigma = -2-(beta)**2*(deltax)**2

"Forming vectors for diagonals"

maindiag = array([1,sigma,sigma,sigma,1])
upperdiag = array([0,1,1,1])
lowerdiag = array([1,1,1,0])

"Forming diagonal matrices"

matrix1 = diag(maindiag, 0)
matrix2 = diag(upperdiag,+1)
matrix3 = diag(lowerdiag,-1)

"Adding the diagonal matrices"

matrix = matrix1 + matrix2 + matrix3
print("the coefficient matrix is")
print(matrix)
print("")

"Solving the matrix equation Ax = b"

b = transpose(array([T0-Ta, 0, 0, 0, T4-Ta]))

solution = linalg.solve(matrix,b)
print("temperature difference is")

print(solution)

print("temperature distribution is")
tdist = solution + Ta
print(tdist)

"Plotting the distribution over length"

def analsol(x):
    top = (T0-T4)*sinh(beta*x)+solution[1]*sinh(beta*(L-x))
    bottom = sinh(beta*L)
    return top/bottom

xinput = array([0,0.00025,0.0005,0.00075,.001])

analdif = analsol(xinput)
analsolution = analdif+Ta

print("anal dif")
print(yanal)
print("my dif")
print(solution)

plt.plot(xinput, tdist)
plt.plot(xinput, analsolution)

