import numpy as np

edades = np.random.randint(0,100, size=500)

#Mean es para sacar el promedio de los datos
print(f"Promedio de edad: {edades.mean()}")

#Median es para sacar la mediana de los datos
print(f"Mediana de edad: {np.median(edades)}")

#Mode es para sacar la moda de los datos
#print(f"Moda: {np.mode(edades)}")

#Max es para sacar el valor maximo de los datos
print(f"Edad maxima: {edades.max()}")

#Min es para sacar el valor minimo de los datos
print(f"Edad minima: {edades.min()}")

#Sum es para sumar los datos
print(f"Cantidad de mayores de edad: {np.sum(edades >= 18)}")