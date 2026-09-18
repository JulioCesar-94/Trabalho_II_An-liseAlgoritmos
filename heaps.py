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
    """
    Cria a estrutura do nó da arvore binomial: possui os campos da chave(distância) e vértice
    Além disso, possui o grau do nó e ponteiros para o pai e os filhos da direita e esquerda
    """
    def __init__(self, key: float, vertex: int):
        self.key = key
        self.vertex = vertex
        self.degree = 0
        self.parent = None
        self.left = None
        self.right = None


class BinomialHeap:
    def __init__(self):
        self.head = None
        self.size = 0

    def link(self, min_node: BinomailNode, max_node: BinomailNode):
        """
        Junta o min_node com o max_node
        Fazendo com que o max_node vire o filho esquerdo de min_node
        """
        max_node.parent = min_node
        max_node.right = max_node.left
        min_node.left = max_node
        min_node.degree += 1

    def merge_roots(self, h1: BinomailNode, h2: BinomailNode) -> BinomailNode:
        if not h1:
            return h2
        if not h2:
            return h1

        if h1.degree <= h2.degree:
            new_head = h1
            h1 = h1.right
        else:
            new_head = h2
            h2 = h2.right
        tail = new_head

        while h1 and h2:
            if h1.degree <= h2.degree:
                tail.right = h1
                h1 = h1.right
            else:
                tail.right = h2
                h2 = h2.right
            tail = tail.right

        if h1:
            tail.right = h1
        if h2:
            tail.right = h2

        return new_head


    def union_trees(self, new_node: BinomailNode):
        """
        Une o novo nó com a floresta da heap binomial
        """
        new_head = self.merge_roots(self.head, new_node)
        if not new_head:
            self.head = None
            return

        prev = None
        curr = new_head
        next_node = curr.right

        while next_node:
            if (curr.degree != next_node.degree) or (next_node.right and next_node.right.degree == curr.degree):
                prev = curr
                curr = next_node
            else:
                if curr.key <= next_node.key:
                    curr.right = next_node.right
                    self.link(curr, next_node)
                else:
                    if not prev:
                        new_head = next_node
                    else:
                        prev.right = next_node
                    self.link(next_node, curr)
                    curr = next_node

            next_node = curr.right

        self.head = new_head

    def push(self, vertex: int, priority: float):
        """
        Insere um novo nó na heap binomial
        """
        new_element = BinomailNode(priority, vertex)

        tree_B0 = BinomialHeap()
        tree_B0.head = new_element
        tree_B0.size = 1
        self.union(new_element)
        self.size += 1

        return new_element
        

    def decrease_key(self, handle: BinomailNode, new_priority: float) -> None:
        """
        Diminui a prioridade do nó referenciado por handle
        Lança Value Error caso a prioridade seja maior
        """
        if new_priority > handle.key:
            raise ValueError

        handle.key = new_priority
        current = handle

        while current.parent and current.key < current.parent.key:
            current.key, current.parent.key = current.parent.key, current.key
            current.vertex = current.parent.vertex = current.parent.vertex, current.key
            current = current.parent

    def pop_min(self) -> tuple[int, float]:
        """
        Retorna o par da raiz de menor chava
        Lança IndexError caso a heap esteja vazia
        """
        if self.head == None:
            raise IndexError

        min_node = self.head
        min_prev = None
        prev = self.head
        current = self.head.right

        while current:
            if current.key < min_node.key:
                min_node = current
                min_prev = prev
            prev = current
            current = current.right

        if min_prev:
            min_prev.right = min_node.right
        else:
            self.head = min_node.right

        son = min_node.left
        new_head = None
        while son:
            son.right = new_head
            son.parent = None
            new_head = son
            son = son.right

        self.union_trees(new_head)
        self.size -= 1

    def __len__(self) -> int:
        return self.size

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
