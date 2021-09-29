from sympy import *

def menu():
    print("\nMenu\n1. Añadir Productos")
    print("2. Vender Producto")
    print("3. Ver Productos")
    print("4. Ver Ganancias")
    print("5. Salir")
    
def añadirProducto(productos):
    print("\n\t__Ingrese nuevo producto y su precio__ ")
    producto = input("Ingrese el nombre del porducto: ")
    valor = int(input("Ingrese valor del producto: "))
    productos.append([producto,valor])
    print("Producto registrado...")
    pprint(productos)
    return(productos)

def venderProducto(productos, ganancias):
    print("\n\t__Vender Producto dentro del stock__")
    print("Productos en almacen...")
    pprint(productos)
    i = int(input("Indique la posicion del producto a vender: "))
    ganancias += productos[i-1][1] 
    productos.pop(i-1)
    return productos, ganancias

def verProductos(productos):
    pprint(productos)    

def verGanancias(ganancias):
    print(ganancias)    