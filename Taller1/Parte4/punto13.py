class Encriptar():

    def encriptar(self,txt):
        aux = ''
        for letra in txt :
            x = self.convertir_a_Binario(ord(letra))
            aux = aux + str(x) + " "

        return aux

    def convertir_a_Binario(self,dec):
        aux = ''
        temp1 = dec
        temp = 0
        i = 0
        while i < 8 :
            temp = temp1 % 2
            aux = aux + str(temp)
            if temp1==dec :
                temp1 = dec//2
            else :
                temp1 = temp1//2

            i = i + 1


        return (self.invertir(aux))

    def invertir(self,var):
        return var[::-1]


class Desencriptar() :

    def Desencriptar(self,num):
        x = num.split()
        aux = ''
        for i in range (len(x)) :
            aux = aux + chr(self.convertir_a_Decimal(int(x[i])))

        return aux



    def convertir_a_Decimal(self,num):
        dec = 0
        i = 0
        for iterator in self.invertir(str(num)) :
            if(int(iterator) == 1):
                dec = dec + 2 ** i

            i = i + 1

        return dec

    def invertir(self,var):
        return var[::-1]


n = Encriptar()
x = Desencriptar()

print("Opción 1 -> Encriptar texto")
print("Opción 2 -> Desencriptar texto en binario")
print("Opción 0 -> Salir")

i = int(input("Eliga una opción valida: "))

while i != 0 :

    if i == 1 :
        print(n.encriptar(input("Introduzca el texto a encriptar: ")))
    elif i == 2 :
        print(x.Desencriptar(input("Introduzca el texto a desencriptar: ")))
    else :
        print("Ingrese una opción valida")

    print("\nOpción 1 -> Encriptar texto")
    print("Opción 2 -> Desencriptar texto en binario")
    print("Opción 0 -> Salir")

    i = int(input("Eliga una opción valida: "))