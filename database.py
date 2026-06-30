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

def delete_expense(id):
    connection=sqlite3.connect("expenses.db")
    cursor=connection.cursor()
    cursor.execute(
        """DELETE FROM expenses
        WHERE ID = ? 
        """,
        (id,)
    )
    connection.commit()
    connection.close()

def delete_expense(id):
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM expenses
        WHERE id = ?
        """,
        (id,)
    )

    connection.commit()
    connection.close()

def update_expense(id, category, amount):
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE expenses
        SET category = ?, amount = ?
        WHERE id = ?
        """,
        (category, amount, id)
    )

    connection.commit()
    connection.close()

def get_total_expense():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT SUM(amount)
        FROM expenses
        """
    )

    total = cursor.fetchone()[0]

    connection.close()

    return total if total is not None else 0

def get_category_totals():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
        """
    )

    rows = cursor.fetchall()

    connection.close()

    return rows
    