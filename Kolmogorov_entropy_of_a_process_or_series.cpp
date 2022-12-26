#include <iostream>
#include <cmath>

double kolmogorovEntropy(int* outcomes, double* probabilities, int n) {
    double entropy = 0.0;
    for (int i = 0; i < n; i++) {
        entropy += -probabilities[i] * log2(probabilities[i]);
    }
    return entropy;
}

int main() {
    // Test the function
    int outcomes[] = {1, 2, 3, 4};
    double probabilities[] = {0.25, 0.25, 0.25, 0.25};
    std::cout << kolmogorovEntropy(outcomes, probabilities, 4) << std::endl;
    return 0;
}
