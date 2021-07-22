
#Primer ejercicio
# num = int(input("Digite el numero de 4 cifras: "))
# if len(str(num)) == 4: 
    
#     v4 = num%10 
#     v3 = (num//10)%10 
#     v2 = (num//100)%10 
#     v1 = (num//1000)%10 
             
#     if v4 >= v3 and v4 >= v2 and v4 >= v1:
#         mayor = v4
#         print("el numero mayor es: ",mayor)
#     elif v3 >= v2 and v3 >= v4 and v3 >= v1:
#         mayor = v3
#         print("el numero mayor es: ",mayor)
#     elif v2 >= v3 and v2 >= v4 and v2 >= v1:
#         mayor = v2
#         print("el numero mayor es: ",mayor)
#     else:
#         mayor = v1
#         print("el numero mayor es: ",mayor)
      
        
#     if mayor%2==0:
#         print("Numero par")
#     else:
#         print("Numero impar")   
  
  
  
  
  
#   numMayor=0
# while True:
#     numero=input()
#     Tam=len(numero)
#     if Tam ==4:
#         break
#     else:
#         print("El numero debe tener 4 digitos\nintente denuevo.")

# for i in [0,1,2,3]:
#     if numero[i] > str(numMayor):
#         numMayor= numero[i]

# numMayor= int(numMayor)
# print("El numero mayor es: ",numMayor)


# if numMayor % 2 == 0:
#     print("Este numero es par")
# else: 
#     print("Este numero es impar")

  
  
  
  
        
#Segundo ejercicio   

# import random
# numero = random.randint(1, 10)
# #print(help(random.randint(1, 10)))
# nadivinado = int(input("Ingrese el número que cree que puede salir: "))

# if numero == nadivinado:
#     print("¡Ganaste!")
# elif numero > nadivinado:
#     print("El número a adivinar es mayor al que ingresaste.")
# elif numero < nadivinado:
#     print("El número a adivinar es menor al que ingresaste.")
# else:
#     print("Opción no válida.")      




#Ejecicio 3

# print("Año bisiesto")
# anno = int(input("Escriba un año: "))
# if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
#     print("El año", anno, "es bisiesto.")
# else:
#     print("El año", anno, "no es bisiesto.")


#Ejercicio 4
# llamada = float(input("ingrese el número de minutos"))
# if llamada <= 5:
#     costo = llamada*100
# elif llamada <= 8:
#  costo = 500 + ((llamada - 5)*80)
# elif llamada <= 10:
#     costo = ((llamada - 8) * 70) + 240 + 500
# else:
#     costo = ((llamada - 10) * 50) + 240 + 500 + 140
# print(costo)

# dia= input("¿es domigo? (Y/N)")
# if dia == "Y":
#     costo = costo * 1.03
# elif dia == "N":
#     jornada = input("¿es mañana o tarde? M/T")
#     if jornada == "M":
#         costo = costo *1.15
#     elif jornada == "T":
#         costo = costo * 1.10
#     else:
#         print("jornada no válida")
# print("Costo final de la llamada", costo)    



# anno = int(input("escribe un año: "))
# if anno%4 == 0:
#     print ("este año es bisiesto")
# elif anno%400 == 0:
#     print ("este año es bisiesto")
# else:
#     print("este año no es bisiesto")


# año = 1980

# if año % 4 != 0: 
# 	print("No es bisiesto")
# elif año % 4 == 0 and año % 100 != 0:
# 	print("Es bisiesto")
# elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
# 	print("No es bisiesto")
# elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
    
# año = 500

# if año % 4 != 0: 
# 	print("No es bisiesto")
# elif año % 4 == 0 and año % 100 != 0:
# 	print("Es bisiesto")
# elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: 
# 	print("No es bisiesto")
# elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
# 	print("Es bisiesto")


year = int(input("Ingrese el año"))
if year%4==0:
    print("Este año es bisiesto")
elif year%400== 0:
    print("Este año es bisiesto")
elif year%100!=0:
    print("Este año no es bisiesto")
print("El año que escogió es",year)
