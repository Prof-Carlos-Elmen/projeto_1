import random  # Importa a biblioteca para geração de números aleatórios
import time  # Importa a biblioteca para medir tempo de execução
import numpy as np  # Importa a biblioteca para manipulação numérica
import matplotlib.pyplot as plt  # Importa biblioteca para geração de gráficos

def generate_unimodal_list(n):
    """Gera uma lista unimodal aleatória com tamanho n"""
    peak_pos = random.randint(1, n - 2)  # Escolhe uma posição aleatória para o pico
    return list(range(peak_pos)) + list(range(peak_pos, 0, -1))  # Cria lista crescente e depois decrescente

def find_peak_sequential(arr):
    """Encontra o primeiro pico em O(n)"""
    n = len(arr)
    for i in range(1, n - 1):  # Percorre a lista do segundo ao penúltimo elemento
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:  # Verifica a condição de pico
            return i  # Retorna o índice do primeiro pico encontrado
    return -1  # Retorna -1 caso não encontre um pico (não esperado para listas unimodais)

def find_peak_binary(arr, left=0, right=None):
    """Encontra um pico usando busca binária em O(log n)"""
    if right is None:
        right = len(arr) - 1  # Define o limite direito caso não tenha sido passado
    if left == right:  # Caso base: quando a busca se reduz a um único elemento
        return left  # Retorna o índice do pico encontrado
    mid = (left + right) // 2  # Encontra o ponto médio do intervalo
    if arr[mid] > arr[mid + 1]:  # Se o elemento do meio for maior que o próximo
        return find_peak_binary(arr, left, mid)  # Procura na metade esquerda
    else:
        return find_peak_binary(arr, mid + 1, right)  # Procura na metade direita

def measure_execution_time(func, arr):
    """Mede o tempo de execução de um algoritmo"""
    start_time = time.time()  # Marca o tempo inicial
    func(arr)  # Executa a função com a entrada fornecida
    return (time.time() - start_time) * 1000  # Retorna o tempo em milissegundos

if __name__ == "__main__":
    # Gerando k tamanhos de entrada entre 10 e 10.000
    k = random.randint(100, 200)  # Define aleatoriamente quantos tamanhos de entrada testar
    sizes = np.linspace(10, 10000, k, dtype=int)  # Gera k valores espaçados entre 10 e 10.000

    # Escolhendo m, número de execuções por tamanho de entrada
    m = random.randint(10, 20)  # Define aleatoriamente quantas execuções para cada tamanho de entrada

    results_sequential = []  # Lista para armazenar tempos médios da busca sequencial
    results_binary = []  # Lista para armazenar tempos médios da busca binária

    for n in sizes:
        test_cases = [generate_unimodal_list(n) for _ in range(m)]  # Gera m listas unimodais para o tamanho n
        seq_times = [measure_execution_time(find_peak_sequential, arr) for arr in test_cases]  # Mede tempo sequencial
        bin_times = [measure_execution_time(find_peak_binary, arr) for arr in test_cases]  # Mede tempo binário

        results_sequential.append((n, np.mean(seq_times)))  # Salva média dos tempos sequenciais
        results_binary.append((n, np.mean(bin_times)))  # Salva média dos tempos binários

    print(f"Gerados {k} tamanhos de entrada e {m} conjuntos de teste para cada um.")  # Exibe resumo da geração de dados
    print("Medições de tempo concluídas.")  # Indica o fim do processo

    # Gerando gráfico comparativo entre busca sequencial e busca binária
    seq_sizes, seq_times = zip(*results_sequential)  # Separa tamanhos e tempos da busca sequencial
    bin_sizes, bin_times = zip(*results_binary)  # Separa tamanhos e tempos da busca binária

    plt.figure(figsize=(10, 6))  # Define o tamanho da figura
    plt.plot(seq_sizes, seq_times, label="Busca Sequencial (O(n))", color='blue')  # Plota os tempos da busca sequencial
    plt.plot(bin_sizes, bin_times, label="Busca Binária (O(log n))", color='red')  # Plota os tempos da busca binária

    plt.xlabel("Tamanho da Entrada (n)")  # Define o rótulo do eixo X
    plt.ylabel("Tempo Médio de Execução (ms)")  # Define o rótulo do eixo Y
    plt.title("Comparação de Tempo de Execução: Busca Sequencial vs. Busca Binária")  # Define o título do gráfico
    plt.legend()  # Exibe a legenda
    plt.grid()  # Adiciona uma grade ao gráfico
    plt.show()  # Exibe o gráfico
