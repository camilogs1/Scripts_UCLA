def agregar_estudiantes():
    nombre=input("Ingrese nombre del estudiante: ")
    apellido=input("Ingrese el apellido del estudiante: ")
    id=int(input("Ingrese el id del estudiante: "))
    curso=input("Ingrese el curso: ")
    cod_curso=int(input("Ingrese codigo del curso: "))
    datos1 = dict(Nombre=nombre, Apellido=apellido, id_estudiante=id,Curso=curso, codigo_curso=cod_curso)
    direccion=input("Ingrese direccion de la residencia: ")
    ciudad=input("Ciudad donde recide: ")
    datos2 = dict(Direccion=direccion, Ciudad=ciudad)
    return datos1

def agregar_notas(datos_a):
    id_v=int(input("Ingrese el id del estudiante: "))
    for i in datos_a:
        if id_v in datos_a:
            nota1=int(input("Ingrese la nota del estudiante: "))
            nota2=int(input("Ingrese la nota del estudiante: "))
            nota3=int(input("Ingrese la nota del estudiante: "))
            nota4=int(input("Ingrese la nota del estudiante: "))
            nota5=int(input("Ingrese la nota del estudiante: "))
            notas= dict(id=id_v, Nota1=nota1, Nota2=nota2, Nota3=nota3, Nota4=nota4, Nota5=nota5)
            return notas
        else:
            aux=1
    if aux == 1:
        print("Ingrese una id existente")
    

def calcular_promedio(datos_b, promedio):
    j=0
    for j in datos_b:
        aux1=datos_b[j]
        promedio += aux1
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
        #asignar valores
        datos_a = datos.values()
        notas=agregar_notas(datos_a)
    elif i == 3 :
        datos_b = notas
        id_v=int(input("Ingrese el id del estudiante: "))
        print(datos_b)
        total=0
        if id_v in datos_b:
            datos_b.pop('id')
            datos_b = datos_b.values()
            print(datos_b)
            total=calcular_promedio(datos_b, total)
            total = total/5 
            print("El promedio del estudiante es: " + str(total))
        else:
            error=1
        if error == 1:
            print("Ingrese una id existente")  
    elif i == 4 : 
        datos_b.pop('id')
        ver_datos(datos, notas, total)

    print("\n\t Bienvenido")
    print("Opción 1 -> Agregar estudiantes")
    print("Opción 2 -> Agregar notas")
    print("Opción 3 -> Calcular promedios")
    print("Opción 4 -> Ver datos estudiantes")
    print("Opción 0 -> Salir")

    i = int(input("Eliga una opción valida: "))