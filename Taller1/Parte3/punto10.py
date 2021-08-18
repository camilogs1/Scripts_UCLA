nombre = input("Ingrese nombre del producto: ")
precio = float(input("Ingrese precio del producto: "))
num = int(input("Ingrese numero de unidades: "))

coste = precio * num

if num <10:
    print("El nombre del producto es "+ nombre +"\nEl precio del producto es " + str("{0:.2f}".format(precio)) 
    + "\nEl numero de productos solicitados son: 00" + str(num)
    + "\nEl coste total es " + str("{0:.2f}".format(coste)))
elif num <=100:
     print("El nombre del producto es "+ nombre +"\nEl precio del producto es " + str("{0:.2f}".format(precio)) 
    + "\nEl numero de productos solicitados son: 0" + str(num)
    + "\nEl coste total es " + str("{0:.2f}".format(coste)))
else:
    print("El nombre del producto es "+ nombre +"\nEl precio del producto es " + str("{0:.2f}".format(precio)) 
    + "\nEl numero de productos solicitados son " + str(num)
    + "\nEl coste total es " + str("{0:.2f}".format(coste)))