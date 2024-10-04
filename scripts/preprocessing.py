# preprocessing.py

import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
train_data = pd.read_csv('../data/train.csv')

# Handling missing values
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
train_data['Embarked'].fillna(train_data['Embarked'].mode()[0], inplace=True)

# Feature engineering
train_data['Sex'] = train_data['Sex'].map({'male': 0, 'female': 1})
train_data['Embarked'] = train_data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Drop unnecessary columns
train_data.drop(columns=['Name', 'Ticket', 'Cabin'], inplace=True)

# Define features and target
X = train_data.drop(columns=['Survived'])
y = train_data['Survived']

# Split into train and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the processed data (optional)
X_train.to_csv('../data/X_train.csv', index=False)
X_val.to_csv('../data/X_val.csv', index=False)
y_train.to_csv('../data/y_train.csv', index=False)
y_val.to_csv('../data/y_val.csv', index=False)

print("Data preprocessing complete.")
