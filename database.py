
import sqlite3

def create_table():
    conn = sqlite3.connect("loan.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            income INTEGER NOT NULL,
            loan_amount INTEGER NOT NULL,
            credit_score INTEGER NOT NULL,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_application(name, income, loan_amount, credit_score, status):
    conn = sqlite3.connect("loan.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO applications
        (name, income, loan_amount, credit_score, status)
        VALUES (?, ?, ?, ?, ?)
    """, (name, income, loan_amount, credit_score, status))

    conn.commit()
    conn.close()
    KeyboardInterrupt