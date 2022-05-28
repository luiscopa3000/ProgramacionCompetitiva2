import numpy as np
from sympy import true
def proceso():
    #n = int(input())
    n = 200
    x = 2
    v = [1]
    c =2; sw = True; z= 1; h = 3; sw2=False; m = 1; i =5
    while x <= n:
        if sw:
            v.append(x)
            z -= 1
            if z == 0:
                sw = False
        else:
            #print(m)
            m += 1
            print(m)
            print(v)
            v.append(1000)
            sw = True
            if sw2 == False:
                z = 2
                sw2 = True
                h = 1
            else:
                sw2 = False
                z = 2*c
                if h == 1:
                    c += 1
                    h =0
                    sw2 = True
            if  m == i:
                sw = False
                print("Entraaaaa-.")
                m = -1
                #i += 1
                if sw2 == true:
                    sw2 = False
            
        x += 1
    print(v)
proceso()


