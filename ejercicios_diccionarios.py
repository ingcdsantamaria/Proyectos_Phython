

# #Diccionario
# def promedioNotas(dicNota):
   
#    n1=dicNota['n1']
#    n2=dicNota['n2']
#    n3=dicNota['n3']
#    n4=dicNota['n4']
   
#    promedio=(n1+n2+n3+n4)/4
#    return(round(promedio,2))


# dicNota  = {
#     'n1': 1.5,
#     'n2': 5,
#     'n3': 2.5,
#     'n4': 4.5
    

# }

# print(promedioNotas(dicNota))





# def reportarPromedio(dicRporte):
#     prom=round(dicRporte['promedio'],2)
#     #return dicRporte['nombre']+' = '+ str(dicRporte['promedio'])
#     return dicRporte['nombre']+' = '+ str(prom)

# def promedioNotas(dicNota):
#    nombre=dicNota['nombre']
#    n1=dicNota['n1']
#    n2=dicNota['n2']
#    n3=dicNota['n3']
#    n4=dicNota['n4']
   
#    promedio=n1+n2+n3+n4/4
#    dicReporte={
#         'nombre':nombre,
#         'promedio':promedio      
#     }
#    return(dicReporte)

# dicNota  = {
#     'nombre':'Pedro Perez',
#     'n1': 1.5,
#     'n2': 5,
#     'n3': 2.5,
#     'n4': 4.5
    

# }

# print(reportarPromedio(promedioNotas(dicNota)))



#diccionario = {'Eduardo': 1, 'Fernando':2, 'Uriel':3, 'Rafael': 4}
#print(diccionario)
# print(diccionario.values())
#print(diccionario.values())
# diccionario.values()


# diccionario = {
#      "clave1":234,
#      "cadena":True,
#      "clave3":"Valor 1",
# }
# print(diccionario)
# print(type(diccionario))
# print(diccionario['clave1'])


# versiones = dict(python=2.7, zope=2.13, plone=5.1)
# print(versiones)
# versiones_adicional = dict(django=2.1)
# print(versiones_adicional)
# versiones.update(versiones_adicional)
# print(versiones)



# persona={
#     'nombre':'Juan Perez',
#     'direccion':'Mz 20b #12',
#     'edad':23       
# }

# nombre=persona['nombre']
# direccion=persona['direccion']

# print(nombre)
# print(direccion)
# print(persona['direccion'])
# print(persona)








#Diccionario--------------------
# diccionario={
#     'azul':'blue',
#     'amarillo':'yellow',
#     'rojo':'red',
#     'verde':'green'
# }

#Quiero saber como se dice amarillo en ingles----------------------

#print(diccionario['amarillo'])
# print(diccionario['azul'])

#Agregar elementos al diccionario---------------------------

# diccionario['cafe']='brown'
# print(diccionario)

# print (diccionario)

#Modificar elementos-------------------------

# diccionario['cafe']='cafe'

# print(diccionario)

#Eliminar un elemento---------------------------- 
#Utilizamos la funcion del()-----------------------

# del(diccionario['azul'])
# print(diccionario)


# white=input("Ingrese la palabra blanco en ingles:")

# diccionario['blanco']=white

# print(diccionario)

# diccionario['cafe']='brown'
# print(diccionario)

#Tuplas
# diccionario_persona={
#     'Felipe':[80, 1.80],
#     'Maria':[60, 1.60],
#     'Fernando':[90, 1.90]   
# }

#print(diccionario_persona)
#print(diccionario_persona['Maria'])

#Excepciones -----------------------------------

# estudiantes={
#     1:'William Guerrero',
#     2:'Sara Sofia Cuayal',
#     3:'Felipe Agrega'
    
# }

#print(estudiantes[1])

#print(estudiantes[4])

#Existe una forma en donde podemos mostrar el valor 
# que pertenece a una clave y si este valor no existe no saldria ese 
# error si no que podria mostrar un mensaje

#utilizar metodo get()

# estudiantes={
#     1:'William Guerrero',
#     2:'Sara Sofia Cuayal',
#     3:'Felipe Agrega'
    
# }


#print(estudiantes.get(1,"No existe este estudiante"))
#Si no sabes si existe o no
#print(estudiantes.get(4,"No existe este estudiante"))


# #Busqueda directa en un diccionario

# estudiantes={
#     1:'William Guerrero',
#     2:'Sara Sofia Cuayal',
#     3:'Felipe Agrega'
    
# }

# print('William Guerrero' in estudiantes)

# #Quiero comprobar si la clave 1 exite en mi diccionario

#print(1 in estudiantes)

# #Claves de mi diccionario

#print(estudiantes.keys())

#Valores de mi diccionario

#print(estudiantes.values())

# #Recorrer diccionarios con el bucle for 
# #poner dentro de una lista y dentro tuplas donde estas la clave y 
# #valor de cada uno de los elementos del diccionario

#print(estudiantes.items())

# #Cuantos estudiantes hay en mi diccionario(cuantos elementos hay en 
# # el diccionario)

# estudiantes={
#     1:'William Guerrero',
#     2:'Sara Sofia Cuayal',
#     3:'Felipe Agrega'
# }

# print(len(estudiantes))


#Para que nuestro diccionario quede limpio se utiliza el metodo clear()

# estudiantes={
#     1:'William Guerrero',
#     2:'Sara Sofia Cuayal',
#     3:'Felipe Agrega'
# }

# estudiantes.clear()
# print(estudiantes)
#print(estudiantes)





# numero = int(input("Dime un número:"))
# cuadrados = {}

# for num in range(1,numero+1):
#     cuadrados[num] = num ** 2
# for num, valor in cuadrados.items():
#     print("%d -> %d" % (num,valor))


#El método title () devuelve una copia de la cadena 
# en la que los primeros caracteres de todas las palabras 
# están en mayúscula.

# #Ejercicio 1
# monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# moneda = input("Introduce una divisa: ")
# print(monedas.get(moneda.title(), "La divisa no está."))



# #Forma 2
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está.")
    
    
    
    
    
 #ejercicio4   
    
# nombre = input('¿Cómo te llamas? ')
# edad = input('¿Cuántos años tienes? ')
# direccion = input('¿Cuál es tu dirección? ')
# telefono = input('¿Cuál es tu número de teléfono? ')
# persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
# print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])  


#ejercicio3
# frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
# fruta = input('¿Qué fruta quieres? ').title()
# kg = float(input('¿Cuántos kilos? '))
# if fruta in frutas:
#     print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
# else: 
#     print("Lo siento, la fruta", fruta, "no está disponible.")  
    
    
#ejercicio4   
# curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
# total_creditos = 0
# for asignatura, creditos in curso.items():
#     print(asignatura, 'tiene', creditos, 'créditos')
#     total_creditos += creditos
# print('Número total de créditos del curso: ', total_creditos)  




# gente = {
#     'Pipi':'Calzaslargas', 
#     'Bob':'Esponja',
#     'Laura':'Ingalls', 
#     'Sherlock':'Holmes'
#     }

# print( gente.get('Pipi') in 'Calzaslargas')
