"""Implemente as três filas de prioridade sem usar heapq."""

from __future__ import annotations
import math

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
        max_node.right = min_node.left
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
        self.union_trees(new_element)
        self.size += 1

        return new_element

    def remove_from_tree(self, node: BinomailNode):
        """
        Remove um nó de uma árvore
        """
        parent = node.parent
        if not parent:
            return

        if parent.left == node:
            parent.left = node.right
        else:
            curr = parent.left
            while curr and curr.right != node:
                curr = curr.right
            if curr:
                curr.right = node.right

        parent.degree -= 1
        node.parent = None
        node.right = None

    def decrease_key(self, handle: BinomailNode, new_priority: float) -> None:
        """
        Diminui a prioridade do nó referenciado por handle
        Lança Value Error caso a prioridade seja maior
        """
        if new_priority > handle.key:
            raise ValueError

        handle.key = new_priority
        current = handle

        if not handle.parent or handle.key >= handle.parent.key:
            return

        # Remove o handle atual da árvore
        self.remove_from_tree(handle)

        # Reinsere o handle na árvore para atualizar os ponteiros
        self.union_trees(handle)

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
            next_son = son.right
            son.right = new_head
            son.parent = None
            new_head = son
            son = next_son

        self.union_trees(new_head)
        self.size -= 1

        return min_node.vertex, min_node.key

    def __len__(self) -> int:
        return self.size

# --------------- Implementação da Heap de Fibonacci --------------------------------------------------

class FibonacciNode:
    def __init__(self, key: float, vertex: int):
        self.key = key
        self.vertex = vertex
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.degree = 0
        self.mark = False

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.size = 0

    def add_to_root_list(self, new_node: FibonacciNode):
        """
        Insere o nó na lista circular de raízes
        """
        if self.min_node == None:
            self.min_node = new_node
            new_node.left = new_node
            new_node.right = new_node
        else:
            new_node.left = self.min_node.left
            new_node.right = self.min_node
            self.min_node.left.right = new_node
            self.min_node.left = new_node


    def remove_from_root_list(self, node:FibonacciNode):
        """
        Remove um nó da lista circular de raízes
        """
        node.left.right = node.right
        node.right.left = node.left

    def link_nodes(self, y: FibonacciNode, x: FibonacciNode):
        """
        Remove y da lista de raízes e faz com que seja filho de x
        """
        self.remove_from_root_list(y)
        y.parent = x
        if x.child == None:
            x.child = y
            y.left = y
            y.right = y
        else:
            y.left = x.child.left
            y.right = x.child
            x.child.left.right = y
            x.child.left = y

        x.degree += 1
        y.mark = False

    def consolidate(self):
        """
        Consolida as árvores de mesmo grau na lista de raízes
        Evitar que a lista de raízes fique maior
        """
        max_degree = 1
        if self.size > 0:
            max_degree = int(2*math.log2(self.size)) + 5

        A = [None]*max_degree

        nodes = []
        if self.min_node:
            current = self.min_node
            nodes.append(current)
            current = current.right
            while current != self.min_node:
                nodes.append(current)
                current = current.right

        for node in nodes:
            x = node
            d = x.degree
            while d < len(A) and A[d] != None:
                y = A[d]
                if x.key > y.key:
                    x, y = y, x
                self.link_nodes(y, x)
                A[d] = None
                d += 1

            if d < len(A):
                A[d] = x

        self.min_node = None
        for i in range(len(A)):
            if A[i] != None:
                if self.min_node == None:
                    self.min_node = A[i]
                    A[i].left = A[i]
                    A[i].right = A[i]
                else:
                    self.add_to_root_list(A[i])
                    if A[i].key < self.min_node.key:
                        self.min_node = A[i]

    def cut(self, x: FibonacciNode, y:FibonacciNode):
        """
        Remove x da lista de filhos do y e coloca-o na lista de raízes
        """
        if x == x.right:
            y.child = None

        else:
            # Remoção do x da lista de filhos do y (reorganização de ponteiros)
            x.left.right = x.right
            x.right.left = x.left
            if y.child == x:
                y.child = x.right

        # Insere o x na lista de raízes
        y.degree -= 1
        self.add_to_root_list(x)
        x.parent = None
        x.mark = False

    def cascading_cut(self, node: FibonacciNode):
        z = node.parent
        if z != None:
            if node.mark == False:
                node.mark = True
            else:
                self.cut(node, z)
                self.cascading_cut(z)
        

    def push(self, vertex: int, priority: float):
        """
        Insere o novo elemento na heap de Fibonacci em complexidade O(1)
        Retorna o nó como identificador/Handle
        """
        new_element = FibonacciNode(priority, vertex)
        self.add_to_root_list(new_element)
        if self.min_node == None or new_element.key < self.min_node.key:
            self.min_node = new_element

        self.size += 1
        return new_element

    def decrease_key(self, handle: FibonacciNode, new_priority: float) -> None:
        """
        Atualiza a prioridade de um Handle para um menor
        Se tentar aumentar a prioridade, retorna um ValueError
        """
        if new_priority > handle.key:
            raise ValueError

        handle.key = new_priority
        y = handle.parent
        if y != None and handle.key < y.key:
            self.cut(handle, y)
            self.cascading_cut(y)

        if handle.key < self.min_node.key:
            self.min_node = handle

    def pop_min(self) -> tuple[int, float]:
        """
        Extrai o menor elemento e reajusta a estrutra complexidade logarítmica amortizada
        """
        if self.min_node == None:
            raise IndexError

        z = self.min_node

        # Adiciona todos os filhos de min_node à lista de raízes
        if z.child != None:
            children = []
            current = z.child
            children.append(current)
            current = current.right
            while current != z.child:
                children.append(current)
                current = current.right

            for x in children:
                self.add_to_root_list(x)
                x.parent = None

        # Remove o min_node da lista de raízes
        self.remove_from_root_list(z)

        # Consolida das árvores de mesmo grau (maior 'trabalho' e custo)
        if z == z.right:
            self.min_node = None
        else:
            self.min_node = z.right
            self.consolidate()

        self.size -= 1
        return z.vertex, z.key

    def __len__(self) -> int:
        return self.size


#------------ Testes ------------

heap = BinomialHeap()

v1 = heap.push(1, 7.0)
v2 = heap.push(2, 9.0)
v3 = heap.push(3, 5.0)

heap.decrease_key(v2, 2.0)
heap.decrease_key(v3, 1.0)

print(heap.pop_min())
print(heap.pop_min())
print(heap.pop_min())
