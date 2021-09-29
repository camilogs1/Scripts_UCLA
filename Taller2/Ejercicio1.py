from funciones_estudiantes import *

print("\n\t Bienvenido")
print("Opción 1 -> Agregar estudiantes")
print("Opción 2 -> Agregar notas")
print("Opción 3 -> Calcular promedios")
print("Opción 4 -> Ver datos estudiantes")
print("Opción 0 -> Salir")

i = int(input("Eliga una opción valida: "))
#declaracion listas para el guardado de informacion
nombre = []
apellido = [] 
id = []
curso = []
cod_curso = []
direccion= []
ciudad = []
nota1 = []
nota2 = []
nota3 = []
nota4 = []
nota5 = []
total= 0
notas={}
while i != 0 :
    if i == 1 :
        datos=agregar_estudiantes(nombre, apellido, id, curso, cod_curso, direccion, ciudad)
    elif i == 2 :
        notas=agregar_notas(id, nota1, nota2, nota3, nota4, nota5)
    elif i == 3 :
        datos_b = notas
        id_a = datos_b['id']
        id_v=int(input("Ingrese el id del estudiante: "))
        error=0
        if id_v in id_a:
            total=calcular_promedio(datos_b, total, id_v)
            print("El promedio del estudiante es: " + str(total))
        else:
            error=1
        if error == 1:
            print("Ingrese una id existente")  
    elif i == 4 : 
        ver_datos(datos, notas, total)

    print("\n\t Bienvenido")
    print("Opción 1 -> Agregar estudiantes")
    print("Opción 2 -> Agregar notas")
    print("Opción 3 -> Calcular promedios")
    print("Opción 4 -> Ver datos estudiantes")
    print("Opción 0 -> Salir")

    i = int(input("Eliga una opción valida: "))