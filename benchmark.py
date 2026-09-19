"""Experimento reproduzível; complete e gere os dados do relatório."""

from __future__ import annotations

import random
import statistics
from dijkstra import Graph, dijkstra
from heaps import PriorityQueue
import time
import math

SEED = 2027
DAGNodeProbability = 0.3

heap_class = ['binary', 'binomial', 'fibonacci']
tam_grafos = [10, 100, 500, 1000]
fam_grafos = [['Completo', 'gerar_grafoCompleto'],
              ['Acíclico direcionado', 'gerar_grafoDAG'],
              ['Gerador', 'gerar_arvoreGeradora']]




# Função que gera um grafo completo e não direcionado(Kn), em que E é quase V²
def gerar_grafoCompleto(n: int):

    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                weight = round(random.uniform(1.0, 100.0), 1)
                graph[i].append((j, weight))
                graph[j].append((i, weight))

    return graph


# Função para gerar um grafo acíclico e direcionado (DAG)
# Utilizando Algoritmo Erdős–Rényi G(n, p), com p = 0.3
# Não é uniforme e não garante conectividade
def gerar_grafoDAG(n: int):

    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if (random.random() < DAGNodeProbability):
                weight = round(random.uniform(1.0, 100.0), 1)
                graph[i].append((j, weight))

    return graph


# Função para gerar uma árvore geradora, cujo E == V - 1
# Utilizando Algoritmo de Wilson, o qual é uniforme
def gerar_arvoreGeradora(n: int):

    graph = [[] for _ in range(n)]

    T = list() # Nós na arvore geradora
    V = list(range(n)) # Nós restantes

    current = random.choice(V)
    T.append(current)
    V.remove(current)


    while len(T) < n:

        # Escolher vértice aleatório não presente na árvore
        path = [-1 for _ in range(n)]
        current = random.choice(V)
        first = current

        # Executar random walk até encontrar árvore
        while current not in T:
            next = random.choice(range(n))
            while next == current:
                next = random.choice(range(n))

            path[current] = next
            current = next

        # Apagar loops e adicionar random walk para árvore
        current = first
        while current not in T:
            next = path[current]
            weight = round(random.uniform(1.0, 100.0), 1)
            graph[current].append((next, weight))
            graph[next].append((current, weight))
            T.append(current)
            V.remove(current)
            current = next

    return graph



# Mede a mediana e o desvio mediano em 7 execuções do algoritmo de dijkstra, dado um grafo e um tipo de heap
def medir(graph: Graph, heap: str, repeticoes: int = 7) -> tuple[float, float]:
    """Retorne mediana e desvio absoluto mediano, em segundos."""
    tempos = []
    for _ in range(repeticoes):
        inicio = time.perf_counter()
        dijkstra(graph, 0, PriorityQueue(heap))
        tempos.append(time.perf_counter() - inicio)
    mediana = statistics.median(tempos)
    mad = statistics.median(abs(t - mediana) for t in tempos)
    return mediana, mad


def main() -> None:
    random.seed(SEED)

    for tam in tam_grafos:
        for tipo in fam_grafos:

            # Executa funcao em tipo
            # tipo: [nome, função]
            Graph = globals()[tipo[1]](tam)

            print(f"Grafo: {tipo[0]} com tamanho {tam}")
            for heap in heap_class:
                print(f"{heap}: {medir(Graph, heap)}")
            print()


if __name__ == "__main__":
    main()

