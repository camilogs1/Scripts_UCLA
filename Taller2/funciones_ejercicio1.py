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