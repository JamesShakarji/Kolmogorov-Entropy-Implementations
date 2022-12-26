pragma solidity ^0.7.0;

function kolmogorovEntropy(uint[] memory outcomes, uint[] memory probabilities) public pure returns (uint) {
    uint entropy = 0;
    for (uint i = 0; i < outcomes.length; i++) {
        entropy += -probabilities[i] * log2(probabilities[i]);
    }
    return entropy;
}

// Test the function
uint[] memory outcomes = [1, 2, 3, 4];
uint[] memory probabilities = [25, 25, 25, 25];
uint entropy = kolmogorovEntropy(outcomes, probabilities);

// Print the result
print(entropy);
