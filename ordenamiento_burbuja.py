import random

def ordenamiento_burbuja(lista):

    n = len(lista)

    for i in range(n):
        print(i)
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista?: '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    

    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)
    print(lista)