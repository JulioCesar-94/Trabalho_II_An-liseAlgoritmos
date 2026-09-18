"""Dijkstra parametrizado pela classe da fila de prioridade."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Type
from heaps import PriorityQueue
import math

Graph = Sequence[Sequence[tuple[int, float]]]
    

def dijkstra(graph: Graph, source: int, heap_class: PriorityQueue):
    """Retorne (distancias, predecessores) usando heap_class."""

    # Inicializa os vetores de distâncias e predecessores
    dist = [math.inf]*len(graph)
    pred = [None]*len(graph)

    # A distância até a origem é 0
    dist[source] = 0

    # Armazena todos os indentificadores/handles em um dicionário
    # Para facilitar no decrease_key
    handles = {}
    for c in range(len(graph)):
        handles[c] = heap_class.push(c, dist[c])

    while len(heap_class) > 0:
        # Extrai o elemento de menor prioridade
        u, d = heap_class.pop_min()

        # Se tiver algum elemento cujo d == inf, esse nó é inalcançável pelo source
        if d == math.inf:
            break

        # Para cada vizinho v de u, de peso w
        for v, w in graph[u]:

            # Testa se é possível relaxar a distância
            # Caso sim, diminui a prioridade do vértice v apontado pelo handle
            if (dist[v] > dist[u] + w):
                dist[v] = dist[u] + w
                pred[v] = u
                heap_class.decrease_key(handles[v], dist[v])

    return dist, pred

