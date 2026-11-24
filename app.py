
from flask import Flask, render_template, request
from predict import check_eligibility
from database import create_table, save_application
import sqlite3

app = Flask(__name__)

create_table()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():

    try:
        name = request.form['name'].strip()
        income = int(request.form['income'])
        loan_amount = int(request.form['loan_amount'])
        credit_score = int(request.form['credit_score'])

        if not name:
            return "Name is required"

        status, message = check_eligibility(
            loan_amount,
            income,
            credit_score
        )

        # Save application in database
        save_application(
            name,
            income,
            loan_amount,
            credit_score,
            message
        )

        return render_template(
            'result.html',
            name=name,
            income=income,
            loan_amount=loan_amount,
            credit_score=credit_score,
            message=message
        )

    except ValueError:
        return "Please enter valid numeric values."


@app.route('/applications')
def view_applications():

    conn = sqlite3.connect("loan.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM applications ORDER BY id DESC")
    applications = cursor.fetchall()

    conn.close()

    return render_template(
        'applications.html',
        applications=applications
    )


if __name__ == '__main__':
    app.run(debug=True)
