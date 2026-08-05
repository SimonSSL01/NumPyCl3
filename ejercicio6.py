import numpy as np

grises = np.random.randint(0,255, size=(15,15))

#Clip es para que los valores no se salgan del rango de 0 a 255
#Transpose es para obtener la imagen transpuesta

print(f"Imagen original: \n {grises}")
print(f"\nImagen con brillo incrementado: \n {grises + 50}")
print(f"\nImagen con brillo disminuido: \n {grises - 50}")
print(f"\nImagen invertida: \n {255 - grises}")
print(f"\nImagen transpuesta: \n {grises.T}")