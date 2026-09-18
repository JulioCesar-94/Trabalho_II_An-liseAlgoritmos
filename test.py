import unittest

# Programa de teste básico para verificar o algoritmo das heaps

from heaps import BinomialHeap, BinaryHeap, FibonacciHeap

class TestPriorityQueues(unittest.TestCase):

    def setUp(self):
        # Instancia as 3 heaps para rodar cada teste em todas elas
        self.heaps = {
            "BinaryHeap": BinaryHeap(),
            "BinomialHeap": BinomialHeap(),
            "FibonacciHeap": FibonacciHeap()
        }

    def test_pop_min_empty_raises_index_error(self):
        """O método pop_min, quando chamado em uma estrutura vazia, deve lançar IndexError."""
        for name, heap in self.heaps.items():
            with self.subTest(heap=name):
                self.assertEqual(len(heap), 0)
                with self.assertRaises(IndexError):
                    heap.pop_min()

    def test_decrease_key_increase_raises_value_error(self):
        """Uma tentativa de aumento de prioridade deve lançar ValueError."""
        for name, heap in self.heaps.items():
            with self.subTest(heap=name):
                h1 = heap.push(vertex=1, priority=10.0)
                
                # Tentativa de aumentar de 10.0 para 15.0
                with self.assertRaises(ValueError):
                    heap.decrease_key(h1, 15.0)
                
                # Tentativa de passar a mesma prioridade (não deve lançar erro se for <=)
                heap.decrease_key(h1, 10.0)

    def test_basic_push_and_pop(self):
        """Insere elementos e garante que a extração ocorre do menor para o maior."""
        for name, heap in self.heaps.items():
            with self.subTest(heap=name):
                data = [(1, 50.0), (2, 10.0), (3, 30.0), (4, 20.0)]
                for vertex, priority in data:
                    heap.push(vertex, priority)

                self.assertEqual(len(heap), 4)

                # Ordem esperada após remoções: vértice 2 (10), vértice 4 (20), vértice 3 (30), vértice 1 (50)
                self.assertEqual(heap.pop_min(), (2, 10.0))
                self.assertEqual(heap.pop_min(), (4, 20.0))
                self.assertEqual(heap.pop_min(), (3, 30.0))
                self.assertEqual(heap.pop_min(), (1, 50.0))
                self.assertEqual(len(heap), 0)

    def test_decrease_key_single_element(self):
        """Testa o decrease_key alterando a prioridade do menor elemento."""
        for name, heap in self.heaps.items():
            with self.subTest(heap=name):
                h1 = heap.push(vertex=10, priority=100.0)
                h2 = heap.push(vertex=20, priority=50.0)

                # Garante que 20 viria antes (50.0 < 100.0)
                # Diminui a chave de h1 para 5.0 -> h1 deve virar o menor
                heap.decrease_key(h1, 5.0)

                self.assertEqual(heap.pop_min(), (10, 5.0))
                self.assertEqual(heap.pop_min(), (20, 50.0))

    def test_decrease_key_multiple_times_on_same_handle(self):
        """Testa reordenamentos consecutivos usando o MESMO handle."""
        for name, heap in self.heaps.items():
            with self.subTest(heap=name):
                h1 = heap.push(vertex=1, priority=100.0)
                h2 = heap.push(vertex=2, priority=80.0)
                h3 = heap.push(vertex=3, priority=60.0)

                # 1ª atualização de h1: de 100 para 70 (agora está entre h2 e h3)
                heap.decrease_key(h1, 70.0)
                
                # 2ª atualização de h1: de 70 para 10 (agora passa a ser a raiz de menor prioridade)
                heap.decrease_key(h1, 10.0)

                self.assertEqual(heap.pop_min(), (1, 10.0))
                self.assertEqual(heap.pop_min(), (3, 60.0))
                self.assertEqual(heap.pop_min(), (2, 80.0))

    def test_dijkstra_like_stress_test(self):
        """Simula o padrão de acessos do algoritmo de Dijkstra (múltiplos push e decrease_key intercalados)."""
        for name, heap in self.heaps.items():
            with self.subTest(heap=name):
                handles = {}
                # Inserção de 100 vértices com prioridade inicial 1000.0
                for v in range(100):
                    handles[v] = heap.push(vertex=v, priority=1000.0)

                # Atualiza os vértices pares com menor prioridade
                for v in range(0, 100, 2):
                    heap.decrease_key(handles[v], float(v))

                # O primeiro a sair deve ser o vértice 0 (prioridade 0.0)
                v_min, p_min = heap.pop_min()
                self.assertEqual((v_min, p_min), (0, 0.0))

                # Atualiza o vértice 99 (ímpar) para passar na frente dos restantes
                heap.decrease_key(handles[99], -1.0)
                self.assertEqual(heap.pop_min(), (99, -1.0))


if __name__ == "__main__":
    unittest.main()