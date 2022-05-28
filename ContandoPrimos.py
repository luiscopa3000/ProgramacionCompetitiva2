""
Contando primos
""
import numpy
def primos(n):
    z = numpy.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if z[i]:
            k=3*i+1|1
            z[       k*k//3     ::2*k] = False
            z[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(z)[0][1:]+1)|1)]

def proceso():
    a,b = map(int, input().split())
    if a >= 5 and b > a:
        print(len(primos(b))-len(primos(a)))
    elif a == 2 and a != b:
        print(len(primos(b)))
    elif a == 3 and a != b:
        print(len(primos(b))-1)
    elif a == b:
        print(0)
def main():
    for i in range(int(input())):
        proceso()
main()
