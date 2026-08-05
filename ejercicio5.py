import numpy as np

produccion = np.random.randint(0, 100, size=(30, 3))

#Axis 1 es para filas, axis 0 es para columnas

#Sum es para sumar los datos
print(f"Produccion diaria: {produccion.sum(axis=1)}")
print(f"Produccion semanal: {produccion.sum(axis=0)}")
print(f"Produccion mensual: {produccion.sum()}")

#Argmax es para sacar el indice del valor maximo
print(f"Linea mas productiva: {produccion.argmax(axis=0)}")