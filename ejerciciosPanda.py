import pandas as pd
import numpy as np


# d = {'a': 1, 'b': 2, 'c': 3}
# ser = pd.Series(data=d, index=['a', 'b', 'c'])
# print (ser)

ventas = pd.Series([15,12,21], index = ["Ene", "Feb", "Mar"])
print(ventas)
print(ventas[0])
print(ventas['Ene'])
# Objetos de tipo de datos ( dtype)
# describe cómo deben interpretarse los bytes en el bloque de memoria de tamaño fijo correspondiente a un elemento de la matriz. Describe los siguientes aspectos de los datos:
# Tipo de datos (entero, flotante, objeto Python, etc.)
# Tamaño de los datos (cuántos bytes hay en, por ejemplo, el número entero)
# Orden de bytes de los datos ( little-endian o big-endian )

#print(ventas.dtype)
# #Podemos acceder a los objetos que contienen los índices y los valores a través de los atributos index y values de la serie, respectivamente:

#print(ventas.index)
#print(ventas.values)

#ventas.name = "Ventas 2020"
#print(ventas.name)
#print(ventas)

# ventas.index.name = "Meses"
# print(ventas)

# #El atributo axes nos da acceso a una lista con los ejes de la serie (solo contiene un elemento al tratarse de una estructura unidimensional):
#print(ventas.axes)
# # #El atributo shape nos devuelve el tamaño de la serie:

#print(ventas.shape)


#datos = { 'manzanas' : [ 3 , 2 , 0 , 1 ], 'naranjas' : [ 0 , 3 , 7 , 2 ] }

# compras = pd.DataFrame( datos )
# print(compras)


# d = {'a': 1, 'b': 2, 'c': 3}
# ser = pd.Series(data=d, index=['a', 'b', 'c'])
# print (ser)


#compras = pd.DataFrame( datos , index = [ 'Juno' , 'Robert' , 'Lily' , 'David' ])   
#print(compras)

#print(compras.index)
#print(compras.columns)

#print(compras.axes)

# compras.index.name = "Clientes"
# compras.columns.name = "Frutas"
# print(compras)

#print(compras.values)

#print(compras.shape)


#Creacion de una serie
#Utilizando una lista

# s = pd.Series([7,5,3])
# print(s)

# s = pd.Series([7,5,3], index = ["Ene", "Feb", "Mar"])
# print(s)


#Diccionario
# d = {"Ene":7, "Feb":5, "Mar":3 }
# s = pd.Series(d)
# print(s)


# d = {"Ene":7, "Feb":5, "Mar":3 }
# s = pd.Series(d, index = ["Abr", "Mar", "Feb", "Ene"],dtype=int)
# print(s)


# s = pd.Series(7, index = ["Ene", "Feb", "Mar"])
# print(s)

#Creando Dataframe
#Diccionario

# elementos = { 
#     "Numero atomico":[1, 6, 47, 88],
#     "Masa atomica":[1.008, 12.011, 107.87, 226],
#     "Familia":["No metal", "No metal", "Metal", "Metal"]
# }
#print(elementos)

# tabla_periodica = pd.DataFrame(elementos)
# print(tabla_periodica)

# tabla_periodica = pd.DataFrame(elementos,
#                                index = ["H", "C", "Ag", "Ra"],
#                                columns = ["Familia", "Numero atomico", "Masa atomica"]
# )
# print(tabla_periodica)


#Utilizando un array Numpy

# import numpy as np

# unidades_Datos = np.array([[2, 5, 3, 2],
#                          [4, 6, 7, 2], 
#                           [3, 2, 4, 1]])
#print(unidades_Datos)

# unidades = pd.DataFrame(unidades_Datos)
# print(unidades)

# unidades = pd.DataFrame(unidades_Datos, index = [2015, 2016, 2017], columns = ["Ag", "Au", "Cu", "Pt"])
# print(unidades)


#Utilizando diferentes diccionarios

