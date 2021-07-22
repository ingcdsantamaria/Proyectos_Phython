
"""
diccionario: dict = {
    "llave" : "tesoro",
    "promedio" : 10
}
print(diccionario["llave"])
#forma diferente de llamar un diccionario
frutas: dict = {}
frutas["fruta1"] = "banana"
frutas["fruta2"] = "manzana"
print(frutas)"""
"""
supermercado: dict = {
    "Limpia vidrios" : "20%",
    "Arroz" : "30%",
    "Papa" : "10%",
    "suavisante" : "50%"
}
#eliminar
del(supermercado['Arroz'])
print(supermercado)"""
""".Keys
.values 
round(sumatoria/4,2)"""
#Diccionario
"""
def promedioNotas(dicNota):
   
   n1=dicNota['n1']
   n2=dicNota['n2']
   n3=dicNota['n3']
   n4=dicNota['n4']
   
   promedio=(n1+n2+n3+n4)/4
   return(round(promedio,2))


dicNota  = {
    'n1': 1.5,
    'n2': 5,
    'n3': 2.5,
    'n4': 4.5
    

}

print(promedioNotas(dicNota))
"""
#la funcion puede recibir un diccionario o variables independientes como en este caso
"""
def func_ejemplo(nombre:str,edad:int,ciudad:str):
    print("la ciudad es: ",ciudad)
    print("la edad es: ",edad)
    print("el nombre es: ",nombre)

persona = {
    "ciudad" : "medellin",
    "edad" : 40,
    "nombre" : "cristian"
}
#**persona me organiza las variables

func_ejemplo(**persona)

#la funcion puede recibir un diccionario o variables independientes como en este caso
"""
# def pago(empleado):
#     tipo = empleado["tipo"]
#     nombre = empleado["nombre"]
#     if tipo == "A":
#         sueldo = 2500000
#     elif tipo == "D":
#         sueldo = 3500000
#     else:
#         sueldo = "N/A"
#     resultado = {
#         "nombre" : nombre,
#         "tipo":tipo,
#         "sueldo":sueldo
#     }
#     return resultado


# empleado = {
#     "id_empleado" : 6754,
#     "tipo" : "A",
#     "nombre" : "cristian"
# }

# print(pago(empleado))