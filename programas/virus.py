import os
os.system("clear")

import random


longitud = 50
caracteres = "cuga"
cadena = " "
for _ in range(longitud):
    cadena += random.SystemRandom().choice(caracteres)


busqueda = cadena.find("ccucggcgggca")

if busqueda != -1:
    resultado = "Positivo"
else:
    resultado = "Negativo"


from datetime import date
from datetime import datetime

now = datetime.now()
fecha = date.today()
hora = now.strftime("%H:%M")


codigo_paciente = int(input("Codigo de paciente: "))

os.system("clear")


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