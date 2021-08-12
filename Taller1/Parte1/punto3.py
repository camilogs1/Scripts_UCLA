horas = float(input("Ingrese el total de horas trabajadas: "))
valor = float(input("Ingrese el valor por cada hora: "))

sueldo = horas * valor
print("El salario bruto es de: ", sueldo)
aux = sueldo * 0.31
print("Las deducciones son de: ", aux)
sueldo -= aux
if (sueldo <= 300):
    aux = sueldo * 0.2
    print("El salario neto sin la bonificación es de: ", sueldo)
    sueldo += aux
    print("El salario neto más la bonificación es de: ", sueldo)
else:
    print("El salario neto es de: ", sueldo)