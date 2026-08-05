from numpy import dtypes
import numpy as np
temperaturas = np.array([25, 28, 30, 22, 26, 29, 31, 24, 27, 32])


# Mean es para sacar el promedio de los datos
print(f"El promedio de clima es de {temperaturas.mean()} grados.")

# Argmax es para sacar el indice del valor maximo
print(f"El dia mas caluroso fue el {temperaturas.argmax()} con {temperaturas.max()} grados.")

# Argmin es para sacar el indice del valor minimo
print(f"El dia mas frio fue el {temperaturas.argmin()} con {temperaturas.min()} grados.")

# Std es para sacar la desviacion estandar de los datos
print(f"La desviacion estandar del clima fue de {temperaturas.std()} grados.")

# Var es para sacar la varianza de los datos
print(f"La varianza del clima fue de {temperaturas.var()} grados.")