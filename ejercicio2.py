import numpy as np

ventas = np.array([[100,200,500,600,100,50,60,80,0,20,11,21],
                    [200,300,400,504,680,700,100,200,300,670,500,600],
                    [10,200,300,50,500,600,60,880,300,67,590,600],
                    [700,200,300,0,560,67,90,540,300,40,500,640],
                    [100,200,300,400,500,600,0,110,300,650,560,600],
                    [100,20,333,4,508,600,100,200,30,400,500,608]
                    ])

#Axis 1 es para filas, axis 0 es para columnas

#Sum es para sumar los datos
print(f"Venta total por vendedor: {ventas.sum(axis=0)}")
print(f"Venta total por mes: {ventas.sum(axis=1)}")
print("\n")

#Argmax es para sacar el indice del valor maximo
print(f"Mejor vendedor: {ventas.argmax(axis=0)}")
print("\n")

#Argmin es para sacar el indice del valor minimo
print(f"Peor vendedor: {ventas.argmin(axis=0)}")
print("\n")

#Mean es para sacar el promedio de los datos
print(f"Promedio de mes: {ventas.mean()}")