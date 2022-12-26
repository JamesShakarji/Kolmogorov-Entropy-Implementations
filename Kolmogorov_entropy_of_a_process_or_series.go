package main

import (
	"fmt"
	"math"
)

func kolmogorovEntropy(outcomes []float64, probabilities []float64) float64 {
	entropy := 0.0
	for i, probability := range probabilities {
		entropy += -probability * math.Log2(probability)
	}
	return entropy
}

func main() {
	// Test the function
	outcomes := []float64{1, 2, 3, 4}
	probabilities := []float64{0.25, 0.25, 0.25, 0.25}
	fmt.Println(kolmogorovEntropy(outcomes, probabilities))
}
