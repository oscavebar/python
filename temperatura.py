import os
os.system("clear")

from datetime import date
from datetime import datetime


temperatura = 0
lista = []
while temperatura != 100:
    temperatura = int(input("Indique las temperaturas (Cuando ponga 100 se dejará de preguntar: "))
    if temperatura != 100:
        lista.append(temperatura)


fecha = date.today()
now = datetime.now()
hora = now.strftime("%H:%M")

cantidad = len(lista)
maxima = max(lista)
minima = min(lista)
media = sum(lista)/float(len(lista))
print("Informe de temperaturas del Parque Nacional de Doñana: ")
print(" ")
print("Fecha: ", fecha)
print("Hora: ", hora)
print("Temperaturas tomadas: ", cantidad)
print("Temperatura máxima: ", maxima)
print("Temperatura mínima: ", minima)
print("Temperatura media: ", media)

lista2 = [str(fecha), ",", str(hora), ",", str(cantidad), ",", str(maxima), ",", str(minima), ",", str(media)]

archivo = open("./temperaturas.txt", "w", encoding="utf-8")
archivo.writelines(lista2)
archivo.close()