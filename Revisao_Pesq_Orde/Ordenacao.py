class Ordenacao:
    # Método para verificar se a lista está ordenada
    @staticmethod
    def esta_ordenada(lista):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                return False
        return True

    # Bubble Sort (Bolha) com contagem
    @staticmethod
    def bolha_sort(lista):
        arr = lista[:]
        n = len(arr)
        comparacoes = 0
        trocas = 0
        for i in range(n-1):
            for j in range(n-1-i):
                comparacoes += 1
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    trocas += 1
        return arr, comparacoes, trocas

    # Comb Sort (Pente) com contagem
    @staticmethod
    def pente_sort(lista):
        arr = lista[:]
        n = len(arr)
        gap = n
        shrink = 1.3
        comparacoes = 0
        trocas = 0
        sorted = False

        while not sorted:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted = True
            i = 0
            while i + gap < n:
                comparacoes += 1
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    trocas += 1
                    sorted = False
                i += 1
        return arr, comparacoes, trocas

    # Selection Sort (Seleção) com contagem
    @staticmethod
    def selecao_sort(lista):
        arr = lista[:]
        n = len(arr)
        comparacoes = 0
        trocas = 0
        for i in range(n-1):
            min_idx = i
            for j in range(i+1, n):
                comparacoes += 1
                if arr[j] < arr[min_idx]:
                    min_idx = j
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                trocas += 1
        return arr, comparacoes, trocas


# ==============================
# Classe Principal para rodar os testes
class Principal:
    @staticmethod
    def main():
        valores = [30, 90, 10, 20, 80, 10, 20, 40, 10]

        print("Lista original:", valores)
        print("Está ordenada?:", Ordenacao.esta_ordenada(valores))

        resultado_bolha = Ordenacao.bolha_sort(valores)
        resultado_pente = Ordenacao.pente_sort(valores)
        resultado_selecao = Ordenacao.selecao_sort(valores)

        print("\nBolha -> Ordenado:", resultado_bolha[0], "Comparações:", resultado_bolha[1], "Trocas:", resultado_bolha[2])
        print("Pente -> Ordenado:", resultado_pente[0], "Comparações:", resultado_pente[1], "Trocas:", resultado_pente[2])
        print("Seleção -> Ordenado:", resultado_selecao[0], "Comparações:", resultado_selecao[1], "Trocas:", resultado_selecao[2])


# Executa o programa principal
if __name__ == "__main__":
    Principal.main()
