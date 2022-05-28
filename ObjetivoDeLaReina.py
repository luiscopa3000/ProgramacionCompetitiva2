""
Descripción
Se le da un tablero de ajedrez y la Reina se coloca en ese tablero de ajedrez. Marca todas las casillas a las que la Reina puede acceder con un solo movimiento. Tenga en cuenta que la Reina puede moverse en cualquier celda en la misma horizontal, vertical o diagonales con su posición actual.

Entrada
La entrada consta de 8 líneas, cada línea contiene exactamente 8 caracteres. El punto ‘‘." (ASCII 46) se usa para marcar la celda libre en el tablero de ajedrez, la letra ‘‘F" se usa para marcar la posición actual de la Reina.

Salida
Imprime 8 líneas, cada línea contiene exactamente 8 caracteres. Para las celdas accesibles por la Reina, reemplace el punto ‘‘." con el ‘‘∗". Las demás celdas permanecerán como estaban en la entrada.

Ejemplo Entrada
........
........
........
........
....F...
........
........
........
Ejemplo Salida
*...*...
.*..*..*
..*.*.*.
...***..
****F***
...***..
..*.*.*.
.*..*..*
""


import sys
def mostrarL(lista):
    l = [str(a) for a in lista]
    print("".join(l).rstrip())
def mostrarM(matriz):
    for i in matriz:
        mostrarL(i)
def buscar(matriz,n):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == n:
                return i,j
    return -1,-1
def VerHori(m, a,b):
    for i in range(8):
        if m[i][b] != "F":
            m[i][b] = "*"
        if m[a][i] != "F":
            m[a][i] = "*"
def pendA(m,a,b):
    for i in range(1,8):
        if b-i >=0 and a-i >=0:
            if m[a-i][b-i] != "F":
                m[a-i][b-i] = "*"
        if b+i<8 and a+i <8:
            if m[a+i][b+i] != "F":
                m[a+i][b+i] = "*"
        if a-i >=0 and b+i <8:
            if m[a-i][b+i] != "F":
                m[a-i][b+i] = "*"
        if a+i <8 and b-i >=0:
            if m[a+i][b-i] != "F":
                m[a+i][b-i] = "*"
def main():
    m = []
    for linea in sys.stdin:
        if linea == "\n":
            break
        lista = list(str(linea))
        m.append(lista)
    a,b = buscar(m,"F")
    VerHori(m,a,b)
    pendA(m,a,b)

    mostrarM(m)
main()

