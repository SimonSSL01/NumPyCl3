import numpy as np

#Una universidad tiene 40 estudiantes y 5 asignaturas, tendra una matriz de 40x5 
estudiantes = np.random.randint(0, 6, size=(40, 5))

print(f"Promedio por estudiante: {estudiantes.mean(axis=1)}")
print(f"Promedio por asignatura: {estudiantes.mean(axis=0)}")
print(f"Mejor estudiante: {estudiantes.argmax(axis=1)}")
print(f"Peor estudiante: {estudiantes.argmin(axis=1)}")
print(f"Numero de aprobados: {np.sum(estudiantes >= 5)}")
print(f"Numero de reprobados: {np.sum(estudiantes < 5)}")