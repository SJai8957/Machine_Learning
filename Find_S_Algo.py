#Implement and demonstrate the FIND-S algorithm for finding the most specific hypothesis based on a given set of training data samples. Read the training data from a CSV file.

import csv

def load_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # skip header
        data = [row for row in reader]
    return headers, data

def find_s_algorithm(data, target_attr_index):
    # Initialize the most specific hypothesis with the first positive example
    for row in data:
        if row[target_attr_index] == 'Yes':
            hypothesis = row[:-1]  # Exclude the target attribute
            break

    print("Initial hypothesis:", hypothesis)

    # Iterate over all examples
    for row in data:
        if row[target_attr_index] == 'Yes':
            for i in range(len(hypothesis)):
                if hypothesis[i] != row[i]:
                    hypothesis[i] = '?'
            print("Updated hypothesis:", hypothesis)

    return hypothesis

def main():
    filename = 'training_data.csv'
    headers, data = load_csv(filename)
    target_attr = 'EnjoySport'
    target_attr_index = headers.index(target_attr)

    final_hypothesis = find_s_algorithm(data, target_attr_index)

    print("\nFinal Most Specific Hypothesis:")
    print(final_hypothesis)

if __name__ == "__main__":
    main()
