""
Descripción
Dada una matriz de números enteros a, la cual consta de n filas y m columnas, llevar a un vector v el mayor número de cada fila. Para mayor comprensión, veamos un ejemplo: sea la matriz a, la cual tiene 5 filas y 4 columnas:



Los mayores de cada fila son: 20,9,15,41,6, las puede observar en la matriz a resaltadas en verde.

Entrada
La primera consta de dos enteros n y m (1≤n,m≤100), los cuales indican el numero de filas y columnas respectivamente.

Le siguen n filas, donde cada fila posee m enteros, cada par separado por un espacio. (−109≤ai,j≤109)

Salida
Imprimir el mensaje: "matriz de entrada:" seguido de la matriz de entrada, y despues imprimir "vector de salida:" seguido del vector v, el cual contiene a los números mayores de cada fila. (Debe imprimir un espacio entre cada par de elementos).

Ejemplo Entrada
5 4
12 3 20 -5
4 8 3 9
-6 15 0 11
2 41 14 4
-7 0 6 4
Ejemplo Salida
matriz de entrada:
12 3 20 -5
4 8 3 9
-6 15 0 11
2 41 14 4
-7 0 6 4
vector de salida:
20 9 15 41 6
""


def mostrarL(lista):
    l = [str(a) for a in lista]
    print(" ".join(l))
def mostrarM(matriz):
    for i in matriz:
        mostrarL(i)
def proceso():
    a,b = map(int, input().split())
    m =[]
    v = []
    for i in range(a):
        lista = list(map(int, input().split()))
        if len(lista) == b:
            maximo = max(lista, key=int)
            v.append(maximo)
            m.append(lista)
    print("matriz de entrada:")
    mostrarM(m)
    print("vector de salida:")
    mostrarL(v)
proceso()
    
