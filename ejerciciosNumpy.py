import numpy as np

# a = np.array([1, 2, 3])
# #print(a)

# a = np.append (a, [10, 11, 12])

# print(a)


#Añadir una columna
#a = np.array([[1, 2, 3], [4, 5, 6]])
#print(a)

# b = np.array([[400], [800]])

# newArray = np.append(a, b, axis = 1)

# print(newArray)

# a = np.array([[1, 2, 3], [4, 5, 6]])

# b = np.array([[5, 8, 3]])

# newArray = np.append(a, b, axis = 0)

# print(newArray)

# A=np.arange(5)
# print(A)


#import numpy as np

# a = np.array([34, 25, 7])   # Crear una matriz de rango 1
# print(type(a))            # Prints "<class 'numpy.ndarray'>"
# print(a)
# print(a.shape)            # Prints "(3,)" devuelve una tupla con el tamaño del array, pero puede ser también usado para redimensionarlo.

# print(a[0], a[1], a[2])   # Prints "1 2 3"

# a[0] = 5                  # Cambiar un elemento de la matriz
# print(a)                  # Prints "[5, 2, 3]"

# b = np.array([[1,2,3],[4,5,6]])    # Crear una matriz de rango 2
# print(b.shape)                     # Prints "(2, 3)"


# b = np.array([1,2,3])    
# print(b.shape) 
  
# print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

# matriz = np.zeros((3,3))   # Crear una matriz de todos los ceros
# print(matriz)              # Prints "[[ 0.  0.]
#                       #          [ 0.  0.]]"

# b = np.ones((1,2))    # Crear un conjunto de todos ellos
# print(b)              # Prints "[[ 1.  1.]]"

# c = np.full((2,2), 7)  # Crear una matriz constante
# print(c)               # Prints "[[ 7.  7.]
#                        #          [ 7.  7.]]"

 
# d = np.eye(3)         # Crear una matriz de identidad 2x2
# print(d)              # Prints "[[ 1.  0.]
#                       #          [ 0.  1.]]"

# e = np.random.random((2,2))  # Crear una matriz llena de valores aleatorios
# print(e)                     # Podría imprimir "[[ 0.91940167  0.08143941]
#                              #               [ 0.68744134  0.87236687]]"



# E=np.random.rand(10)
# print(E)
# arr = np.random.rand(5)

# A=arr[0]
# print(A)



#Rebanar matrices
#import numpy as np

# Crear la siguiente matriz 
# [[ 1  2  3]
#  [ 5  6  7]
#  [ 9 10 11 ]]
#a = np.array([[1,2,3], [5,6,7], [9,10,11]])

# Usar el rebanado para sacar el subconjunto que consiste en las 2 primeras filas
# y las columnas 1 y 2; b es el siguiente conjunto de forma (2, 2):
# [[2 3]
#  [6 7]]
#b = a[:2, 1:3]
#print(b)


# import random
  
# # prints a random value from the list
# list1 = [1, 2, 3, 4, 5, 6] 
# print(random.choice(list1))
  
# # prints a random item from the string 
# string = "striver" 
# print(random.choice(string))  
# #La salida siempre será diferente ya que el sistema devuelve un elemento aleatorio.


# from numpy import random as r
# print(r.choice(['Andres','Juan','Pedro', 'Mateo'], size= r.choice([1,2],p=[0.1,0.9]) , p=[0.5,0.2,0.2,0.1], replace=False))



# import numpy as np
# arr = np.array([3,5,7])
# print(arr.sum())


# ran=np.random.rand(5,5)
# print(ran)




