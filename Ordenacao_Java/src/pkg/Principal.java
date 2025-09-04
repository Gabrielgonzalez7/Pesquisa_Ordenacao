package pkg;

public class Principal {
	public static void main(String[] args) {
        // Gerar lista aleatória
        int[] lista = Util.popularListaAleatoria(10, 1, 100);

        // Exibir lista antes da ordenação
        Util.exibirLista(lista, "Lista gerada aleatoriamente:");

        // medir tempo de execução
        long tempoInicio = System.nanoTime();
        int[] resultados = Ordenacao.pente(lista);
        long tempoFim = System.nanoTime();

        double tempoSegundos = (tempoFim - tempoInicio) / 1_000_000_000.0;

        // Exibir resultados
        Util.exibirLista(lista, "Lista ordenada (pente):");
        System.out.println("Tempo da rotina ordenar por pente: " + tempoSegundos + " s");
        System.out.println("Comparações: " + resultados[0]);
        System.out.println("Trocas: " + resultados[1]);
    }
}
