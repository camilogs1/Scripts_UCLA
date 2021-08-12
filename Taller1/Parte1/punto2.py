a = float(input("Ingrese el coeficiente de X²: "))
b = float(input("Ingrese el coeficiente de x: "))
c = float(input("Ingrese el valor individual: "))

x1 = (-b + (b**2 - (4*a*c))**0.5)/2*a
x2 = (-b - (b**2 - (4*a*c))**0.5)/2*a

print("La primera raiz es: " , x1)
print("La segunda raiz es: " , x2)