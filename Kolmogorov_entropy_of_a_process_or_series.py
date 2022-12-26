import math

def kolmogorov_entropy(outcomes, probabilities):
    entropy = 0
    for p in probabilities:
        entropy += -p * math.log2(p)
    return entropy

#summing the negative logarithms of these probabilities
  
# Test the function
outcomes = [1, 2, 3, 4]
probabilities = [0.25, 0.25, 0.25, 0.25]
print(kolmogorov_entropy(outcomes, probabilities))
