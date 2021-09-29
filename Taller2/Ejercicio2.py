import numpy as np
import pandas as pd
from funciones_ejercicio2 import *

print("\n\t Pruebas")
print("Opción 1 -> Adicionar enfermedades y sintomas")
print("Opción 2 -> Mostar historial enfermedades")
print("Opción 3 -> Guardar sintomas")
print("Opción 0 -> Salir")

i = int(input("Eliga una opción valida: "))
enfermedades = sintomas_defecto()
while i != 0 :
    if i == 1 : 
        adicionar_enfermedad(enfermedades)
    elif i == 2 :
        print(enfermedades)
    elif i == 3 : 
        guardar(enfermedades)

    print("\n\t Pruebas")
    print("Opción 1 -> Adicionar enfermedades y sintomas")
    print("Opción 2 -> Mostar historial enfermedades")
    print("Opción 3 -> Guardar sintomas")
    print("Opción 0 -> Salir")
    
    i = int(input("Eliga una opción valida: "))