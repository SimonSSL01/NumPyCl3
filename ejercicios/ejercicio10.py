import numpy as np

matriz = np.random.randint(0,100, size=(10,10))
#matriz = np.array(input("Ingrese una matriz: "))

#Se imprime la dimension de la matriz
print(f"Dimension: {matriz.shape}")

#Se imprime el numero de filas
print(f"Numero de filas: {matriz.shape[0]}")

#Se imprime el numero de columnas
print(f"Numero de columnas: {matriz.shape[1]}")

#Se imprime el total de datos
print(f"Total de datos: {matriz.size}")

#Se imprime el valor maximo
print(f"Maximo: {matriz.max()}")

#Se imprime el valor minimo
print(f"Minimo: {matriz.min()}")

#Se imprime el promedio
print(f"Promedio: {matriz.mean()}")

#Se imprime la mediana
print(f"Mediana: {np.median(matriz)}")

#Se imprime la varianza
print(f"Varianza: {matriz.var()}")

#Se imprime la desviacion estandar
print(f"Desviacion estandar: {matriz.std()}")