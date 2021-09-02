count = 0
suma = 0

for m in range(1,100):
        
    for  i in range(1,m):
        if m%i == 0:
            count +=1
        
    if count ==1:
        suma = suma +m
        print(m)    
    count=0    

print("La suma de los numeros primos del 1 al 100 es: ",suma)    

    