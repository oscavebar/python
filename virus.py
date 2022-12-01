
# Se importan la librería de sistema y random

import os
os.system("clear")

import random


# A continuación se crea el genoma aleatorio
longitud = 50
caracteres = "cuga"
cadena = " "
for _ in range(longitud):
    cadena += random.SystemRandom().choice(caracteres)


# Aquí se busca la variante del covid y se determina si el resultado es positivo o negativo
busqueda = cadena.find("ccucggcgggca")

if busqueda != -1:
    resultado = "Positivo"
else:
    resultado = "Negativo"

# Se importan las librerías para la fecha y para la hora
from datetime import date
from datetime import datetime

now = datetime.now()
fecha = date.today()
hora = now.strftime("%H:%M")


# Se pregunta el codigo de paciente
codigo_paciente = int(input("Codigo de paciente: "))

os.system("clear")


# Se crea el informe por pantalla con los resultados.
print("Informe de virus COVID: ")
print (" ")
print("Fecha: ", fecha)
print("Hora: ", hora)
print("Código de paciente: ", codigo_paciente)
print("Resultado: ", resultado)
if resultado == "Positivo":
    print("Positivo: Sí sen encuentra restos de la variante de COVID")
else:
    print("Negativo: No se encuentra restos de la variante de COVID")

lista = [str(fecha), hora, codigo_paciente, resultado]

print(lista)