import java.lang.Math;

public class KolmogorovEntropy {
    public static double kolmogorovEntropy(int[] outcomes, double[] probabilities) {
        double entropy = 0.0;
        for (int i = 0; i < outcomes.length; i++) {
            entropy += -probabilities[i] * Math.log(probabilities[i]) / Math.log(2);
        }
        return entropy;
    }

    public static void main(String[] args) {
        // Test the function
        int[] outcomes = {1, 2, 3, 4};
        double[] probabilities = {0.25, 0.25, 0.25, 0.25};
        System.out.println(kolmogorovEntropy(outcomes, probabilities));
    }
}
