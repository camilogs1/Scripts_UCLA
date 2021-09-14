def operacion():
    print("\t Menu registro")
    print("Opción 1 -> Ingresar nuevo producto")
    print("Opción 0 -> Salir")
    aux1 = 0
    i = int(input("Eliga una opción valida: "))
    while i != 0:
        if i == 1 :
            print("\t Seleccione un producto valido en minusculas")
            aux = input("-> ")
            if aux == 'leche':
                aux1 = aux1 + 2500
            elif aux == 'huevos':
                aux1 = aux1 + 1500
            elif aux == 'carne':
                aux1 = aux1 + 4500
            elif aux == 'pollo':
                aux1 = aux1 + 4000
            elif aux == 'arepas':
                aux1 = aux1 + 1000

        print("Opción 1 -> Ingresar nuevo producto")
        print("Opción 0 -> Salir")
        i = int(input("Eliga una opción valida: "))
    return aux1

def precios():
    print("leche -> 2.500")
    print("huevos -> 1.500")
    print("carne -> 4.500")
    print("pollo -> 4.000")
    print("arepas -> 1.000")

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