#WAP to demonstrate the working of the Decision Tree based ID3 Algorithm. Use an appropriate dataset for building the Decision Tree and apply this knowledge to classify a new sample.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# 1. Dataset: Play Tennis Example
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# 2. Encode categorical variables to numbers
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
for column in df.columns:
    df[column] = le.fit_transform(df[column])

# Separate features and target
X = df.drop('PlayTennis', axis=1)
y = df['PlayTennis']

# 3. Build Decision Tree using ID3 (entropy criterion)
clf = DecisionTreeClassifier(criterion='entropy', random_state=0)
clf.fit(X, y)

# 4. Visualize the tree structure
tree_rules = export_text(clf, feature_names=list(X.columns))
print("Decision Tree Rules:")
print(tree_rules)

# 5. Classify a new sample
# Example new sample: Outlook=Sunny, Temperature=Cool, Humidity=High, Wind=Strong
new_sample = pd.DataFrame({
    'Outlook': ['Sunny'],
    'Temperature': ['Cool'],
    'Humidity': ['High'],
    'Wind': ['Strong']
})

# Encode the new sample
for column in new_sample.columns:
    new_sample[column] = le.fit(df[column]).transform(new_sample[column])

# Predict
prediction = clf.predict(new_sample)
result = le.inverse_transform(prediction)

print("\nNew Sample Classification:")
print(f"Sample: {new_sample.to_dict(orient='records')[0]}")
print(f"PlayTennis: {result[0]}")
