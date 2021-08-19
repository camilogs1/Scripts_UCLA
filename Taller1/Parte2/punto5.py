x= float(input("\tIntroducir dos numeros para relaizar operaciones\nNumero 1: "))
y= float(input("Numero 2: "))

suma = x+y
resta = x-y
mult = x*y
divi = x/y
pot = x**y
derx = x>>1
dery = y>>1
izqx = x<<1
izqy = y<<1

print("La suma de {0} y {1} es: {2}".format(x,y,suma))    
print("La resta de {0} y {1} es: {2}".format(x,y,resta))    
print("La multiplicación de {0} y {1} es: {2}".format(x,y,mult))    
print("La división de {0} y {1} es: {2}".format(x,y,divi))
print("La potencia de {0} a la {1} es: {2}".format(x,y,pot))    

###  INCOMPLETO