
import joblib
import pandas as pd

model = joblib.load("loan_model.pkl")

def check_eligibility(loan_amount, annual_income, credit_score):

    if annual_income <= 0:
        return False, "Invalid Annual Income"

    if loan_amount <= 0:
        return False, "Invalid Loan Amount"

    if credit_score < 300 or credit_score > 850:
        return False, "Invalid Credit Score"

    loan_ratio = loan_amount / annual_income

    input_data = pd.DataFrame(
        [[annual_income, loan_amount, credit_score, loan_ratio]],
        columns=[
            "income",
            "loan_amount",
            "credit_score",
            "loan_ratio"
        ]
    )

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        return True, "Eligible for the Loan (ML Prediction)."

    return False, "Not Eligible for the Loan (ML Prediction)."
