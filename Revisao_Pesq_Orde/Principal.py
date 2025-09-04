from Ordenacao import Ordenacao
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