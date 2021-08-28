n = int(input("Ingrese el valor de n: "))
m = int(input("Ingrese el valor de m: "))

i=1
k=0
for i in range(n):
    k = i + (k +1)
    i += 1

j=1
for j in range(m):
    j += 1
    k *= j

print("El resultado es: " + str(k))