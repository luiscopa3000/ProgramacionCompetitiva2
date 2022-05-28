#Problem 2183
"""
Descripción
Llamemos MichiNúmero a un entero positivo x si en la notación decimal todos sus dígitos son iguales. Por ejemplo 1, 2, 7,  y 88 son MichiNúmeros, pero 124 y 2019 no son MichiNúmeros.

Para un número n, encuentre la cantidad de MichiNúmeros entre los números de 1 a n.

Entrada
La primera línea contiene un número entero t (1≤t≤10^4). Luego siguen t casos de prueba.

Cada caso de prueba se caracteriza por un número entero n (1≤n≤10^9).

Salida
Para cada caso de prueba, genere el número de MichiNúmeros entre los números de 1 a n.

Ejemplo Entrada
6
1
2
3
4
5
100
Ejemplo Salida
1
2
3
4
5
18
"""

def veri2(n):                       #1
    cont = 0                        #1
    for i in range(1,10):           #9
        x = ""                      #9
        for j in range(n):          #9n
            x = x + str(i)          #9(n-1)
            if int(x) <= n:         #9(n-1)
                cont += 1           #9(n-1)
            else:
                break
    return cont                     #1
def main():
    n = int(input())
    for i in range(n):
        x = int(input())
        print(veri2(x))             
main()