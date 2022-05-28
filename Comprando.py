#1312 Problem  C	
""
Descripción
Steve desea comprar un coche nuevo. No es rico por lo que el preferirá un coche razonablemente barato. El único inconveniente es que la calidad de los coches baratos es cuestionable. Así, Steve decide hacer una lista de precios de los automóviles de donde escogerá el coche con el tercer precio más bajo.

Se lee un vector de enteros con los precios. Un precio se puede repetir varias veces en la lista de precios, pero debe contar como una sola vez. 

Escribe un programa que devuelve el tercer precio más bajo de la lista. Si hay menos de tres precios diferentes  el resultado es −1.

Entrada
La entrada consiste de varios casos de prueba. La primera línea de cada caso de prueba contiene el número de precios coches 1<N≤50. La siguiente línea contiene 0<N≤1000 números que representan la lista de precios. La entrada termina cuando no hay más datos.

Salida
Imprima para cada caso de prueba el tercer precio menor de la lista.

Ejemplo Entrada
9
10  40  50  20  70  80  30  90  60
10
10  10  10  10  20  20  30  30  40  40
1
10
5
80  90  80  90  80

Ejemplo Salida
30
30
-1
-1
""
import sys
def proceso():
    v=list(map(int,input().split()))
    x = set(v)
    x = sorted(x)
    if len(x) >= 3:
        print(x[2])
    else:
        print("-1")

def main():
    for linea in sys.stdin:
        if linea == "\n":
            break
        proceso()
main()
