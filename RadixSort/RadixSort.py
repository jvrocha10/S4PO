import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import shuffle

mpl.use('Agg')

def desenhaGrafico(x, y, figura, L1 ="Entradas", L2 ="Saídas"):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label ="Lista aleatória")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(L2)
    plt.xlabel(L1)
    plt.savefig(figura)

def geraLista(tamanho):
    lista = list(range(1, tamanho + 1))
    shuffle(lista)
    return lista

def radixsort(lista):
    base = 1
    maior = max(lista)

    while maior/base > 0:
        indice = len(lista) + 1
        ocorrencias = [0] * indice

        for i in lista:
            ocorrencias[i] += 1

        aux = 0

        for i in range(indice):
            for j in range(ocorrencias[i]):
                lista[aux] = i
                aux += 1
        base *= 10


tamanho = [20000,30000,40000,50000,60000]
tempo = []

for i in range(5):
    lista = geraLista(tamanho[i])
    tempo.append(timeit.timeit("radixsort({})".format(lista), setup="from __main__ import radixsort", number=1))

desenhaGrafico(tamanho, tempo, "Tempo.png", 'Tamanho', 'Tempo')
