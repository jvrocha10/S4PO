import timeit

from random import randint, shuffle

import matplotlib.pyplot as plt



def desenhaGrafico(x, y, xl="Entradas", yl="Saidas", name="out"):

    fig = plt.figure(figsize=(12, 10))

    ax = fig.add_subplot(111)

    ax.plot(x, y, label="Lista Aleatória")

    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)

    plt.ylabel(yl)

    plt.xlabel(xl)

    plt.savefig(name)





def generateList(size):

    lista = list(range(1, size + 1))

    shuffle(lista)

    return lista





def heapify(arr, n, i): 

    largest = i  

    l = 2 * i + 1     

    r = 2 * i + 2     

  

    if l < n and arr[i] < arr[l]: 

        largest = l 



    if r < n and arr[largest] < arr[r]: 

        largest = r 

  

    if largest != i: 

        arr[i],arr[largest] = arr[largest],arr[i]  

        heapify(arr, n, largest) 



def heapSort(arr): 

    n = len(arr) 

  

    for i in range(n, -1, -1): 

        heapify(arr, n, i) 

  

    for i in range(n-1, 0, -1): 

        arr[i], arr[0] = arr[0], arr[i]  

        heapify(arr, i, 0) 

    return(arr)



size = [15000,25000,35000,45000,55000]

time = []



for s in size:

    lista = generateList(s)

    time.append(timeit.timeit("heapSort({})".format(lista),

                              setup="from __main__ import heapSort", number=1))

    print(s)



desenhaGrafico(size, time, "Size", "Time","Tempo.png")
