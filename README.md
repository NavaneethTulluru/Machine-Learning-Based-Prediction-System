# Ad Click Prediction Using Logistic Regression

## 📌 Project Overview
This project predicts whether a user will click on an online advertisement using demographic and behavioral data. It uses a Logistic Regression model to classify user behavior and help improve digital marketing strategies.

## 📊 Dataset
The dataset used is `advertising.csv` which contains the following features:
- Age
- Area Income
- Daily Time Spent on Site
- Daily Internet Usage
- Clicked on Ad (target variable)

> **Note:** `advertising.csv` is included in this project folder for local testing. If this file is private, remove it from the repo and add it to `.gitignore`.

## 🛠️ Technologies Used
- Python 3.13
- pandas
- numpy
- scikit-learn

## ⚙️ How It Works
1. The dataset is loaded using pandas.
2. Important features are selected for training.
3. Data is split into training and testing sets (70% train, 30% test).
4. A Logistic Regression model is trained.
5. The model is evaluated using accuracy and classification report.

## ✅ Results
- Accuracy achieved: **93.67%**
- Precision, Recall, and F1-score are around **0.94**

## 🚀 How to Run the Project

1. Install required libraries:
```bash
pip install pandas numpy scikit-learn
