salario = int(input("Ingrese la renta anual del trabajador: "))

if (salario < 10000):
    print("El impositivo es del 5%")
elif (10000 <= salario >= 20000):
    print("El impositivo es del 15%")
elif (20000 < salario >= 35000):
    print("El impositivo es del 20%")
elif (35000 < salario >= 60000):
    print("El impositivo es del 30%")
elif (salario > 60000):
    print("El impositivo es del 45%")