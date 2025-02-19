

Equipe: Ana Carmélia e Carlos Elmen
Disciplina: Projeto e Análise de Algoritmos
Professor: Thiago Alves Rocha

# projeto_1
Neste projeto você vai comparar experimentalmente dois algoritmos. Na comparação, você vai apresentar um gráfico no qual o eixo horizontal representa o tamanho da entrada e o eixo vertical representa o tempo de execução. Além disso, você deve comparar as respostas dos dois algoritmos em cada entrada, para ter mais garantia que ambos estão implementados corretamente.

Seu código deve escolher tamanhos de entrada de forma que cada tamanho n seja tal que 10 ≤ n ≤ 10.000. Além disso, os tamanhos de entrada escolhidos devem ser aproximadamente igualmente espaçados. A quantidade k de tamanhos de entrada deve ser escolhida aleatoriamente com 100 <= k <= 200.
Para o tempo de execução de cada tamanho de entrada n, você deve executar os algoritmos com m entradas de tamanho n de forma que m é escolhido aleatoriamente com 10 ≤ m ≤ 20. O m escolhido aleatoriamente deve ser o mesmo para todos os tamanhos de entrada. Note que, para uma comparação mais justa, todos os algoritmos devem ser executados com o mesmo conjunto de entradas. 

Além disso, cada entrada também deve ser criada aleatoriamente. Por exemplo, se a entrada do seu problema é um vetor A de tamanho n com elementos do tipo inteiro, você pode criar a entrada de forma que cada A[i] seja escolhido com −2n ≤ A[i] ≤ 2n.


Índice do Pico de uma distribuição Unimodal 
1- Percorre a lista sequencialmente, verificando para cada índice i se ele satisfaz a condição de pico. Retorna o primeiro índice que atende à definição. Este algoritmo possui tempo O(n).
2- Um algoritmo baseado em busca binária com tempo O(lg n).
