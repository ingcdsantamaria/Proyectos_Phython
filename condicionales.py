
"""#1. Leer un número de 4 dígitos, mostrar el dígito mayor e informar si es par o impar.
num = int(input("Digite el numero de 4 cifras: "))
if len(str(num)) == 4: 
    
    v4 = num%10 
    v3 = (num//10)%10 
    v2 = (num//100)%10 
    v1 = (num//1000)%10 
    if v4 >= v3 and v4 >= v2 and v4 >= v1:
        mayor = v4
        print("el numero mayor es: ",mayor)
    elif v3 >= v2 and v3 >= v4 and v3 >= v1:
        mayor = v3
        print("el numero mayor es: ",mayor)
    elif v2 >= v3 and v2 >= v4 and v2 >= v1:
        mayor = v2
        print("el numero mayor es: ",mayor)
    else:
        mayor = v1
        print("el numero mayor es: ",mayor) 
    if mayor%2==0:
        print("Numero par")
    else:
        print("Numero impar")
"""
#tarea
"""

import random
a = random.randrange(1,6)
tem = 0
if tem < 3:
    n = int(input("\n PRIMER INTENTO:\n\tIngrese el numero que desea adivinar:\n"))
    if n > 0 and n < 6:
        if n == a:
            if n%2 == 0:
                print("\n\tFELICITACIONES!!\nUsted a acertado el numero que digito es: "+str(n)+" el numero a adivinar era: "+str(a)+" y su numero es par")
                tem = 3
            else:
                print("\n\tFELICITACIONES!!\nUsted a acertado el numero que digito es: "+str(n)+" el numero a adivinar era: "+str(a)+" y su numero es impar")
                tem = 3
        elif n >a:
            print("El numero digitado es mayor al que desea adivinar intente lo nuevamente")
            tem = tem +1
            n = int(input("\n SEGUNDO INTENTO:\n\tIngrese el numero que desea adivinar:\n"))
            if n == a:
                if n%2 == 0:
                    print("\n\tFELICITACIONES!!\nUsted a acertado el numero que digito es: "+str(n)+" el numero a adivinar era: "+str(a)+" y su numero es par")
                    tem = 3
                else:
                    print("\n\tFELICITACIONES!!\nUsted a acertado el numero que digito es: "+str(n)+" el numero a adivinar era: "+str(a)+" y su numero es impar")
                    tem = 3
            elif n >a:
                print("El numero digitado es mayor al que desea adivinar intente lo nuevamente ")
                tem = tem +1
                n = int(input("\nTERCER Y ULTIMO INTENTO:\n\tIngrese el numero que desea adivinar:\n"))
                if n == a:
                    if n%2 == 0:
                        print("\n\tFELICITACIONES!!\nUsted a acertado el numero que digito es: "+str(n)+" el numero a adivinar era: "+str(a)+" y su numero es par")
                        tem = 3
                    else:
                        print("\n\tFELICITACIONES!!\nUsted a acertado el numero que digito es: "+str(n)+" el numero a adivinar era: "+str(a)+" y su numero es impar")
                        tem = 3
                elif n >a:
                    print("El numero digitado es mayor al que desea adivinar\n\tLO SIENTO A PERDIDO")
                    tem = tem +1
                else:
                    print("el numero digitado es menor que el que desea adivinar\n\tLO SIENTO A PERDIDO")
                    tem = tem +1
            else:
                print("el numero digitado es menor que el que desea adivinar intente lo nuevamente")
                tem = tem +1
                n = int(input("\nTERCER Y ULTIMO INTENTO:\n\tIngrese el numero que desea adivinar:\n"))
                if n == a:
                    if n%2 == 0:
                        print("\n\tFELICITACIONES!!\nUsted a acertado el numero que digito es: "+str(n)+" el numero a adivinar era: "+str(a)+" y su numero es par")
                        tem = 3
                    else:
                        print("\n\tFELICITACIONES!!\nUsted a acertado el numero que digito es: "+str(n)+" el numero a adivinar era: "+str(a)+" y su numero es impar")
                        tem = 3
                elif n >a:
                    print("El numero digitado es mayor al que desea adivinar\n\tLO SIENTO A PERDIDO")
                    tem = tem +1
                else:
                    print("el numero digitado es menor que el que desea adivinar\n\tLO SIENTO A PERDIDO")
                    tem = tem +1
        else:
            print("el numero digitado es menor que el que desea adivinar intente lo nuevamente")
            tem = tem +1
            n = int(input("\n SEGUNDO INTENTO:\n\tIngrese el numero que desea adivinar:\n"))
            if n == a:
                if n%2 == 0:
                    print("\n\tFELICITACIONES!!\nUsted a acertado el numero que digito es: "+str(n)+" el numero a adivinar era: "+str(a)+" y su numero es par")
                    tem = 3
                else:
                    print("U\n\tFELICITACIONES!!\nsted a acertado el numero que digito es: "+str(n)+" el numero a adivinar era: "+str(a)+" y su numero es impar")
                    tem = 3
            elif n >a:
                print("El numero digitado es mayor al que desea adivinar intente lo nuevamente")
                tem = tem +1
                n = int(input("\nTERCER Y ULTIMO INTENTO:\n\tIngrese el numero que desea adivinar:\n"))
                if n == a:
                    if n%2 == 0:
                        print("\n\tFELICITACIONES!!\nUsted a acertado el numero que digito es: "+str(n)+" el numero a adivinar era: "+str(a)+" y su numero es par")
                        tem = 3
                    else:
                        print("\n\tFELICITACIONES!!\nUsted a acertado el numero que digito es: "+str(n)+" el numero a adivinar era: "+str(a)+" y su numero es impar")
                        tem = 3
                elif n >a:
                    print("El numero digitado es mayor al que desea adivinar\n\tLO SIENTO A PERDIDO")
                    tem = tem +1
                else:
                    print("el numero digitado es menor que el que desea adivinar\n\tLO SIENTO A PERDIDO")
                    tem = tem +1
            else:
                print("el numero digitado es menor que el que desea adivinar intente lo nuevamente")
                tem = tem +1
                n = int(input("\nTERCER Y ULTIMO INTENTO:\n\tIngrese el numero que desea adivinar:\n"))
                if n == a:
                    if n%2 == 0:
                        print("\n\tFELICITACIONES!!\nUsted a acertado el numero que digito es: "+str(n)+" el numero a adivinar era: "+str(a)+" y su numero es par")
                        tem = 3
                    else:
                        print("\n\tFELICITACIONES!!\nUsted a acertado el numero que digito es: "+str(n)+" el numero a adivinar era: "+str(a)+" y su numero es impar")
                        tem = 3
                elif n >a:
                    print("El numero digitado es mayor al que desea adivinar\n\tLO SIENTO A PERDIDO")
                    tem = tem +1
                else:
                    print("el numero digitado es menor que el que desea adivinar\n\tLO SIENTO A PERDIDO")
                    tem = tem +1
"""
"""import random
a = random.randrange(1,6)
i=0
while i < 3:
    n = int(input("Ingrese el numero que desea adivinar:\n"))
    if n == a:
        print("\n\tFELICITACIONES!!\nUsted a acertado el numero que digito es: "+str(n)+" el numero a adivinar era: "+str(a)+" y su numero es par")
        i = i + 3
    elif n > a:
        print("El numero digitado es mayor al que desea adivinar intente lo de nuevo")
        i = i +1
    elif n < a:
        print("el numero digitado es menor que el que desea adivinar intente lo de nuevo")
        i = i +1
    else:
        print("No a digitado un numero entre 1 y 5")"""
        

