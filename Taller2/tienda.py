from funciones import *

def main():
    
    print("\tAdministrador Tienda")
    menu()
    x = int(input("Ingrese opcion valida: "))
    productos = []
    ganancias = 0

    while (x != 5):
        if x == 1:
          productos = añadirProducto(productos)
        elif x == 2:
            productos, ganancias =  venderProducto(productos, ganancias)
        elif x == 3:
            print("\n\tProductos dentro del stock")
            verProductos(productos)
        else:
            verGanancias(ganancias)       

        menu()
        x = int(input("Ingrese opcion valida: "))
        
if __name__ == '__main__':
    main()