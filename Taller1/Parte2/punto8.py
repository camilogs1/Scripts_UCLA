count = 0
suma = 0

for m in range(1,100):
        
    for  i in range(1,m):
        if m%i == 0:
            count +=1
        
    if count ==1:
        suma = suma +m

    count=0    

print(suma)    

    