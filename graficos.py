
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


def findWith(list, graph, heap, tam, column):
    for row in list:
        if row[0] == graph and row[1] == heap and str(row[2]) == str(tam):
            return row[column + 3]


def plotTempo(list, graph, column):
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


def plotOperacoes(list):
    plt.clf()

    frac = []

    # Pegando apenas string de nome em fam_grafos.
    grafos = [x[0] for x in fam_grafos]

    # Devido ao funcionamento de djikstra.py, relação de número de operações
    # decrease_key / Push depende apenas do tipo de grafo utilizado, sendo
    # constante em heap e tamanho. Por isso, fixou-se heap arbitrariamente
    # e tamanho em um valor alto.
    for tipo in grafos:
        frac.append(float(findWith(list, tipo, heap_class[0], tam_grafos[-1], 4)) /
                    float(findWith(list, tipo, heap_class[0], tam_grafos[-1], 2)))

    plt.bar(grafos, frac)
    plt.title('Relação Decrease-Key/Push')
    plt.xlabel('Família de grafo')
    plt.ylabel('DK/Push')

    saida = "img/Relação DK-Push"
    plt.savefig(saida)
    return saida





benchmarking = []

with open('benchmarking.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)

    header = next(reader) 

    for row in reader:
        benchmarking.append(row)



for grafo in fam_grafos:
    for i in range(0, 2):
        print ("Arquivo criado: " + plotTempo(benchmarking, grafo[0], i))

print ("Arquivo criado: " + plotOperacoes(benchmarking))