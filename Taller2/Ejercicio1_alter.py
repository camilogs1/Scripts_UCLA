def agregar_estudiantes():
    nombre=input("Ingrese nombre del estudiante: ")
    apellido=input("Ingrese el apellido del estudiante: ")
    curso=input("Ingrese el curso: ")
    cod_curso=(input("Ingrese codigo del curso: "))
    direccion=input("Ingrese direccion de la residencia: ")
    ciudad=input("Ciudad donde reside: ")
    datos1 =(nombre, apellido, curso, cod_curso, direccion, ciudad)
    return datos1

def agregar_notas():
    nota1=int(input("Ingrese la nota del estudiante: "))
    nota2=int(input("Ingrese la nota del estudiante: "))
    nota3=int(input("Ingrese la nota del estudiante: "))
    nota4=int(input("Ingrese la nota del estudiante: "))
    nota5=int(input("Ingrese la nota del estudiante: "))
    notas =(nota1, nota2, nota3, nota4, nota5)
    return notas

def calcular_promedio(datos_b):
    promedio=0
    i=0
    for i in datos_b:
        aux=datos_b[i]
        promedio += aux
    promedio = promedio/5
    return promedio

def ver_datos(datos, notas, promedio):
    print("Los datos del estudiante son: " + str(datos))
    print("Las notas del estudiante son: " + str(notas))
    print("El promedio total de estudiante es de: " + str(promedio))
        
print("\n\t Bienvenido")
print("Opción 1 -> Agregar estudiantes")
print("Opción 2 -> Agregar notas")
print("Opción 3 -> Calcular promedios")
print("Opción 4 -> Ver datos estudiantes")
print("Opción 0 -> Salir")

i = int(input("Eliga una opción valida: "))

while i != 0 :

    if i == 1 :
        datos=agregar_estudiantes()
    elif i == 2 :
        notas=agregar_notas()
    elif i == 3 :
        total=calcular_promedio(notas)
        print("El promedio del estudiante es: " + str(total))
    elif i == 4 : 
        ver_datos(datos, notas, total)

    print("\n\t Bienvenido")
    print("Opción 1 -> Agregar estudiantes")
    print("Opción 2 -> Agregar notas")
    print("Opción 3 -> Calcular promedios")
    print("Opción 4 -> Ver datos estudiantes")
    print("Opción 0 -> Salir")

    i = int(input("Eliga una opción valida: "))