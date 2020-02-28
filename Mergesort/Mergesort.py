import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import shuffle

mpl.use('Agg')

def desenhaGrafico(x, y, y2, figura, L1 ="Entradas", L2 ="Saídas"):
    fig = plt.figure(figsize=(12, 14))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label ="Lista aleatória")
    ax.plot(x, y2, label="Lista inversa")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(L2)
    plt.xlabel(L1)
    plt.savefig(figura)

def geraLista(tamanho):
    lista = list(range(1, tamanho + 1))
    shuffle(lista)
    return lista

def listaDecrescente(tamanho):
    lista = list(range(1, tamanho + 1))
    lista.reverse()
    return lista

def mergesort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]
        mergesort(esquerda)
        mergesort(direita)

        i = 0
        j = 0
        k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

tamanho = [20000,40000,60000,80000,100000]
tempo = []
tempo2 = []

for i in range(5):
    lista = geraLista(tamanho[i])
    lista2 = listaDecrescente(tamanho[i])
    tempo.append(timeit.timeit("mergesort({})".format(lista), setup="from __main__ import mergesort", number=1))
    tempo2.append(timeit.timeit("mergesort({})".format(lista2), setup="from __main__ import mergesort", number=1))

desenhaGrafico(tamanho, tempo, tempo2, "Tempo.png", 'Tamanho da lista', 'Tempo')
