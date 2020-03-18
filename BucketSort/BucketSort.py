import timeit

import matplotlib as mpl

import matplotlib.pyplot as plt

from random import shuffle



mpl.use('Agg')



def desenhaGrafico(x, y, figura, xLabel ="Entradas", yLabel ="Saídas"):

    fig = plt.figure(figsize=(12, 10))

    ax = fig.add_subplot(111)

    ax.plot(x, y, label ="Lista aleatória")

    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)

    plt.ylabel(yLabel)

    plt.xlabel(xLabel)

    plt.savefig(figura)



def geraLista(tamanho):

    lista = list(range(1, tamanho + 1))

    shuffle(lista)

    return lista



def bucketsort(lista):

    comprimento = len(lista)

    cesta = [[] for _ in range(comprimento)]

    maior = max(lista)

    tamanho = maior/comprimento



    for i in range(comprimento):

        j = int(lista[i] / tamanho)

        if j != comprimento:

            cesta[j].append(lista[i])

        else:

            cesta[comprimento - 1].append(lista[i])



    for i in range(comprimento):

        insertionsort(cesta[i])



    lista_ordenada = []

    for i in range(comprimento):

        lista_ordenada = lista_ordenada + cesta[i]



    return lista_ordenada





def insertionsort(lista):

    for i in range(1, len(lista)):

        atual = lista[i]

        j = i - 1

        while j >= 0 and atual < lista[j]:

            lista[j + 1] = lista[j]

            j -= 1

        lista[j + 1] = atual





tamanho = [15000,25000,35000,45000,55000]

tempo = []



for i in range(5):

    lista = geraLista(tamanho[i])

    tempo.append(timeit.timeit("bucketsort({})".format(lista), setup="from __main__ import bucketsort", number=1))



desenhaGrafico(tamanho, tempo, "Tempo.png", 'Tamanho', 'Tempo')
