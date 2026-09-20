# Relatório experimental

## Ambiente e protocolo

<!-- Descreva máquina, Python, semente, aquecimento e repetições. -->
O ambiente utilizado nos experimentos possui sistema operacional Linux Ubuntu 24.04.4 LTS, com Python 3.13.12 e semente 2027. Para cada combinação de família de grafo, tamanho e heap, foram realizadas 3 rodadas de aquecimento, descartadas da análise, para garantir a estabilidade das medições, seguidas de 10 repetições cronometradas, das quais foram extraídos a mediana e o desvio mediano.

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
    Foram utilizados grafos formados por 10, 100, 250, 500, 750, 1000, 1500, 2000, 2500, 3000, 3500
    nós para testar os heaps em execuções de Djikstra em diferentes tipos de grafos com diferentes
    ordens de magnitude de tamanho, verificando complexidades de dijkstra e heaps. Tamanhos escolhidos
    também são númerosos e uniformemente espaçados o suficiente para formarem gráficos capazes de
    melhor visualizar as diferenças de complexidade.


## Resultados

<!-- Inclua unidades e dispersão. -->

Tabela 'benchmarking.csv' é criada ao executar 'benchmark.py', tabela então transformada em
gráficos para melhor análise em 'graficos.py', armazenados em 'imagens/'.

Há 3 tipos de gráficos em 'imagens/':

### 1.Relação DK/Push 
Gráfico adimensional que mostra a razão entre o número de operações de decrease-key pelas operações de push, quantificando a densidade do tipo      de grafo de acordo com as requisições ao heap.

![Relação DK-Push](imagens/Relação%20DK-Push.png)

### 2.Tempo mediano por tamanho de grafo
Mede a velocidade e o desempenho absoluto do algoritmo em segundos.
## Grafo Gerador
![Tempo mediano (Gerador)](imagens/Tempo%20mediano%20x%20Tamanho%20de%20grafo%20(Gerador).png)

## Grafo Vazio
![Tempo mediano (Vazia)](imagens/Tempo%20mediano%20x%20Tamanho%20de%20grafo%20(Vazia).png)

## Grafo Acíclico Direcionado (DAG)
![Tempo mediano (Acíclico Direcionado)](imagens/Tempo%20mediano%20x%20Tamanho%20de%20grafo%20(Acíclico%20direcionado).png)

## Grafo Completo
![Tempo mediano (Completo)](imagens/Tempo%20mediano%20x%20Tamanho%20de%20grafo%20(Completo).png)

### 3.Variação mediana
Mede a dispersão estatística e a estabilidade das 10 repetições em segundos.

## Grafo Gerador
![Variação mediana(Gerador)](imagens/Variação%20mediana%20x%20Tamanho%20de%20grafo%20(Gerador).png)

## Grafo Vazio
![Variação mediana (Vazia)](imagens/Variação%20mediana%20x%20Tamanho%20de%20grafo%20(Vazia).png)

## Grafo Acíclico Direcionado (DAG)
![Variação mediana (Acíclico Direcionado)](imagens/Variação%20mediana%20x%20Tamanho%20de%20grafo%20(Acíclico%20direcionado).png)

## Grafo Completo
![Variação mediana (Completo)](imagens/Variação%20mediana%20x%20Tamanho%20de%20grafo%20(Completo).png)

Podemos observar que nos grafos vazio e gerador, o heap binário se apresenta como o mais eficiente, possuindo os menores tempos de execução e uma variação muito pequena. No grafo acíclico direcionado, o heap binomial apresenta os menores tempos medianos, enquanto o fibonacci apresenta o pior desempenho. Por fim, no grafo completo, os heaps binomial e fibonacci conseguem superar a eficiência do binário no maior tamanho testado (4000 nós), apresentando menores tempos medianos. Além disso, o gráfico de variação do grafo completo revela um pico agudo de instabilidade para o heap binário nesse exato tamanho, contrastando com a estabilidade mantida pelas outras duas estruturas.

Nos grafos vazio e gerador, o heap binário apresentou os menores tempos medianos em todos os tamanhos testados, com a menor dispersão no grafo gerador. No grafo acíclico direcionado, binário e binomial ficaram praticamente empatados, com leve vantagem do binomial em 4000 nós, enquanto o Fibonacci apresentou o pior desempenho em todos os tamanhos. No grafo completo, os três heaps tiveram tempos muito próximos, com o binário ligeiramente mais lento em 1000 e 4000 nós, diferença pequena diante da dispersão. Nesse mesmo grafo, em 4000 nós, o binário apresentou um pico de variação (~0,17 s), contrastando com a dispersão das outras duas estruturas (~0,01 s).



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

3. Como o benchmark roda no ecossistema do Python (interpretado e gerenciado dinamicamente), instantes em que o Garbage Collector entra em ação causam pausas na execução. Isso justifica os picos e anomalias percebidos na "Variação Mediana" em tamanhos de grafos maiores, figurando como uma ameaça à validade de comparar estruturas de dados puras na linguagem Python.
