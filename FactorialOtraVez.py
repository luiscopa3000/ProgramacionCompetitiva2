#Problem 1335
"""
Descripción
Mateo es un estudiante de ingeniera que esta desarrollando una forma original para representar numero enteros. El denomino este método "A Curious Method" cuya abreviación es ACM.

La anotación ACM utiliza los mismos dígitos que la notación decimal, los dígitos del 0 al 9.

Para convertir un numero A de la notación ACM a decimal usted debe adicionar k términos, donde k es el numero de dígitos del numero A en notación ACM. El valor del termino i correspondiente al dígito i contando de derecha a izquierda es ai×i!.

Por ejemplo 719ACM es equivalente a 5310, dado que  7×3!+1×2!+9×1!=53.

Mathews recién comienza sus estudios y desea que le ayudes a convertir los números en notación ACM a notación decimal.

Entrada
Cada caso de prueba esta dado en una linea que contiene un una cadena de un máximo de 5 dígitos, que representa el numero en notación ACM. la cadena no tiene ceros a la izquierda.

El ultimo caso de prueba es una linea que contiene un cero.

Salida
Por cada caso de entrada imprima una linea conteniendo el numero decimal para la representación del numero ACM.

Ejemplo Entrada
719
1
15
110
102
0
Ejemplo Salida
53
1
7
8
8
"""


import sys
def factorial(n):                           #1
    if n == 0:                              
        return 1                            
    else:                                   #1    
        return n * factorial(n-1)           #t(n-1)+1

def proceso(n):                             #1
    x = 0                                   #1
    l = len(n)                              #1
    for i in n:                             #n+1
        x = (int(i)*factorial(l))+x         #n(n+1)
        l = l-1                             #n
    print(x)                                #1
#                                           t(n) = 5+n^2+2n
def main():
    for linea in sys.stdin:
        linea = linea.strip()
        if str(linea) == "0":
            break
        else:
            proceso(str(linea))         #t(n) = 5+n^2+2n
main()#                                  t(n) = 5+n^2+2n        