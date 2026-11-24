
def check_eligibility(loan_amount, annual_income, credit_score):

    # Validate annual income
    if annual_income <= 0:
        return False, "Invalid Annual Income"

    # Validate loan amount
    if loan_amount <= 0:
        return False, "Invalid Loan Amount"

    # Validate credit score
    if credit_score < 300 or credit_score > 850:
        return False, "Invalid Credit Score"

    # Calculate loan ratio
    loan_ratio = loan_amount / annual_income

    # Check credit score
    if credit_score < 650:
        return False, "Credit Score is too low."

    # Check loan ratio
    elif loan_ratio > 0.4:
        return False, "Loan amount exceeds allowed limit."

    else:
        return True, "Eligible for the Loan."
