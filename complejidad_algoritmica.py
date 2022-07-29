import time
import sys

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    
    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial_r(n-1)


if __name__ == '__main__':
    n = 1995
    sys.setrecursionlimit(n + 100)

    comienzo1 = time.time()
    factorial(n)
    final1 = time.time()
    print(final1 - comienzo1)
    print("GOLA")

    comienzo2 = time.time()
    factorial_r(n)
    final2 = time.time()
    imprimir = final2 - comienzo2
    print(imprimir)
    print("GOLA")