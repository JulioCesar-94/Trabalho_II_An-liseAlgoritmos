# Relatório experimental

## Ambiente e protocolo

<!-- Descreva máquina, Python, semente, aquecimento e repetições. -->
O ambiente em que esse trabalho foi feito os experimentos é numa máquina com sistema operacional Linux Ubuntu 24.04.4 LTS, com a versão do Python 3.13.12, semente de 2027 e cada experimento será realizado 7 vezes, extraindo a mediana e o desvio mediano.

## Famílias de grafos

<!-- Descreva pelo menos três famílias e quatro tamanhos por família. -->
Famílias:
    Grafo completo:
        Todos os nós se ligam a todos os outros através de arestas não direcionadas,
        E ~ V^2

    Árvore Geradora/Spanning Tree:
        Grafo conectado acíclico não direcionado,
        E = V-1,
        Implementação: Wilson's Algorithm

    Grafo Acíclico Direcionado/Directed Acyclic Graph:
        Grafo conectado acíclico e direcionado,
        E ~ V^2,
        Implementação: Erdős–Rényi G(n, p) Model, com p = 0.3

    Grafo Vazio:
        Grafo sem arestas,
        E = 0


Tamanhos:
    Foram utilizados grafos formados por 10, 100, 250, 500, 750, 1000, 1500, 2000, 2500 nós para
    testar os heaps em execuções de Djikstra em diferentes tipos de grafos com diferentes ordens
    de magnitude de tamanho, verificando complexidades de dijkstra e heaps. Tamanhos escolhidos
    também são númerosos e uniformemente espaçados o suficiente para formarem gráficos capazes de
    melhor visualizar as diferenças de complexidade.


## Resultados

<!-- Inclua unidades e dispersão. -->

Tabela 'benchmarking.csv' é criada ao executar 'benchmark.py', tabela então transformada em
gráficos para melhor análise em ''.
Os dados medidos e armazenados foram:
    Tamanho: Medida adimensional, representa a quantidade de arestas geradas no grafo.
    Tempo mediano: Medida em segundos, representa duração mediana dos tempos de execução de determinado grafo, heap, tamanho.
    Variação mediana: Medida em segundos, representa a mediana das diferenças entre cada execução e o tempo mediano.
    Push, Pop, Decrease Key: Medida adimensional, representa a quantidade de operações do tipo executadas.


## Discussão

<!-- Relacione resultados, operações dominantes e análise assintótica. -->

A efetividade de cada tipo de heap depende altamente da família do tamanho do grafo utilizado
no algoritom de Djikstra, não necessariamente seguindo a eficiência sugerida pela complexidade
assintótica. O tipo de família de grafo afeta a distribuição de arestas e, mais importantemente,
a densidade do grafo gerado, afetando a fração em que operações de decrease_key representam com
o total de operações de heap.
Para grafos esparsos como vazios e árvores geradoras, o heap binário é significativamente mais rápido em todos
os tamanhos


## Limitações e ameaças à validade

1. Implementação usada de Grafos Acíclicos Direcionados, Erdős–Rényi G(n, p) Model, é um
algoritmo estocástico que requer como argumentos uma constante (p | 0 < p < 1), desse modo,
seu comportamento tem alta dependência dos valores de p e de semente usados, podendo, em
casos extremos, gerar nenhuma aresta ou metade de um grafo completo, variando então o tempo
de execução do algoritmo de Djikstra ao alterar número e ordem de chamadas de cada tipo
operação de heap.

2. Testes foram executados em computadores pessoais e não especializados em consistência
necessária para executar testes altamente precisos de tempo de execução dos algoritmos,
havendo pequenas diferenças tempos de execução em diferentes instantes.

3.