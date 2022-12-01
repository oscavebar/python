## Comentario

### Se importan la librería del S.O.

import os
os.system("clear")

from datetime import date
from datetime import datetime

### Aqúi se guardan los valores de temperatura introducidos en una lista, hasta que se escriba 100.
temperatura = 0
lista = []
while temperatura != 100:
    temperatura = int(input("Indique las temperaturas (Cuando ponga 100 se dejará de preguntar: "))
    if temperatura != 100:
        lista.append(temperatura)

### Se guardan las variables de fecha y hora
fecha = date.today()
now = datetime.now()
hora = now.strftime("%H:%M")


### Se guardan variables con los valores requeridos de las listas.
cantidad = len(lista)
maxima = max(lista)
minima = min(lista)
media = sum(lista)/float(len(lista))

### Se presenta en pantalla en informe.
print("Informe de temperaturas del Parque Nacional de Doñana: ")
print(" ")
print("Fecha: ", fecha)
print("Hora: ", hora)
print("Temperaturas tomadas: ", cantidad)
print("Temperatura máxima: ", maxima)
print("Temperatura mínima: ", minima)
print("Temperatura media: ", media)


### Se crea una tupla con los resultados y son enviados a un fichero externo.
lista2 = [str(fecha), ",", str(hora), ",", str(cantidad), ",", str(maxima), ",", str(minima), ",", str(media)]

archivo = open("./temperaturas.txt", "w", encoding="utf-8")
archivo.writelines(lista2)
archivo.close()


## Ejecución

![Ejecución](/imagenes/temperatura1.png)
![Ejecución2](/imagenes/temperatura2.png)

