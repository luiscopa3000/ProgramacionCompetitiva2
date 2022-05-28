#Problem 2328
"""
Descripción
Generar una matriz a, la cual debe constar de n filas y m columnas, para n=5 y m=4 la matriz generada seria:



Puede notar que la matriz se genera desde la última fila, intercalando por filas los número naturales y los números Fibonacci.

Entrada
La única línea consta de dos enteros n y m (1≤n∗m≤144), las cuales indican el número de filas y columnas respectivamente.

Salida
Imprima la matriz solicitada, por cada fila: cada par de elementos deben estar separados por un espacio.

Ejemplo Entrada
5 4
Ejemplo Salida
9 10 11 12
13 8 5 3
5 6 7 8
2 1 1 0
1 2 3 4
"""


def fibonacci(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = fibonacci(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)
def mostrar(m):
    for i in m:
        print(i)
def NaNum(a,b):
    c = 0; m =[]
    for i in range(a):
        v = [];s=[]
        for j in range(b):
            s.append(str(fibonacci(c)[0]))
            c += 1
            v.append(str(c))
        if len(m) < a:
            m.append(" ".join(v))
        if len(m) < a:
            m.append(" ".join(s[::-1]))
        else:
            break
    return list(reversed(m))
        
def main():
    a,b = map(int, input().split())
    mostrar(NaNum(a,b))

main()
        