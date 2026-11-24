
import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Generate synthetic educational dataset
np.random.seed(42)

total_records = 1000

income = np.random.randint(150000, 1500000, total_records)
loan_amount = np.random.randint(50000, 800000, total_records)
credit_score = np.random.randint(300, 851, total_records)

loan_ratio = loan_amount / income

# Educational eligibility labels
eligible = (
    (credit_score >= 650) &
    (loan_ratio <= 0.40)
).astype(int)

df = pd.DataFrame({
    "income": income,
    "loan_amount": loan_amount,
    "credit_score": credit_score,
    "loan_ratio": loan_ratio,
    "eligible": eligible
})

X = df[["income", "loan_amount", "credit_score", "loan_ratio"]]
y = df["eligible"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Model Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))

joblib.dump(model, "loan_model.pkl")

print("Improved ML model trained successfully!")
