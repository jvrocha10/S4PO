import timeit

import matplotlib as mpl

import matplotlib.pyplot as plt

from random import shuffle

mpl.use('Agg')



def desenhaGrafico(x, y, figura, xLabel ="Entradas", yLabel ="Saídas"):

    fig = plt.figure(figsize=(12, 8))

    ax = fig.add_subplot(111)

    ax.plot(x, y, label ="Lista")

    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)

    plt.ylabel(yLabel)

    plt.xlabel(xLabel)

    plt.savefig(figura)



def geraLista(tamanho):

    lista = list(range(1, tamanho + 1))

    shuffle(lista)

    return lista



def shellsort(lista):

    tamanho = len(lista)

    intervalo = tamanho // 2



    while intervalo > 0:

        for i in range(intervalo, tamanho):

            aux = lista[i]

            j = i

            while j >= intervalo and lista[j - intervalo] > aux:

                lista[j] = lista[j - intervalo]

                j -= intervalo

            lista[j] = aux

        intervalo //= 2





tamanho = [30000,40000,50000,60000,70000]

tempo = []



for i in range(5):

    lista = geraLista(tamanho[i])

    tempo.append(timeit.timeit("shellsort({})".format(lista), setup="from __main__ import shellsort", number=1))



desenhaGrafico(tamanho, tempo, "Tempo.png", 'Tamanho da lista', 'Tempo')
