def sintomas_defecto():
    gripa = dict(sintoma1='fiebre', sintoma2='malestar', sintoma3='congestion nasal',
    sintoma4='debilidad', sintoma5='dolor en la garganta')

    covid = dict(sintoma1='fiebre', sintoma2='debilidad', sintoma3='perdida del sabor',
    sintoma4='diarrea', sintoma5='perdida del olfato')

    enfermedades = [gripa, covid]

    print(gripa)
    print(covid)

    a=input("Ingrese: ")
    i=0
    for i in enfermedades:
        if a in enfermedades:
            print(a)
        else:
            aux=1
    if aux == 1:
        print("No dio")




print("\n\t Pruebas")
print("Opción 1 -> Adicionar sintomas")
print("Opción 2 -> Adicionar enfermedades")
print("Opción 3 -> Mostar historial")
print("Opción 4 -> Mostrar relaciones")
print("Opción 0 -> Salir")

i = int(input("Eliga una opción valida: "))
while i != 0 :
    if i == 1 : 
        sintomas_defecto()
    elif i == 2 :
        b=0
    elif i == 3 : 
        c=0
    elif i == 4 : 
        d=0
    print("\n\t Pruebas")
    print("Opción 1 -> Adicionar sintomas")
    print("Opción 2 -> Adicionar enfermedades")
    print("Opción 3 -> Mostar historial")
    print("Opción 0 -> Salir")
    
    i = int(input("Eliga una opción valida: "))