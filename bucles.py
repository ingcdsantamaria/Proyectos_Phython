
# def factorial(n: int) -> int:
#     resultado = 1
#     numero_actual = 2
#     while numero_actual <= n:
#         resultado = resultado * numero_actual
#         numero_actual += 1
#     return resultado


# print(factorial(5))
# """
# promedio, total, contar = 0.0, 0, 0
# print("Introduzca la nota de un estudiante (-1 para salir): ")
# grado = int(input())
# while grado != -1:
#     total = total + grado
#     contar = contar + 1
#     print("Introduzca la nota de un estudiante (-1 para salir): ")
#     grado = int(input())
# promedio = total / contar
# print("Promedio de notas del grado escolar es: " + str(promedio))"""

# #1. Escribir un programa que cree un diccionario vacío y lo vaya llenado 
# # con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono,
# #  correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un 
# # nuevo dato debe imprimirse el contenido del diccionario.

# #.items()
# #for ya tenemos una condicion
# #lo especificamos
# """
# personas = {}
# n=0
# cantidad = int(input("Introduce la cantidad de personas que vamos a guradar:"))
# while n < cantidad:
#     personas["nombre"] = input("Nombre de la persona:")
#     personas["edad"] = input("Edad de la persona:")
#     personas["sexo"] = input("Sexo de la persona:")
#     personas["telefono"] = input("Telefono de la persona:")
#     personas["correo "]= input("Correo de la persona:")
#     personas["direccion"] = input("Direccion de la persona:")
#     n+=1
#     print(personas)"""

# canasta={}
# def compra():
#     cant = str(input("Desea ingresar un articulo a su factura(escriba si o no):\n"))
#     n=input(cant)
#     i=1
#     while n != "no":
#         canasta[input("Ingrese el articulo")] = int(input("Ingrese el precio"))
#         print(canasta)
#         n = str(input("Desea ingresar un articulo a su factura"))
#         i+=1
# def total(canasta):
#     print("Lista de la compra\n")
#     print("Articulo\tValor")
#     for clave, valor in canasta.items():
#         print(clave,'\t',valor)     
#     suma:int =int(sum(canasta.values()))
#     print("Total a pagar:\t",suma)

# compra()
# total(canasta)

#daniel
# #CLASE DICCIONARIOS----------------------------

# def Compra():
#     listaC={}
#     N_articulos=0
#     total=0
#     N_articulos=int(input("Cuantos articulos desea agregar a la cesta de compra : "))
#     while N_articulos >0:
        
#         listaC[str(input("ingrese el nombre del articulo : "))]=int(input("ingrese el precio edl articulo : "))
#         N_articulos=N_articulos-1
    
#     print("\nLista de la compra\nArticulo\tPrecio")
#     for i in listaC:  
#         print ( i,'\t\t',listaC[i]) 
    
#     for i in listaC:  
#         total= sum(listaC.values())
    
#     print("\ntotal\t\t",total)

# Compra()
#ejercicio

# i=51
# resultado=0
# suma:str =""
# while i > 50 and i < 200:
#     resultado: int = i+resultado
#     suma=suma+" + "+str(i)
#     i+=2

# print("suma: "+suma[3:]," resultado: ",resultado)

#ejercicio 2
# n=1
# while n <= 2:
#     persona = {
#         "nombre: " : str(input("ingrese nombre: ")),
#         "edad: " : int(input("ingrese edad: "))
#     }
#     print("persona_",n,": ",persona)
#     n+=1

#ejercicio #3

# cant = "ingrese nota"
# cont=0
# total=0
# n = int(input(cant))
# while n != -1:
#     total= total + n
#     cont+=1
#     n = int(input(cant))
# else:
#     promedio = total / cont
#     print(promedio)

