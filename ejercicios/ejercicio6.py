import numpy as np

grises = np.random.randint(0,255, size=(15,15))

#Clip es para que los valores no se salgan del rango de 0 a 255
#Transpose es para obtener la imagen transpuesta

#Se imprime la imagen original
print(f"Imagen original: \n {grises}")

#Se suma 50 a cada valor de la imagen
print(f"\nImagen con brillo incrementado: \n {grises + 50}")

#Se resta 50 a cada valor de la imagen
print(f"\nImagen con brillo disminuido: \n {grises - 50}")

#Se resta cada valor de la imagen a 255
print(f"\nImagen invertida: \n {255 - grises}")

#Se transpone la imagen
print(f"\nImagen transpuesta: \n {grises.T}")