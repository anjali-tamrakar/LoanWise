
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

    name = request.form['name']
    income = int(request.form['income'])
    loan_amount = int(request.form['loan_amount'])
    credit_score = int(request.form['credit_score'])

    status, message = check_eligibility(
        loan_amount, income, credit_score
    )
    save_application(name, income, loan_amount, credit_score, message)
    return render_temlate('result.htlml ', name=name, income=income, loan_amount=loan_amount, credit_score=credit_score, message=message)
@app.route('/applications')
def view_applications():
    conn = sqlite3.connect("loan.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM applications")
    applications = cursor.fetchall()
    print(applications)
    conn.close()

    return render_template(
        'applications.html',
        applications=applications
    )


if __name__ == '__main__':
    app.run(debug=True)