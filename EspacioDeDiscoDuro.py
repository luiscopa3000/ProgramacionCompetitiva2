#1310 Problem  B	
import sys
def ordenar(lista):
    lista.sort(reverse = True)
    return lista
def sumar(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma
def proceso():
    U=list(map(int,input().split()))
    C=list(map(int,input().split()))
    C = ordenar(C)
    x = sumar(U)
    cont =1
    for i in C:
        if x > i:
            x -= i
            cont += 1
        else:
            break
    print(cont)

def main():
    for linea in sys.stdin:
        if linea == "\n":
            break
        proceso()
main()