# lista = []

# for i in range(4, 31, 2):
#     if(i % 3 == 0):
#         lista.append(i ** 2)

# for i in range(len(lista)):
#     print(lista[i])


# mi_lista = []
# for numero in range(4 , 31, 2):
#     if numero%3 == 0:
#         mi_lista.append(numero**2)
# print(mi_lista)





# lista = []
# for i in range(4, 30, 2):
#     if(i % 3 == 0):
#         lista.append(i ** 2)
# print(lista)        

# lista = []
# for x in range(4, 31, 2):
#     cuadrado = x**2
#     if cuadrado%3 == 0:
#         lista.append(cuadrado)

# print(lista)






#Primer ejemplo
# mi_lista = []
# for x in range(4, 31, 2):
#     if x%3 == 0:
#         mi_lista.append(x**2)

# print(mi_lista)
# [36, 144, 324, 576, 900]

#Segundo ejemplo

# mi_diccionario = dict()
# for y in range(3, 11):
#     mi_diccionario[(y, y**3)] = []
#     for x in range(4, 31, 2):
#         if x%y == 0:
#             mi_diccionario[(y, y**3)].append(x**2)

# print(mi_diccionario)


# mi_diccionario = { (y, y**3) : [ x**2 for x in range(4,31,2) if x%y == 0 ] for y in range(3, 11) }
# print(mi_diccionario)


# def dijkstra(unvisited: set, distances: dict, neighbours: dict, start: str) -> tuple:
    
    
#     known = { vertex: 0 if vertex == start else float('inf') for vertex in unvisited }
    
    

   
#     previous = {vertex: None for vertex in unvisited}

    
#     while len(unvisited) > 0:

        
#         distance, visit = min( [ (known[candidate], candidate) for candidate in unvisited] )
        
#         calculated = {neighbour: distance + distances[visit, neighbour] for neighbour in neighbours[visit]}

        
#         previous.update( {vertex: visit if calculated[vertex] < known[vertex] else previous[vertex] for vertex in neighbours[visit]} )
#         known.update( {vertex: calculated[vertex] if calculated[vertex] < known[vertex] else known[vertex] for vertex in neighbours[visit] })

       
#         unvisited.remove(visit)

    
#     return known, previous

# unvisited = {'A', 'B', 'C', 'D', 'E', 'C'}

# distances = {('A', 'B'): 6, ('A', 'D'): 1, ('B', 'C'): 5, ('B', 'D'): 2, ('B', 'E'):2, ('D', 'E'): 1, ('E','C'): 5,
#              ('B', 'A'): 6, ('D', 'A'): 1, ('C', 'B'): 5, ('D', 'B'): 2, ('E', 'B'):2, ('E', 'D'): 1, ('C','E'): 5}

# neighbours = {
#                 'A': ['B', 'D'],
#                 'B': ['A', 'D', 'C'],
#                 'C': ['B', 'E'],
#                 'D': ['A', 'B', 'E'],
#                 'E': ['D', 'B', 'C']
#               }

# minimas, predecesores = dijkstra(unvisited, distances, neighbours, 'A')
# minimas, predecesores = sorted(minimas.items()), sorted(predecesores.items())
# print('Distancias minimas: \n {} \nPredecesores: \n {}'.format(minimas, predecesores))

#Funcion zip

# cadena='hola'
# diccionario=dict(zip(range(len(cadena)),cadena))
# print(diccionario)

# lista=['h','o','l','a']
# diccionario=dict(zip(range(len(lista)),lista))
# print(diccionario)

# tupla=('h','o','l','a')
# diccionario=dict(zip(range(len(tupla)),tupla))
# print(diccionario)

# conjunto={'h','o','l','a'}
# diccionario=dict(zip(range(len(conjunto)),conjunto))
# print(diccionario)

#Envolturas de funciones 

# def suma(val1=0, val2=0):
#     return val1+val2

# def operacion(funcion,val1=0,val2=0):
#     return funcion(val1, val2)
    
    
# funcion_suma= suma
# resultado=operacion(funcion_suma,10,20)
# print(resultado)   

#Para que sirven los asteriscos--------------------------------------------
# txt='texto' * 5
# print(txt)

# def saludar(*nombres): # anteponemos un asterisco al nombre del parámetro

#     print(nombres) # vemos como nombres es una tupla con todos los parámetros recibidos (se han empaquetado)

#     for nombre in nombres: # recorremos la tupla
#         print(f'Hola, {nombre}!') # y saludamos


#saludar('Juan')

# saludar('Juan', 'Laura', 'Lucia')


# def saludar(saludo, *nombres, hora, despedida='Adios...'):
    
#     for nombre in nombres:
#         print(f'{saludo}, {nombre}')

#     print(f'Esta es la hora: {hora}')
#     print(despedida)

#saludar('Buenos días', 'Carlos', 'Manuel', hora='09:15am')
#print()
# saludar('Buenas noches', 'Roberto', 'Fernando', hora='23:30', despedida='Hasta mañana')

# def funcion(p1, p2=10, p3=20):
#     print(f'p1 es {p1}')
#     print(f'p2 es {p2}')
#     print(f'p3 es {p3}')

#llamando a la función pasando p2 y p3 por posicion
#funcion(1, 2, 3)

#print()

# llamando a la función pasando p3 por nombre
# funcion(1, 2, p3=3)



# def saludar(**nombres):
    
#     print(nombres) # vemos como tenemos un diccionario en el parámetro nombres

#     for parametro in nombres:
#         print(f'¡Hola, {nombres[parametro]}!')

# diccionario = {'nombre1':'juan', 'nombre2':'Laura', 'nombre3':'Lucía'}

# saludar(**diccionario)
    




#Funciones lambda----------------------------------------------

#Calculo del area de un triangulo

# def area_triangulo(base, altura):
#     area=base*altura/2
#     return area


# print(area_triangulo(5,7))

#Lambda nunca podra colocar condicionales o while, solo calculos sencillos.
# area_triangulo=lambda base,altura:(base*altura/2)
# print(area_triangulo(5,7))
# triangulo1=area_triangulo(6,8)
# print(triangulo1)

#Funcion que eleve al cubo un numero
# al_cubo=lambda numero:pow(numero,3)
# #al_cubo=lambda numero:numero**3
# print(al_cubo(3))

#comision de un empleado con un formato en concreto entre exclamaciones 
#y le agregue un simbolo de pesos

# destacar_valor=lambda comision:'{}! $'.format(comision)#Le aplica el formato que queremos
# comision_juan=50000

# print(destacar_valor(comision_juan))

# sin_parametros=lambda :True
# print(sin_parametros())


