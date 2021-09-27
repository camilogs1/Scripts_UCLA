from Tienda.precios import registrar_precios


from precios import *

def registrar():

    nombre=input("Añadir producto: ")
    precio=input("Añadir precio del producto: ")

    registrar_precios(nombre, precio)