from operaciones import *
from precios import *

print("\n\t Bienvenido a la tienda")
print("Opción 1 -> Ver precios de los productos")
print("Opción 2 -> Registrar productos")
print("Opción 0 -> Salir")

i = int(input("Eliga una opción valida: "))

while i != 0 :

    if i == 1 :
        precios()
    elif i == 2 :
        total = operacion()
        print("El total a pagar es: " + str(total))
    else :
        print("Ingrese una opción valida")

    print("\n\t Bienvenido de nuevo")
    print("Opción 1 -> Ver precios de los productos")
    print("Opción 2 -> Registrar productos")
    print("Opción 0 -> Salir")

    i = int(input("Eliga una opción valida: "))