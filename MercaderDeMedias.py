


#problem 1762


"""
Descripción
Jhon trabaja en una tienda de ropa. Tiene una gran pila de medias que debe emparejar por colores para la venta. Dado un arreglo de enteros representando el color de cada media, determine cuántos pares de medias con colores iguales hay.
Por ejemplo, hay medias n=7 medias con colores arr=[1,2,1,2,1,3,2]. Hay un par de color 1 y uno de color 2. Hay tres medias impares restantes, una para cada color. El número de pares es 2.
Entrada
La primera línea contiene un entero n, el número de medias representados en arr
La segunda línea contiene n enteros separados por un espacio describiendo los colores arr[i] de las medias en la pila.
1≤n≤100
1≤arr[i]≤100 dónde 0≤i<n.
La entrada termina cuando no hay mas datos.
Salida
Retorne el número total de pares de medias que Jhon pueda vender.

Ejemplo Entrada
9
10 20 20 10 10 30 50 10 20
Ejemplo Salida
3
"""

import sys
from timeit import default_timer
def proceso(n):                                 #1
    lista = list(map(int, input().split()))     #1
    lista.sort()                                #n log n
    i = 0                                       #1
    cont = 0                                    #1
    t = 0                                       #1
    while True:                                 #n
        if i+1 < n:                             #n
            if lista[i] == lista[i+1]:          #n-1
                lista.pop(i)
                lista.pop(i)
                n -=2
                cont += 1
            else:                               #n-1
                i += 1                          #n-1
        else:
            break
    print(cont)                                 #1
#                                       t(n) = 5+3(n-1)+2n+nlog10(n)
def main():                                     #1
    for linea in sys.stdin:
        if linea == '\n':
            break
        else:
            n = int(linea)                      #1
            proceso(n)                      #1+5n+nlogn
main()      #                           #t(n) = 2+5n+nlogn
