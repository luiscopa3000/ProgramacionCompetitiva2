#Problem 1522
"""
Descripción
Matilde gusta de las matemáticas, y de hecho compite en las olimpiadas de matemáticas de su colegio; ella ha logrado batir a todos sus compañeros en un simple juego que tiene que ver con los factoriales.

Alan es un amigo de Matilde y apostó con ella que puede vencerle en su juego de factoriales. El día de mañana ellos se enfrentarán y Alan esta en problemas, necesita con urgencia que le ayuden a realizar un programa que sea capaz de vencer a Matilde!

El juego de los factoriales consiste en que dado un numero n, los jugadores deben calcular lo más rápidamente posible el dígito menos significativo (el de las unidades) del número n!. Matilde siempre ha sido la más veloz en responder y responde con exactitud.

Ahora los factoriales son fáciles de calcular, para un numero n, su factorial n! se calcula multiplicando 1∗2∗3∗...∗(n−2)∗(n−1)∗n

En matemáticas el 0 en factorial es 0!=1, y se puede decir que: 0!=1,1!=1,2!=1∗2,3!=1∗2∗3 y así  sucesivamente.

Puedes ayudar a que Alan consiga un programa lo suficientemente rápido en calcular el dígito que corresponde a las unidades para n! siendo n un numero entero positivo?
Entrada
La primera línea contiene un número M entero que indica la cantidad de casos de prueba.
A partir de la segunda línea se tienen los casos de prueba (uno por línea), para cada caso de prueba se tiene un único numero entero positivo (n≤109) del que se debe calcular la respuesta (el dígito de las unidades de n!).
Salida
Para cada caso de prueba imprimir la respuesta que consiste en el  dígito de las unidades de n!, siendo n la entrada del caso de prueba.
Ejemplo Entrada
3
3
2
0
Ejemplo Salida
6
2
1
"""
def factorial(n):                           #1
    if n == 0:                              
        return 1                            
    else:                                   #1    
        return n * factorial(n-1)           #t(n-1)+1
def main():                                 #1
    n = int(input())                        #!
    for i in range(n):                      #n+1
        k = int(input())                    #n
        if k >4:                            #n            
            print("0")
        else:                               
            print(factorial(k)[len(factorial(k))-1])        #n(2n+2)
main()