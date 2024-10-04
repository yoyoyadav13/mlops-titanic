# train_model.py

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Load the processed data
X_train = pd.read_csv('../data/X_train.csv')
X_val = pd.read_csv('../data/X_val.csv')
y_train = pd.read_csv('../data/y_train.csv').values.ravel()  # Flatten the target array
y_val = pd.read_csv('../data/y_val.csv').values.ravel()

# Initialize the model
model = LogisticRegression(max_iter=200)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the validation set
y_pred = model.predict(X_val)

# Evaluate the model
accuracy = accuracy_score(y_val, y_pred)
print(f"Validation Accuracy: {accuracy:.2f}")

# Save the model
with open('../models/titanic_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model training complete and saved.")
