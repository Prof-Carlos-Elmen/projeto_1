# CODIGO UNIFICADO
import random  # Importa a biblioteca para geração de números aleatórios
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
if __name__ == "__main__":
    # Criando uma lista unimodal aleatória
    n = 20  # Define o tamanho da lista
    peak_pos = random.randint(1, n - 2)  # Define uma posição aleatória para o pico
    arr = list(range(peak_pos)) + list(range(peak_pos, 0, -1))  # Gera a lista unimodal  
    print("Array unimodal:", arr)  # Exibe a lista gerada
    print("Pico encontrado (Sequencial):", find_peak_sequential(arr))  # Encontra o pico com o método sequencial
    print("Pico encontrado (Busca Binária):", find_peak_binary(arr))  # Encontra o pico com busca binária
