hora = int(input("Ingrese la hora de inicio del evento: "))
minuto = int(input("Ingrese el minuto de inicio del evento: "))

duracion=int(input("Ingrese la duración del evento en minutos: "))
dura_horas=0

while duracion >=59:
    dura_horas+=1
    duracion-=59
    restante=duracion

if dura_horas>0:
    hora_fin = hora+dura_horas
    min_fin = restante
else:
    hora_fin=hora
    min_fin=minuto+duracion
    if min_fin > 59:
        min_fin-=60
        hora_fin+=1
        

if hora_fin >24:
    hora_fin-=24    

print("La hora de finalización del evento es: ",hora_fin,":",min_fin)


