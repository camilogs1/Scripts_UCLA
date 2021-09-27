from operaciones import *
from precios import *
from registrar import *

print("\n\t Bienvenido a la tienda")
print("Opción 1 -> Ver precios de los productos")
print("Opción 2 -> Registrar nuevos productos")
print("Opción 3 -> Pagar productos")
print("Opción 0 -> Salir")

i = int(input("Eliga una opción valida: "))

while i != 0 :

    if i == 1 :
        mostrar_precios()
    elif i ==2 :
        registrar()
    elif i == 3 :
        total = operacion()
        print("El total a pagar es: " + str(total))
    else :
        print("Ingrese una opción valida")

    print("\n\t Bienvenido a la tienda")
    print("Opción 1 -> Ver precios de los productos")
    print("Opción 2 -> Registrar nuevos productos")
    print("Opción 3 -> Pagar productos")
    print("Opción 0 -> Salir")

    i = int(input("Eliga una opción valida: "))