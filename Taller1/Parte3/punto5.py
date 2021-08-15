from sympy import *

print("Ingrese los valores de la primera matriz 3x3")
a = input("Ingrese un a1: ")
b = input("Ingrese un a2: ")
c = input("Ingrese un a3: ")
d = input("Ingrese un b1: ")
e = input("Ingrese un b2: ")
f = input("Ingrese un b3: ")
g = input("Ingrese un c1: ")
h = input("Ingrese un c2: ")
i = input("Ingrese un c3: ")

M = Matrix([[a, b, c], [d, e, f], [g, h, i]])

print("Ingrese los valores de la segunda matriz 3x3")
j = input("Ingrese un a1: ")
k = input("Ingrese un a2: ")
l = input("Ingrese un a3: ")
m = input("Ingrese un b1: ")
n = input("Ingrese un b2: ")
o = input("Ingrese un b3: ")
p = input("Ingrese un c1: ")
q = input("Ingrese un c2: ")
r = input("Ingrese un c3: ")
N = Matrix([[j, k, l], [m, n, o], [p, q, r]])

A = M * N
B = M + N
C = M - M
#falta producto punto

print("La multiplicación entre las matrices es " + str(A))
print("La suma entre las matrices es " + str(B))
print("La resta entre las matrices es " + str(C))
#print("El producto punto entre las matrices es " + D)