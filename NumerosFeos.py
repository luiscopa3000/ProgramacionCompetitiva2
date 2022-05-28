#1301 Problem  F
""
Descripción
Los números feos son aquellos cuyos factores primos son 2,3,5. La secuencia

1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ...

Muestra los primeros 11 números feos. Por  se incluye el el numero 1.

El numero feo 6 es el 6 que tiene como divisores el 2 y el 3. El numero feo 7 e el 8, etc.

Entrada
La entrada consiste de varios casos de prueba. La primera linea tiene un numero entero que tiene el numero de casos de prueba.
Luego siguen n líneas cada una con un número que representa el numero feo que queremos imprimir. Este numero es menor o igual a 1600.

Salida
Escriba en la salida el numero feo solicitado.

Ejemplo Entrada:
8
1
2
3
4
5
6
7
8

Ejemplo Salida:
1
2
3
4
5
6
8
9

""
def numFeo(n):
    dp = [0] * (n)
    p2 = 0; p3 = 0; p5 = 0
    dp[0] = 1
    for i in range(1, n):
        sigFeo = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
        dp[i] = sigFeo
        if sigFeo == dp[p2] * 2:
            p2 += 1
        if sigFeo == dp[p3] * 3:
            p3 += 1
        if sigFeo == dp[p5] * 5:
            p5 += 1
    return dp[n - 1]

def main():
    n = int(input())
    for i in range(n):
        print(numFeo(int(input())))
main()