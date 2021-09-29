import numpy as np
import pandas as pd

def sintomas_defecto():
    gripa = ['fiebre', 'malestar', 'congestion nasal', 'debilidad', 'dolor en la garganta']
    covid = ['perdida de olores', 'diarrea', 'congestion nasal', 'debilidad', 'perdida de sabores']
    diabetes = ['sed','malestar','sueño','picor en el cuerpo','azucar elevada']
    cancer = ['perdida de peso','dolores','sangrado','inapetencia','perdida de cabello']
    sida = ['desaliento','ulceras','perdida de peso','vomito','fiebre']
    enfermedades = dict(Gripa=gripa, Covid=covid, Diabetes=diabetes, Cancer=cancer, Sida=sida)
    return enfermedades

def adicionar_enfermedad(enfermedades):
    new=[]
    nom=input("Ingrese una enfermedad: ")
    print("\tSe debe añadir 5 sintomas")
    s1=input("Ingrese los sintomas: ")
    s2=input("Ingrese los sintomas: ")
    s3=input("Ingrese los sintomas: ")
    s4=input("Ingrese los sintomas: ")
    s5=input("Ingrese los sintomas: ")
    new = [s1, s2, s3, s4, s5]
    enfermedades[nom] = new
    return enfermedades


def guardar(enfermedades):
    #np.save('enfermedades.npy', enfermedades)
    #panda = pd.DataFrame(enfermedades)
    #panda.to_excel('enfermedades.xlsx')
    with open('miarchivo.txt', 'w') as archivo:
        archivo.write(str(enfermedades))
    #enfermedades_disco = np.load('enfermedades.npy', allow_pickle='TRUE')
    #print(enfermedades_disco)
