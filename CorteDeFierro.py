#Problem 1724
"""""
Descripción
    Tienes un barra fierro de la construcción de longitud n. Quieres cortar esta barra en multiples piezas donde cada pieza es un numero entero positivo. La condición es que todas las piezas sean de distinto tamaño.

    Si es posible escriba posible y en caso contrario imposible, como se muestra en el ejemplo.

    Si la entrada es 9 y 3 significa que la longitud de la barra es 9 y queremos 3 piezas diferentes.
    Una posible solución es hacer cortes de longitud 1,3,5, por lo que la respuesta es posible.

Entrada
    La entrada consiste de varios casos de prueba y termina cuando no hay más datos.
    Cada caso de prueba consiste de dos números enteros la longitud de fierro entre 1 y 1,000,000 y el numero de piezas que se requiere. que hay que hacer.

Salida
    Imprima lo solicitado.

Ejemplo Entrada
9 3
12 1
9 4
10 4
750932 901
54 10

Ejemplo Salida
posible
posible
imposible
posible
posible
imposible
"""
import sys
def verificar(x,y):                             #1
    c = int(y**2-(y*(y-1)/2))                   #1
    if c<=x:                                    #1
        return True                             #1
    else:
        return False                            #1
#                                          ----------
#                                          t(n) = 5
#                                          ----------
#                                          t(n) pertenece O(1)

def main():                                 #1
    for linea in sys.stdin:                 
        if linea == '\n':                   
            break                           
        x,y = map(int,linea.split())        #1
        if verificar(x,y):                  #5
            print("posible")                #1
        else:
            print("imposible")
#                                          ----------
#                                           t(n) = 7
main()#                                  t(n) = 7
#                                        t(n) pertenece O(1)

