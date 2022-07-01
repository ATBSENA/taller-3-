print()
print("Evidencia_taller_3 y solucion: ")
print()

import os
contenidocarpeta= os.listdir('/Users/User/Desktop/andresBernalAprendiz')
print()

ruta='C:/Users/User/Desktop/AndresBernalAprendiz'


print("1. lista de archivos de la carpeta AndresBernalAprendiz: ",contenidocarpeta)
print()
print("Nombres, extenciones y ruta de los archivos contenidos en la carpeta: ")
print()

for archivo in contenidocarpeta:
    nombre, extension = os.path.splitext(archivo)
    print("El nombre del archivo es '{}' y la extension es '{}', su ruta es: {}".format(nombre, extension, ruta))

print()
print("2. Este es el contenido del archivo Usuarios.csv: ")
print()
import csv
from operator import delitem

with open('Usuarios.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print()
print("3. Esta es la informacion solicitada, del archivo Usuarios.csv, con las columnas solicitadas: ")
print()
import csv

with open('Usuarios.csv') as f:
    reader = csv.reader(f, delimiter=';')
    cantidad_columnas= len('Usuarios.csv')-1
    for row in reader:
        print("{0}, {1}, {2}, {3}".format(row[1], row[2], row[4], row[10]), "Cantidad de columnas por usuario: ", cantidad_columnas)