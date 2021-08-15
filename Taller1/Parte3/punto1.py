def convertir (n):
    enteros = [5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ['V', 'IV','M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    numeral = ''
    i = 0

    while n > 0:
        for _ in range(n // enteros[i]):
            numeral += romanos[i]
            n -= enteros[i]
        i += 1
    return numeral

def ingreso():
    print("La conversión a numeros romanos del numero ingresado es: " + convertir(n))

i = 1
while (i == 1):
    n = input("Ingrese un numero entero: ")
    n = int(n)
    if n < 5000:
        ingreso()
        i += 1
    else:
        print("El numero tiene que ser menor a 5000")