import numpy as np

edades = np.random.randint(0,100, size=500)

print(f"Promedio de edad: {edades.mean()}")
print(f"Mediana de edad: {np.median(edades)}")
#print(f"Moda: {np.mode(edades)}")
print(f"Edad maxima: {edades.max()}")
print(f"Edad minima: {edades.min()}")
print(f"Cantidad de mayores de edad: {np.sum(edades >= 18)}")