package pkg;

public class Ordenacao {
	public static int[] pente(int[] lista) {
        boolean houveTroca = true;
        int qtdComparacoes = 0;
        int qtdTrocas = 0;
        int distancia = lista.length;

        while (houveTroca || distancia > 1) {
            distancia = (int) (distancia / 1.3);
            if (distancia < 1) {
                distancia = 1;
            }
            houveTroca = false;

            for (int i = 0; i < lista.length - distancia; i++) {
                qtdComparacoes++;
                if (lista[i] > lista[i + distancia]) {
                    qtdTrocas++;
                    houveTroca = true;

                    // troca
                    int tmp = lista[i];
                    lista[i] = lista[i + distancia];
                    lista[i + distancia] = tmp;
                }
            }
        }

        return new int[]{qtdComparacoes, qtdTrocas};
    }
}