# unidades_2015 = {"Ag":2, "Au":5, "Cu":3, "Pt":2}
# unidades_2016 = {"Ag":4, "Au":6, "Cu":7, "Pt":2}
# unidades_2017 = {"Ag":3, "Au":2, "Cu":4, "Pt":1}

# unidades = pd.DataFrame([unidades_2015, unidades_2016, unidades_2017],
#                        index = [2015, 2016, 2017])
# print(unidades)


# unidades_2015 = {"Ag":2, "Au":5, "Cu":3, "Pt":2}
# unidades_2016 = {"Ag":4, "Au":6, "Cu":7, "Pt":2}
# unidades_2017 = {"Ag":3, "Pb":2, "Cu":4, "Pt":1}

# unidades = pd.DataFrame([unidades_2015, unidades_2016, unidades_2017],
#                        index = [2015, 2016, 2017])
# print(unidades)


#HEAD


# entradas = pd.Series([11, 18, 12, 16, 9, 16, 22, 28, 31, 29, 30, 12],
#             index = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago",
#              "sep", "oct", "nov", "dic"])
# #print(entradas)

# salidas = pd.Series([9, 26, 18, 15, 6, 22, 19, 25, 34, 22, 21, 14],
#             index = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago",
#              "sep", "oct", "nov", "dic"])
# #print(salidas)
# almacen = pd.DataFrame({"entradas": entradas, "salidas": salidas})
# almacen["neto"] = almacen.entradas - almacen.salidas
#print(almacen)

#print(entradas.head(2))
#print(almacen.head(2))

# tail

#print(entradas.tail(7))
#print(almacen.tail(7))

#sample
#print(entradas.sample(5))
#print(almacen.sample(5))

#Describe
#print(almacen.describe())

#info
#print(almacen.info())

#El método value_counts
# s = pd.Series([3, 1, 2, 1, 1, 4, 1, 2, np.nan])
# print(s)
#print(s.value_counts())

# print(s.value_counts(dropna = False))

#print(s.value_counts(bins = 2))

#Seleccion series
# s = pd.Series([10, 20, 30, 40])
# print(s)

# print(s[0])
# print(s[2])

# s = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "d"])
# #print(s)

# print(s["a"],s[0])
# print(s["d"],s[3])

#s = pd.Series([10, 20, 30, 40], index = [3, 2, 1, 0])
# print(s)
#print(s[0])


#Uso de rangos

#s = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "d"])
#print(s)
#print(s[1:3])
# print(s[1:])
# print(s[:3])
#print(s["a":"c"])
#print(s[:"c"])
#print(s["b":])

# print(s.get(1)) 
# print(s.get("b"))

#Metodo loc

# s = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "d"])
# print(s)
# print(s.loc["b"])
##print(s.loc[0])

#Medoto iloc

#s = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "d"])
# print(s)
# print(s.iloc[1])
# print(s.iloc[0])
# print(s.iloc[3])

# print(s.iloc[-1])
# print(s.iloc[-4])


#Seleccion de informacion Dataframe

# ventas = pd.DataFrame({
#     "Entradas":[41, 32, 56, 18],
#     "Salidas":[17, 54, 6, 78],
#     "Valoración": [66, 54, 49, 66],
#     "Límite": ["No", "Si", "No", "No"],
#     "Cambio": [1.43, 1.16, -0.67, 0.77]},
#     index = ["Ene", "Feb", "Mar", "Abr"])
# #print(ventas)

# #print(type(ventas["Entradas"]))
# #print(ventas["Entradas"])

# print(ventas["Entradas"]["Feb"])
# #Sin embargo, la más que razonable opción de eliminar los corchetes que separan ambos índices y sustituirlos por una coma no funciona:

# #print(ventas["Entradas","Feb"])
# #Si, una vez seleccionada una columna, le asignamos una lista o array (o serie) de valores de la misma longitud, estamos modificando dicha columna del dataframe:

# ventas["Entradas"] = [33, 25, 40, 12]
# print(ventas)