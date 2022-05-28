#Problem 1387
"""
Descripción
Comenzando con un entero entre 00 y 99 inclusive, escritos como dos dígitos (use un cero a la izquierda en caso de que el número sea menor que 10). Realice los siguiente:
Sume los dos dígitos.
Ahora concéntrese en el dígito de la derecha, en el número original y en el de la suma.
Finalmente combine estos números.
Si repetimos este proceso varias veces obtenemos el número original..

Por ejemplo

Inicio  Sume los dos dígitos   Combine los dos dígitos
------------------------------------------------------
 26 :     2+6 = 08 :            "6" y "8" = 68
 68 :     6+8 = 14 :            "8" y "4" = 84
 84 :     8+4 = 12 :            "4" y "2" = 42
 42 :     4+2 = 06 :            "2" y "6" = 26

En este caso tomo 4 pasos para obtener el número original.. Se pide que devuelva el número de pasos requeridos para obtener el número original.

Entrada
En la entrada hay varios casos de prueba. Cada caso de prueba viene en una linea que contiene un número 0≤N≤99.La entrada termina cuando no hay más datos

Salida
Por cada caso de prueba escriba en una línea el número de pasos requeridos para obtener el número original.

Ejemplo Entrada
26
55
0
71
Ejemplo Salida
4
3
1
12
"""

import sys
def SumDigitos(numero):                                 #1
    if len(numero) == 2:                                #1
        x = str(int(numero[0])+int(numero[1]))          #1
        if len(x) == 1:                                 #1
            x = "0"+x                                   #1
        return numero[1]+x[1]                           #1
    else:
        return numero + numero
#                                                       t(n) = 5
def proceso(n):
    z = n
    cont = 1
    while True:
        if int(z) == int(SumDigitos(n)):                #5
            break
        n = SumDigitos(n)
        cont += 1
    print(cont)
def main():
    for linea in sys.stdin:
        if linea == '\n':
            break
        else:
            linea = linea.strip()
            proceso(str(linea))#        t(n) = 300
main()