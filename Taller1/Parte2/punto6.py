print("\tIngrese numeros para ordenar")
n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))
n4 = int(input("Numero 4: "))

lista = []
lista = [n1,n2,n3,n4]

for i in range(1,len(lista)):
    for k in range(len(lista)- i):
        if lista[k] > lista[k+1]:
            aux = lista[k]
            lista[k] = lista[k+1]
            lista[k+1] = aux

print("Numeros ordenados de menor a mayor: ",lista)

for i in range(1,len(lista)):
    for k in range(len(lista)- i):
        if lista[k] < lista[k+1]:
            aux = lista[k]
            lista[k] = lista[k+1]
            lista[k+1] = aux

print("Numeros ordenados de mayor a menor: ",lista)