"""Experimento reproduzível; complete e gere os dados do relatório."""

from __future__ import annotations

import random
import statistics
from dijkstra import Graph, dijkstra
from heaps import PriorityQueue
import time

SEED = 2027

heap_class = ['binary', 'binomial', 'fibonacci']
tam_grafos = [10, 100, 500, 1000]
fam_grafos = ['completo', 'dag', 'esparso']

# Função que gera um grafo completo e não direcionado(Kn), em que E é quase V²
def gerar_grafoCompleto(n: int):

    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i < j:
                weight = round(random.uniform(1.0, 100.0), 1)
                graph[i].append((j, weight))
                graph[j].append((i, weight))

    return graph

# Função para gerar um grafo acíclico e direcionado (DAG)
def gerar_grafoDAG(n: int):
    pass

# Função para gerar um grafo esparso e não direcionado, cujo E == V
def gerar_grafoEsparso(n: int):
    pass


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
    print(gerar_grafoCompleto(5))

    for tam in tam_grafos:
        for tipo in fam_grafos:
            if tipo == 'completo':
                Graph = gerar_grafoCompleto(tam)

            #elif tipo == 'dag':
            #    Graph = gerar_grafoDAG(tam)

            #elif tipo == 'esparso':
            #    Graph = gerar_grafoEsparso(tam)

            print(f"Grafo: {tipo} com tamanho {tam}")
            for heap in heap_class:
                print(f"{heap}: {medir(Graph, heap)}")
            print()


if __name__ == "__main__":
    main()

