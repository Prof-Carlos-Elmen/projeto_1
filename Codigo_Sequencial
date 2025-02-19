# CODIGO SEQUENCIAL
import random
def find_peak_sequential(arr):
    """Encontra o primeiro pico em O(n)"""
    n = len(arr)
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return i
    return -1  # Caso não encontre um pico (não esperado para listas unimodais)
if __name__ == "__main__":
    # Criando uma lista unimodal aleatória
    n = 20
    peak_pos = random.randint(1, n - 2)
    arr = list(range(peak_pos)) + list(range(peak_pos, 0, -1))
    print("Array unimodal:", arr)
    print("Pico encontrado (Sequencial):", find_peak_sequential(arr))
