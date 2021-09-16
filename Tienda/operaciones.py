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
        print("Opción 0 -> Ver total a pagar")
        i = int(input("Eliga una opción valida: "))
    return aux1