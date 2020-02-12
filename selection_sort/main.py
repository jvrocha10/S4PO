import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint, shuffle
import timeit

def plot_grafico(x, y, z, pasta, l1, l2, xl = "Entrada de valores", yl = "Saída de valores"):
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label= l1)
    ax.plot(x, z, label= l2)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)

    fig.savefig(pasta)

def geraLista(tam):
    lista = list(range(1, tam+1))
    shuffle(lista)
    return lista

def selection_sort(lista):
    count = 0
    flag = False
    for i in range(len(lista)):
        min = i
        for j in range(i + 1, len(lista)):
            count += 1
            if lista[min] > lista[j]:
                min = j

        aux = lista[i]
        lista[i] = lista[min]
        lista[min] = aux


    return count

x = [1000, 10000,30000, 60000]
y = []
y_des = []
tempo_ord = []
count_ord = []
tempo_des = []
count_des = []

for i in range(len(x)):
    y.append(geraLista(x[i]))
    count_ord.append(selection_sort(y[i]))
    aux = list(range(1, x[i]))
    aux.reverse()
    y_des.append(aux)
    count_des.append(selection_sort(y_des[i]))

for i in range(len(x)):
    tempo_ord.append(timeit.timeit("selection_sort({})".format(y[i]), setup="from __main__ import selection_sort", number=1))
    tempo_des.append(timeit.timeit("selection_sort({})".format(y_des[i]), setup="from __main__ import selection_sort", number=1))

plot_grafico(x, tempo_ord, tempo_des, "Tempo.png", "Tempo Embaralhado", "Tempo Invertido")
plot_grafico(x, count_ord, count_des, "Interacoes.png", "Interacoes Embaralhado", "Interacoes Invertido")
