from complejidad_algoritmica import factorial, factorial_r 
import time
import sys

if __name__ == '__main__':
    n = 9000
    sys.setrecursionlimit(n + 100)

    comienzo1 = time.time()
    factorial(n)
    final1 = time.time()
    print(final1 - comienzo1)
    print("GOLA")
    print("GOLA")


    comienzo2 = time.time()
    factorial_r(n)
    final2 = time.time()
    imprimir = final2 - comienzo2
    print(imprimir)
    print("GOLA")