#For a given set of training data examples stored in a CSV file, implement and demonstrate the Candidate-Elimination algorithm to output a description of the set of all hypotheses consistent with the training examples.

import pandas as pd

# Load training data from CSV file
data = pd.read_csv('training_data.csv')

# Separate features and target
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Initialize Specific hypothesis and General hypothesis
specific_h = X[0].copy()
general_h = [["?" for _ in range(len(specific_h))] for _ in range(len(specific_h))]

print("Initial specific hypothesis:", specific_h)
print("Initial general hypothesis:", general_h)

# Function to check if two tuples match except for '?'
def consistent(hypothesis, example):
    for h, e in zip(hypothesis, example):
        if h != "?" and h != e:
            return False
    return True

# Candidate-Elimination Algorithm
for i, example in enumerate(X):
    if y[i] == "Yes":  # Positive example
        # Generalize specific hypothesis S
        for j in range(len(specific_h)):
            if specific_h[j] != example[j]:
                specific_h[j] = "?"
                
        # Remove inconsistent general hypotheses
        for g in general_h:
            for j in range(len(g)):
                if g[j] != "?" and g[j] != example[j]:
                    g[j] = "?"
                
    else:  # Negative example
        for j in range(len(specific_h)):
            if specific_h[j] != example[j]:
                continue
            else:
                new_h = specific_h.copy()
                new_h[j] = "?"
                if new_h not in general_h:
                    general_h.append(new_h)
        
        # Remove general hypotheses inconsistent with negative example
        general_h = [g for g in general_h if not consistent(g, example)]
    
    print(f"\nAfter example {i+1} -> {example} with label {y[i]}:")
    print("Specific hypothesis:", specific_h)
    print("General hypothesis set:")
    for g in general_h:
        print(g)

# Final output
print("\nFinal Specific Hypothesis:", specific_h)
print("\nFinal General Hypothesis Set:")
for g in general_h:
    print(g)

