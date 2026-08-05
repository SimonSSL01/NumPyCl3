import numpy as np

estudiantes = np.random.randint(0, 6, size=(40, 5))

#Axis 1 es para filas, axis 0 es para columnas

#Mean es para sacar el promedio de los datos
print(f"Promedio por estudiante: {estudiantes.mean(axis=1)}")
print(f"Promedio por asignatura: {estudiantes.mean(axis=0)}")

#Argmax es para sacar el indice del valor maximo
print(f"Mejor estudiante: {estudiantes.argmax(axis=1)}")

#Argmin es para sacar el indice del valor minimo
print(f"Peor estudiante: {estudiantes.argmin(axis=1)}")

#Sum es para sumar los datos y se usa np.sum en vez de estudiantes.sum porque es mas rapido
print(f"Numero de aprobados: {np.sum(estudiantes >= 5)}")
print(f"Numero de reprobados: {np.sum(estudiantes < 5)}")