#3. La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por 
# el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan se cobran a 100 pesos por minuto, 
# los siguientes tres, 80 pesos, los siguientes dos minutos, 70 pesos, y a partir del décimo minuto, 50 pesos. 
# Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y en turno 
# de tarde 10 %.  Realice un algoritmo para determinar cuánto debe pagar.
"""
print("Esta llamando...")
llamada = int(input("ingrese el tiempo que duro en la llamada"))

if llamada <= 5:
    valor = llamada*100
elif llamada <= 8:
    valor = 500+(llamada - 5)*80
elif llamada <= 10:
    valor = (llamada - 8)*70 + 740
elif llamada > 10:
    valor = (llamada - 10)*50 + 880
else:
    print("DIGITE NUEVAMENTE")
print(valor)
n1 = int(input("si es domingo ingrese 1 si no 0"))
if n1 == 1:
    precio = valor + (valor * 0.3)
    print(precio)
elif n1 == 0: 
    n2 = int(input("si es mañana ingrese 1 si es tarde ingrese 0"))
    if n2 == 1:
        precio = valor + (valor * 0.15)
        print(precio)
    elif n2 == 0:
        precio = valor + (valor * 0.10)
        print(precio)
    else:
        print("DIGITE NUEVAMENTE")
else:
    print("DIGITE NUEVAMENTE")"""

#4. Escriba un programa que pida un año y que escriba si es bisiesto o no.
#  Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100
#  no lo son, aunque los múltiplos de 400 sí.

a = int(input("ingrese el año que desea saber:\n"))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(" ES BISIESTO")
else:
    print("NO ES BISIESTO")