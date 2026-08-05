import numpy as np

accion = np.random.uniform(0,100, size=100)

#Precio promedio
print(f"Precio promedio: {accion.mean()}")

#Precio maximo
print(f"Precio maximo: {accion.max()}")

#Precio minimo
print(f"Precio minimo: {accion.min()}")

#Variacion porcentual
print(f"Variacion porcentual: {(accion.max() - accion.min()) / accion.min() * 100}")

#Dias donde el precio fue superior al promedio, aca se usa where para encontrar los indices de los valores que cumplen la condicion
print(f"Dias donde el precio fue superior al promedio: {np.where(accion > accion.mean())}")