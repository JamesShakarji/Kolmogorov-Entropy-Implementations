use std::f64;

fn kolmogorov_entropy(outcomes: &[f64], probabilities: &[f64]) -> f64 {
    let mut entropy = 0.0;
    for (outcome, probability) in outcomes.iter().zip(probabilities) {
        entropy += -probability * probability.log2();
    }
    entropy
}

// Test the function
let outcomes = [1.0, 2.0, 3.0, 4.0];
let probabilities = [0.25, 0.25, 0.25, 0.25];
println!("{}", kolmogorov_entropy(&outcomes, &probabilities));
