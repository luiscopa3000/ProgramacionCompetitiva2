#1162 Problem  A
""
Descripción
Una imprenta, antes de imprimir una cadena, revisa la cantidad de letras que va a necesitar, para asi no llevar mas letras de las que va a usar.
El problema, es que los textos suelen ser muy largos.
Entrada
La entrada comienza con el numero de casos a considerar t.
Por cada caso de prueba, existe una cadena en cada linea.
Esa linea, puede contener mas de una palabra y espacios entre ellas.
Pero solo contendra letras de la 'a' a la 'z'.
Su longitud no sera mayor a 1000 caracteres.
Salida
Por cada caso de prueba, imprimir la cantidad de letras necesarias para imprimir dicho texto.
Ejemplo Entrada:
1
sadfasd
Ejemplo Salida:
4
Ayuda
""
import sys
def contarLetras(cadena, letra):
    cont = 0
    for i in cadena:
        if i == letra:
            cont += 1
    return cont
def eliminarLetras(cadena, letra):
    cadena = cadena.replace(letra, "")
    return cadena
def proceso():
    s = sys.stdin.readline().rstrip()
    cont = 0
    temp = s
    for i in range(len(str(s))):
        temp = eliminarLetras(temp, temp[0])
        cont += 1
        if len(temp) == 0:
            break
    print(cont)
def main():
    e = int(sys.stdin.readline())
    for i in range(e):
        proceso()
main()
