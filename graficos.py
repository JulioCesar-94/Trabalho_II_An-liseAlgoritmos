
import csv
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# Para o código não travar em plt.plot()
matplotlib.use('Agg')

# Caso alterar algum desses, rodar benchmark antes desse arquivo
from benchmark import tam_grafos, heap_class, fam_grafos


def find(list, graph, heap, column):
    ret = []

    for row in list:
        if row[0] == graph and row[1] == heap:
            ret.append(float(row[column + 3]))

    return ret


def plot(list, graph, column):
    plt.clf()
    for heap in heap_class:
        plt.plot (tam_grafos, find(list, graph, heap, column), label=heap)
    saida = header[column + 3] + " x Tamanho de grafo (" + graph + ")"
    plt.title(header[column + 3] + " x Tamanho de grafo (" + graph + ")")
    plt.xlabel("Tamanho de grafo")
    plt.ylabel(header[column + 3])
    plt.legend()

    saida = "img/" + saida
    plt.savefig(saida)
    return saida



benchmarking = []

with open('benchmarking.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)

    header = next(reader) 

    for row in reader:
        benchmarking.append(row)



for grafo in fam_grafos:
    for i in range(0, 5):
        print ("Arquivo criado: " + plot(benchmarking, grafo[0], i))
