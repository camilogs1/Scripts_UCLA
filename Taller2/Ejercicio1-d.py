def agregar_estudiantes(nombre, apellido, id, curso, cod_curso, direccion, ciudad):
    nombre.append(input("Ingrese nombre del estudiante: "))
    apellido.append(input("Ingrese el apellido del estudiante: "))
    id.append(int(input("Ingrese el id del estudiante: ")))
    curso.append(input("Ingrese el curso: "))
    cod_curso.append(int(input("Ingrese codigo del curso: ")))
    direccion.append(input("Ingrese direccion de la residencia: "))
    ciudad.append(input("Ciudad donde reside: "))
    datos1 = dict(Nombre=nombre, Apellido=apellido, id_estudiante=id,Curso=curso, 
    codigo_curso=cod_curso, Direccion=direccion, Ciudad=ciudad)
    return datos1

def agregar_notas(id, nota1, nota2, nota3, nota4, nota5):
    id_v=int(input("Ingrese el id del estudiante: "))
    for i in id:
        if id_v in id:
            nota1.append(int(input("Ingrese la nota del estudiante: ")))
            nota2.append(int(input("Ingrese la nota del estudiante: ")))
            nota3.append(int(input("Ingrese la nota del estudiante: ")))
            nota4.append(int(input("Ingrese la nota del estudiante: ")))
            nota5.append(int(input("Ingrese la nota del estudiante: ")))
            notas= dict(id=id, Nota1=nota1, Nota2=nota2, Nota3=nota3, Nota4=nota4, Nota5=nota5)
            return notas
        else:
            aux=1
    if aux == 1:
        print("Ingrese una id existente")
    

def calcular_promedio(datos_b, total, id):
    #hallar posicion del id buscado para hallar promedio
    total=0
    aux = datos_b['id']
    aux = aux.index(id)
    datos_b = list(datos_b.values())
    for j in range(1,len(datos_b)):
        aux1=datos_b[j][aux]
        total += aux1
    total = total/5
    return total

def ver_datos(datos, notas, promedio):
    print("Los datos del estudiante son: " + str(datos))
    print("Las notas del estudiante son: " + str(notas))
    #print("El promedio total de los estudiante es de: " + str(promedio))
        

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