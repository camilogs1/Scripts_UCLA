print("\tIngrese los puntos en tres dimensiones para calcular distancia")
x1 = int(input("X1: "))
y1 = int(input("Y1: "))
z1 = int(input("Z1: "))

x2 = float(input("X2: "))
y2 = float(input("Y2: "))
z2 = float(input("Z2: "))

d = float(((x2-(x1))**2+(y2-(y1))**2+(z2-(z1))**2)**0.5)

print("La distancia entre los puntos es: {0:.2f}".format(d))