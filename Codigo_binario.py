# CODIGO BINARIO
import random
def find_peak_binary(arr, left=0, right=None):
    """ 
    Encontra um pico em um array unimodal usando busca binária em O(log n).
    - Se `right` for None, define como o último índice do array.
    - Se `left` e `right` forem iguais, significa que encontramos um pico.
    - Caso contrário, divide o array no meio e decide em qual lado continuar a busca.
    """
    if right is None:
        right = len(arr) - 1  # Define o limite direito inicial

    if left == right:
        return left  # Quando os limites se encontram, temos um pico

    mid = (left + right) // 2  # Calcula o meio do intervalo

    # Verifica se devemos continuar a busca na esquerda ou na direita
    if arr[mid] > arr[mid + 1]:  
        return find_peak_binary(arr, left, mid)  # Busca na esquerda
    else:
        return find_peak_binary(arr, mid + 1, right)  # Busca na direita

if __name__ == "__main__":
    # Criando uma lista unimodal aleatória
    n = 20  # Tamanho do vetor
    peak_pos = random.randint(1, n - 2)  # Define a posição do pico

    # Criando um array unimodal crescente até `peak_pos` e decrescente depois
    arr = list(range(peak_pos)) + list(range(peak_pos, 0, -1))

    # Exibe o array e o pico encontrado
    print("Array unimodal:", arr)
    print("Pico encontrado (Busca Binária):", find_peak_binary(arr))
