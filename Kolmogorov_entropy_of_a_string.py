def kolmogorov_entropy(string, distribution):
    """Computes the Kolmogorov entropy of a string."""
    entropy = 0
    for c in string:
        probability = distribution[c]
        entropy += -probability * np.log2(probability)
    return entropy
