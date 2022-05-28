#Problem 1566
"""
Descripción
Se te dara un conjunto S de numeros y un conjunto de preguntas Q. Una pregunta Q es un numero entero y se te pide encontrar  la suma de dos numeros distintos en S tal que este lo mas cerca posible a Q.

Entrada
La entrada tiene multiples casos de prueba. Cada una empieza con un numero n (1≤n≤1000), que representa el total de numeros del conjunto S, luego siguen n numeros que son los numero del conjunto S. Luego se te dara un numero m (1≤25≤m) que representa el numero de preguntas Q. La entrada termina cuando n sea igual a 0

Salida
La salida debe organizarse como en el ejemplo a continuación. Para cada pregunta imprime la pregunta Q y la suma mas cercana a Q.(Vea la aclaración de entrada en ayuda)
Ejemplo Entrada
5
3
12
17
33
34
3
1
51
30
3
1
2
3
3
1
2
3
3
1
2
3
3
4
5
6
0
Ejemplo Salida
Case 1:
Closest sum to 1 is 15.
Closest sum to 51 is 51.
Closest sum to 30 is 29.
Case 2:
Closest sum to 1 is 3.
Closest sum to 2 is 3.
Closest sum to 3 is 3.
Case 3:
Closest sum to 4 is 4.
Closest sum to 5 is 5.
Closest sum to 6 is 5.
"""


def main():                                                             #1
    contador = 1
    while True:
        n = int(input())                                                #1
        if n == 0:
            break
        v = []                                                          #1
        for i in range(n):                                              #n+1
            v.append(int(input()))                                      #n
        q = int(input())                                                #1
        print("Case "+str(contador)+":")                                #1
        contador += 1                                                   #1
        while q > 0:                                                    #m
            m = int(input())                                            #m-1
            diferencia = 10**9                                          #m-1
            numero = 0                                                  #m-1
            for i in range(n-1):                                        #n(m-1)
                for j in range(i+1, n):                                 #n-1(n-1)(m-1)
                    suma = v[i] + v[j]                                  #n-1(n-2)(m-1)
                    difer = abs(suma - m)                               #n-1(n-2)(m-1)
                    if difer < diferencia:                              #n-1(n-2)(m-1)
                        diferencia = difer                              #n-1(n-2)(m-1)
                        numero = suma                                   #n-1(n-2)(m-1)
            print("CLosest sum to "+str(m)+" is "+str(numero)+".")      #m-1
            q -= 1                                                      #m-1
main()#                                                                 t(n) = 7+2n+m+5(m-1)+n(m-1)+(n-1)(n-1)(m-1)+5((n-1)(n-2)(m-1))
#                                                                       t(n) = -6n^2+18n+17m-16nm+6n^2m-9
#                                                                       t(n) pertenece O(n^2,m)