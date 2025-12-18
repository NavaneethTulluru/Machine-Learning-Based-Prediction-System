
import pandas as pd  # This is required to use pd.read_csv

# Load the CSV file
df = pd.read_csv("advertising.csv")

# Display the first 5 rows
print(df.head())

# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
df = pd.read_csv("advertising.csv")

# Display first 5 rows to check the data
print("First 5 rows of the dataset:")
print(df.head())

# Example: prepare features and target (adjust column names if needed)
X = df[['Age', 'Area Income', 'Daily Time Spent on Site']]  # features
y = df['Clicked on Ad']  # target column (change if different)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
