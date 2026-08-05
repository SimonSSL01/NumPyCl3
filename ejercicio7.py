import numpy as np

#uniform es para generar numeros aleatorios en un rango determinado y el randint es para generar numeros enteros aleatorios en un rango determinado
mediciones = np.random.uniform(0,1, size=100)

print(f"Sensores fuera del rango permitido: {np.where((mediciones < 0.1) | (mediciones > 0.9))}")
print(f"Promedio: {mediciones.mean()}")
print(f"Desviacion estandar: {mediciones.std()}")
print(f"Cantidad de sensores criticos: {np.where(mediciones < 0.1)}")