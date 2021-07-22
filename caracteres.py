#Una string es una secuencia de caracteres. -------------------------------------
# Puede acceder a los caracteres de uno en uno con el operador de paréntesis:

#fruta = 'fresa'
#letra = fruta[0]
#letra2 = fruta[2]
#print(letra2)
# print(letra2)


#Obtener la longitud de un string usando len()-----------------------------------
#len es una función incorporada que devuelve el número de caracteres de una cadena:

# fruta = 'banana'
# len(fruta)
# print(len(fruta))

#Para obtener el último carácter, hay que restarle 1 a la longitud:
# fruta = 'banana'
# longitud = len(fruta)
# ultimo = fruta[longitud-1]
# print(ultimo)

#Rebanas de String----------------------------------
#Un segmento de un string se llama un trozo. Seleccionar una rebanada es similar a seleccionar una caracter:
# s = 'Monty Python'
# print(len(s))
# print(s[0:5])
# print(s[:5])
# print(s[6:13])
#print(s[6:])

# print(s[:])



#Comparación de string----------------------------------------
#Los operadores de comparación trabajan con strings. Para ver si dos cadenas son iguales:
# palabra = 'banana'
# if palabra == 'banana':
#     print('Esta bien, bananas')
    
    
#Uso de funcion lower() upper()------------------------------

# palabra = 'Banana'.lower()

# if palabra == 'banana':
#     print('Esta bien, bananas')  
    
    
#Método de cadena llamado find que busca la posición de una cadena dentro de otra -----------

# palabra = 'banana'
# index = palabra.find('a')
# print(index)     


#Una tarea común es eliminar los espacios en blanco (espacios, tabulaciones o nuevas líneas) del principio y el final de una cadena utilizando el método de la tira:

# linea = '        Aqui vamos            '
# mensaje = linea.strip()
# print(mensaje)


#Caracteres especiales en el string------------------------------

# Saldrán dos líneas en pantalla, una con Hola, la otra con Mundo
# cadena = "Hola\nMundo"  
# print(cadena)

#Contar número de veces que el substring aparece en el string : count
# cadena = "un uno, un dos, un tres"

# print (cadena.count("un"))        # Saca 4, hay 4 "un" en cadena.
# print (cadena.count("un",10))     # Saca 1, hay 1 "un" a partir de la posición 10 de cadena.
# print (cadena.count("un",0,10))   # Saca 3, hay 3 "un" entre la posición 0 y la 10.


#Reemplazar substring en string : replace

#El método replace nos permite obtener una copia de la cadena original 
#(no reemplaza en la cadena original) 
#en la que se reemplaza el substring que se le indique por uno nuevo

# cadena = "un uno, un dos, un tres"

# print (cadena.replace("un", "XXX"))        # saca por pantalla "XXX XXXo, XXX dos, XXX tres"
# print (cadena.replace("un", "XXX", 2))     # Sólo reemplaza 2 "un", así que saca por pantalla "XXX XXXo, un dos, un tres"


#El método format() de string-----------------------------------------------------------
#Se pueden definir variables y 
# poner llaves {} en el string donde van a ir los números o caracteres. 
# Entre paréntesis pasamos los valores.

# # saca "El valor es 12
# print ("El valor es {}".format(12))

# # saca "El valor es 12.3456
# print ("El valor es {}".format(12.3456))

# # Tres conjuntos {}, el primero para el primer parámetro de format(), el segundo para el segundo
# # y así sucesivamente.
# # saca "Los valores son 1, 2 y 3"
# print ("Los valores son {}, {} y {}".format(1,2,3))

# # Entre las llaves podemos poner la posición del parámetro. {2} es el tercer parámetro de format()
# # {0} es el primer parámetro de format.
# # saca "Los valores son 3, 2 y 1"
# print ("Los valores son {2}, {1} y {0}".format(1,2,3)) 


#Multiplicar -----------------------------------

#Si quieres varias copias de una cadena de caracteres utiliza
# el operador de multiplicación (*).

# mensaje2a = 'Hola ' * 3
# mensaje2b = 'Mundo'
# print(mensaje2a + mensaje2b)



