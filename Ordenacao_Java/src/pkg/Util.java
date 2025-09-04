package pkg;
import java.util.Random;

public class Util {
	public static int[] popularListaAleatoria(int quantidade, int inicio, int fim) {
		Random random = new Random();
		int[] lista = new int[quantidade];

        for (int i = 0; i < quantidade; i++) {
            lista[i] = random.nextInt((fim - inicio) + 1) + inicio; // [inicio, fim]
        }

        return lista;
    }

    // Exibe os elementos da lista com uma frase
    public static void exibirLista(int[] lista, String frase) {
        System.out.println(frase);
        for (int item : lista) {
            System.out.print(item + " ");
        }
        System.out.println(); // quebra de linha no final
    }

}
