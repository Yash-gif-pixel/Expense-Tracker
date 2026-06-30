import sqlite3
connection=sqlite3.connect("expenses.db")
cursor=connection.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
     category TEXT,
      amount INTEGER 
    )
      
    """)
connection.commit()
connection.close()

def save_expense(category,amount):
    connection= sqlite3.connect("expenses.db")
    cursor=connection.cursor()
    cursor.execute(
        """INSERT INTO expenses
        (category,amount)
        VALUES(?,?)""",
        (category,amount)
    )   
    connection.commit()
    connection.close()

def get_all_expenses():
    connection=sqlite3.connect("expenses.db")
    cursor=connection.cursor()
    cursor.execute(
        """SELECT * FROM expenses"""
    )
    rows=cursor.fetchall()
    connection.close()
    return rows