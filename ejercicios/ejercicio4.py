import numpy as np

inventario = np.random.randint(0, 100, size=(15, 8))

#np.where es para encontrar el indice de un valor y max es para encontrar el valor maximo
print(f"Producto con mayor existencia: {np.where(inventario == inventario.max())}")

#np.where es para encontrar el indice de un valor y min es para encontrar el valor minimo
print(f"Sucursal con menor inventario: {np.where(inventario == inventario.min())}")

#np.sum es para sumar los valores
print(f"Inventario total: {inventario.sum()}")

#np.mean es para sacar el promedio de los valores
print(f"Inventario promedio: {inventario.mean()}")

#np.where es para encontrar el indice de un valor y 0 es para encontrar el valor minimo
print(f"Productos agotados: {np.where(inventario == 0)}")