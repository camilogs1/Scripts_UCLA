from sympy import *
from numpy import *

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

m1 = Matrix([[a, b, c], [d, e, f], [g, h, i]])

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
n1 = Matrix([[j, k, l], [m, n, o], [p, q, r]])

A = m1 * n1
B = m1 + n1
C = m1 - n1

print("\n\tLa multiplicación entre las matrices es: \n")
pprint(A)
print("\n\tLa suma entre las matrices es: \n")
pprint(B)
print("\n\tLa resta entre las matrices es: \n")
pprint(C)