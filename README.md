
# LoanWise – ML-Based Loan Eligibility Prediction System

## Project Overview
LoanWise is a web-based application that predicts loan eligibility using Machine Learning. Users can enter their personal financial details and receive an eligibility prediction.

This project is developed as an academic prototype to demonstrate Machine Learning, Flask, and database integration.

## Features
- Loan eligibility prediction using Machine Learning
- Applicant details submission
- Credit score validation
- Eligible and Not Eligible results
- SQLite database for storing applications
- Application records page
- Prediction explanation

## Technologies Used
- Python
- Flask
- Machine Learning
- Scikit-learn
- Pandas
- NumPy
- SQLite
- HTML
- CSS

## Project Structure
```text
LoanWise/
│
├── app.py
├── database.py
├── predict.py
├── train_model.py
├── loan_model.pkl
├── loan.db
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── applications.html
│
├── static/
│   └── style.css
│
└── README.md
```

## How to Run the Project

### 1. Install Required Libraries
```bash
pip install flask pandas numpy scikit-learn joblib
```

### 2. Train the ML Model
```bash
python train_model.py
```

### 3. Run the Application
```bash
python app.py
```

### 4. Open in Browser
http://127.0.0.1:5000/

## How It Works
1. User enters applicant details.
2. Flask receives the submitted information.
3. The ML model predicts loan eligibility.
4. The result is displayed on the website.
5. Application details are stored in SQLite.
6. Saved applications can be viewed on the applications page.

## Academic Disclaimer
LoanWise is an educational prototype using synthetic training data. It is not a real banking system and does not provide actual loan approval or financial advice.
