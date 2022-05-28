#1611 Problem  E
""
Descripción
Estas en una sala donde existe N botones numerados de 0 a N - 1, cada botón tiene escrito encima un número, si el número escrito encima del botón numero i es número K entonces al presionar el botón número i se apagara y luego se prendera el botón número K, al principio el botón 0 esta prendido y todos los demás apagados (solo se puede presionar un botón si esta prendido), tu objetivo es saber si apretando una secuencia de botones es posible prender el botón M.
 
Si el número escrito encima del botón es el mismo número del botón entonces al presionarlo permanecerá prendido.
Entrada
La entrada consiste de un solo caso de prueba, la primera línea contiene dos números enteros N (2 <= N <= 100) y M (0 <= M < N) que es el número de botones y el botón que debes intentar prender, la segunda línea contiene N números ai que indican los números escritos encima de cada botón (0 <= ai < N)
Salida
Si es posible prender el botón M imprima SI en otro caso imprima NO.
Ejemplo Entrada
5 3
1 4 2 3 3
Ejemplo Salida
SI
""
from sympy import false, true
def main():
    a , b = map(int, input().split())
    v = list( map(int, input().split()))
    i = int(v[0])
    sw = false
    for c in range(a):
        if i != v[i]:
            i = v[i]
            if i == b:
                sw = true
                break
    if sw:
        print("SI")
    else:
        print("NO")
main()