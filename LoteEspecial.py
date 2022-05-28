#Problem 2307
"""
Descripción

Se le dará un lote de n números, donde la tarea es verificar si el lote cumple las siguientes condiciones:

Los números del lote están en orden no decreciente.
La suma total de todos los números del lote es impar.
Existen al menos x números primos.
En caso de que el lote cumpla con todas las condiciones mostrar “SI” sin comillas, en otros casos mostrar “NO” sin comillas. 

Entrada
La primera linea contiene dos enteros n y x (1<=n<=100, 1<=x<=n) donde n es la cantidad de números del lote y x la cantidad mínima de números primos.

Le siguen n lineas donde ni es el i-esimo termino del lote. (1<=ni<=1000)

Salida
En caso de que el lote cumpla con todas las condiciones mostrar “SI” sin comillas, en otros casos mostrar “NO” sin comillas.

Ejemplo Entrada
5 2
5
5
4
5
1
Ejemplo Salida
NODescripción


Se le dará un lote de n números, donde la tarea es verificar si el lote cumple las siguientes condiciones:

Los números del lote están en orden no decreciente.
La suma total de todos los números del lote es impar.
Existen al menos x números primos.
En caso de que el lote cumpla con todas las condiciones mostrar “SI” sin comillas, en otros casos mostrar “NO” sin comillas. 

Entrada
La primera linea contiene dos enteros n y x (1<=n<=100, 1<=x<=n) donde n es la cantidad de números del lote y x la cantidad mínima de números primos.

Le siguen n lineas donde ni es el i-esimo termino del lote. (1<=ni<=1000)

Salida
En caso de que el lote cumpla con todas las condiciones mostrar “SI” sin comillas, en otros casos mostrar “NO” sin comillas.

Ejemplo Entrada
5 2
5
5
4
5
1
Ejemplo Salida
NO
"""


from cmath import sqrt
import math
def checkPrimo(numero):                             #1
	if numero <= 1:                                 #1
		return False                                #1
	for i in range (2, int(math.sqrt(numero))+1):   #m^1/2-2
		if  numero % i == 0:                       #m^1/2-3
			return False                            #1
	return True                                     #1

def proceso():                                      #1
    a,b = map(int, input().split())                 #1
    z = 0;p = 0;s=0                                 #3
    sw = False                                      #1
    for i in range(a):                              #n+1
        n = int(input())                            #n
        if n >= z:                                  #n
            s += n                                  #n
            z = n                                   #n
            if checkPrimo(z):                       #n()
                p += 1                              #n
        else:
            sw = True
    if sw:                                          #1
        print("NO")
    else:
        if s % 2 != 0 and p >= b:                   #1
            print("SI")                             #1
        else:
            print("NO")
proceso()