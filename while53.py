# def factorial(n: int) -> int:
#     resultado = 1
#     numero_actual = 2
#     while numero_actual <= n:
#         resultado = resultado * numero_actual
#         numero_actual += 1
#     return resultado


# print(factorial(5))


# Evento
# promedio, total, contar = 0.0, 0, 0
# print("Introduzca la nota de un estudiante (-1 para salir): ")
# grado = int(input())
# while grado != -1:
#     total = total + grado
#     contar = contar + 1
#     print("Introduzca la nota de un estudiante (-1 para salir): ")
#     grado = int(input())
# promedio = total / contar
# print("Promedio de notas del grado escolar es: " + str(promedio))


# promedio, total, contar = 0.0, 0, 0
# mensaje = "Introduzca la nota de un estudiante (-1 para salir): "

# grado = int(input(mensaje))
# while grado != -1:
#     total = total + grado
#     contar += 1
#     grado = int(input(mensaje))
# else:
#     promedio = total / contar
#     print("Promedio de notas del grado escolar: " + str(promedio))


# variable = 10

# while variable > 0:
#     print('Actual valor de variable:', variable)
#     variable = variable -1
#     if variable == 5:
#         break


# variable = 10

# while variable > 0:
#     variable = variable -1
#     if variable == 5:
#         continue
#     print('Actual valor de variable:', variable) # no imprime el 5  
    
    
#Bucle For

# for i in [1,2,3,4,5]:
#     print ("Hola mundo")

#La variable iteradora i me esta recorriendo elemento por elemento
#El bucle for te recorre la coleccion elemento por elemento, lo que 
# se da cuenta el iterador es la cantidad que hay de estos elementos

# for i in [1,2,3,"alejandro",5]:
#     print ("Hola mundo")  
    
#         
# for i in [1,2,3,"alejandro",5]:
#     print (i)  #Imprime los elementos de nuestra coleccion 


#Otra manera de formar nuetro bucle for

# coleccion=[1,2,3,"alejandro",5]  
# for i in coleccion:  
#     print (i)
    
#Diccionario

# diccionario={
#     'Alejandro':25,
#     'Rolando':30,
#     'Maria':25
    
#     }


# for i in diccionario:  
#     print (i)#



# for i in diccionario:  
#     print (diccionario[i])     


# #Imprimir los dos

# for i in diccionario:  
#     print (i,'->',diccionario[i]) 

# #Imprimir los dos con items(), con el cual se recorre todos los elementos del diccionario.    
# for clave, valor in diccionario.items():
#     print(clave,'->',valor)     
    
    
  