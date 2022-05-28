""
Descripción

Andres tiene una cerradura en su casillero de la carrera, esta cerradura es representada por n discos giratorios con dígitos del 0 al 9 escritos en ellos, entonces Andres tiene que girar algunos discos para que la combinación de dígitos de los discos forme una combinación secreta. Con un solo movimiento puede rotar un disco hacia adelante o hacia atrás. En particular en un movimiento puede pasar del dígito 0 al digito 9 y viceversa. Ahora Andres quiere que los ayudes a saber cual es el menor número de movimientos para abrir la cerradura.



Entrada

La primera línea contiene un número n (1<=n<=1000) el numero de discos de la cerradura.

La segunda línea contiene el estado actual de los discos de la cerradura

La tercera línea contiene la combinación secreta para abrir la cerradura.

Salida
Muestre el numero minimo de movimientos que Andres necesita para abrir la cerradura.

Ejemplo Entrada
5
82195
64723
Ejemplo Salida
13
""

# devuelve el minimo entre el movimiento atras y adelante
def minimo(a, b):
    if a <= b:
        return a 
    else: 
        return b
#Cuenta los movimientos necesarios
def contarE(x,y):
    if x <= y:
        return int(y)-int(x)
    else:
        z = int(y)-int(x)
        z = z+10
        return z
def proceso():
    n = int(input())
    x = str(input())
    y = str(input())
    z = 0
    for i in range(n):
        # Movimientos de    6    8             8    6
        z += minimo(contarE(x[i],y[i]),contarE(y[i],x[i]))
    print(z)
proceso()