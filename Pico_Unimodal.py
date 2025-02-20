import numpy as np  # Biblioteca para manipulação de arrays e geração de números aleatórios
import time  # Biblioteca para medir tempo de execução
import matplotlib.pyplot as plt  # Biblioteca para geração de gráficos

# Função para gerar um vetor unimodal aleatório
def generate_unimodal_array(n):
    """Gera um vetor unimodal aleatório com valores entre -2n e 2n, garantindo um pico distinto."""
    peak_index = np.random.randint(1, n - 1)  # Escolhe aleatoriamente um índice de pico dentro da faixa
    left_side = np.sort(np.random.randint(-2*n, 2*n - 1, peak_index))  # Gera e ordena a parte crescente
    peak_value = np.random.randint(left_side[-1] + 1, 2*n)  # Garante um valor de pico maior que a parte crescente
    right_side = np.sort(np.random.randint(-2*n, peak_value, n - peak_index - 1))[::-1]  # Gera e ordena a parte decrescente
    return np.concatenate((left_side, [peak_value], right_side))  # Junta as três partes para formar o array unimodal

# Algoritmo O(n) para encontrar o pico
def sequential_peak_index(arr):
    """Encontra o índice do pico percorrendo o array sequencialmente."""
    n = len(arr)
    if n == 1 or arr[0] >= arr[1]:  # Verifica se o primeiro elemento é o pico
        return 0
    if arr[n - 1] >= arr[n - 2]:  # Verifica se o último elemento é o pico
        return n - 1
    for i in range(1, n - 1):  # Percorre o array do segundo ao penúltimo elemento
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:  # Verifica se o elemento atual é um pico
            return i
    return -1  # Caso nunca ocorra (não deveria acontecer)

# Algoritmo O(log n) para encontrar o pico
def binary_search_peak_index(arr):
    """Encontra o índice do pico usando busca binária."""
    left, right = 0, len(arr) - 1  # Define os limites da busca
    while left < right:
        mid = (left + right) // 2  # Calcula o meio do intervalo
        if arr[mid] > arr[mid + 1]:  # Se o meio é maior que o próximo, o pico está à esquerda
            right = mid  # Move o limite direito
        else:  # Caso contrário, o pico está à direita
            left = mid + 1  # Move o limite esquerdo
    return left  # Retorna o índice do pico encontrado

# Configuração do experimento
np.random.seed(42)  # Define a semente para reprodutibilidade
k = np.random.randint(100, 201)  # Escolhe aleatoriamente um número de tamanhos entre 100 e 200
sizes = np.linspace(10, 10000, k, dtype=int)  # Gera k tamanhos igualmente espaçados entre 10 e 10.000
m = np.random.randint(10, 21)  # Escolhe aleatoriamente um número de repetições entre 10 e 20

seq_times, bin_times = [], []  # Listas para armazenar os tempos médios de execução

# Executa os testes para cada tamanho de entrada
for n in sizes:
    total_seq_time = 0  # Acumulador para tempo do algoritmo sequencial
    total_bin_time = 0  # Acumulador para tempo do algoritmo binário
    
    for _ in range(m):
        arr = generate_unimodal_array(n)  # Gera um array unimodal aleatório
        
        # Mede o tempo do algoritmo sequencial
        start = time.time()
        seq_result = sequential_peak_index(arr)
        total_seq_time += time.time() - start
        
        # Mede o tempo do algoritmo de busca binária
        start = time.time()
        bin_result = binary_search_peak_index(arr)
        total_bin_time += time.time() - start
        
           
    # Calcula o tempo médio de execução para cada algoritmo
    seq_times.append(total_seq_time / m)
    bin_times.append(total_bin_time / m)

# Gráfico comparativo dos tempos de execução
plt.figure(figsize=(12, 8))  # Define o tamanho da figura
plt.plot(sizes, seq_times, label="Sequencial O(n)", color="r")  # Plota os tempos sequenciais
plt.plot(sizes, bin_times, label="Busca Binária O(log n)", color="b")  # Plota os tempos binários
plt.xlabel("Tamanho da Entrada", fontsize=14)  # Rótulo do eixo X
plt.ylabel("Tempo Médio de Execução (s)", fontsize=14)  # Rótulo do eixo Y
plt.legend(fontsize=12)  # Adiciona legenda
plt.title("Comparação de Algoritmos para Encontrar Índice do Pico", fontsize=16)  # Título do gráfico
plt.grid(True, linestyle="--", alpha=0.60)  # Adiciona uma grade ao gráfico
plt.xticks(fontsize=12)  # Ajusta tamanho da fonte do eixo X
plt.yticks(fontsize=12)  # Ajusta tamanho da fonte do eixo Y
plt.show()  # Exibe o gráfico

