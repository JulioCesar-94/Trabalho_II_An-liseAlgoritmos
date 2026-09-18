"""Implemente as três filas de prioridade sem usar heapq."""

from __future__ import annotations

# --------------- Implementação da Heap binária -----------------------------------------------------
class BinaryHeapHandle:
    """
    Identificador opaco possui os atributos key (prioridade/distância até o nó), vertex (valor/vértice)
    e o índice que revela a posição na heap.
    """
    def __init__(self, key, value, idx):
        self.key = key
        self.vertex = value
        self.idx = idx

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def swap_nodes(self, i, j):
        """
        Troca dois elementos do array e atualiza os indíces nos handles
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.heap[i].idx = i
        self.heap[j].idx = j

    def heapify_up(self, idx: int):
        """
        Subir o elemento na árvore caso seja menor que o pai
        """
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx].key < self.heap[parent].key:
                self.swap_nodes(parent, idx)
                idx = parent
            else:
                break

    def heapify_down(self, idx: int):
        """
        Desce o elemento na árvore caso seja maior que algum dos descendentes
        """
        size = len(self.heap)
        while True:
            child = idx
            left = 2*idx + 1
            right = 2*idx + 2

            if left < size and self.heap[left].key < self.heap[child].key:
                child = left
            if right < size and self.heap[right].key < self.heap[child].key:
                child = right

            if child != idx:
                self.swap_nodes(child, idx)
                idx = child
            else:
                break

    def push(self, vertex: int, priority: float):
        """
        Insere um novo Handle na heap binária
        Retorna o novo Handle inserido
        """
        new_element = BinaryHeapHandle(priority, vertex, len(self.heap))
        self.heap.append(new_element)
        self.heapify_up(new_element.idx)
        return new_element

    def decrease_key(self, handle: BinaryHeapHandle, new_priority: float) -> None:
        """
        Diminui a chave do Handle referenciado
        """
        if new_priority > handle.key:
            raise ValueError

        handle.key = new_priority
        self.heapify_up(handle.idx)

    def pop_min(self) -> tuple[int, float]:
        """
        Extrai o valor que está na raiz (recupera e remove)
        Se a heap estiver vazia, lança IndexError
        """
        if (self.__len__() == 0):
            raise IndexError

        minimum = self.heap[0]
        last = self.heap[len(self.heap) - 1]
        self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self.heap[0].idx = 0
            self.heapify_down(0)

        return minimum.vertex, minimum.key


    def __len__(self) -> int:
        return len(self.heap)



# --------------- Implementação da Heap binomial -----------------------------------------------------

class BinomailNode:
    def __init__(self, key):
        self.key = key

class BinomialHeap:
    def __init__(self):
        raise NotImplementedError

    def push(self, vertex: int, priority: float):
        raise NotImplementedError

    def decrease_key(self, handle, new_priority: float) -> None:
        raise NotImplementedError

    def pop_min(self) -> tuple[int, float]:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

# --------------- Implementação da Heap de Fibonacci --------------------------------------------------

class FibonacciNode:
    def __init__(self, key):
        self.key = key

class FibonacciHeap:
    def __init__(self):
        raise NotImplementedError

    def push(self, vertex: int, priority: float):
        raise NotImplementedError

    def decrease_key(self, handle, new_priority: float) -> None:
        raise NotImplementedError

    def pop_min(self) -> tuple[int, float]:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError


#------------ Testes ------------
