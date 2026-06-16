import sqlite3
def get_connection():
    return sqlite3.connect("expenses.db")
    
def create_table():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def insert_expense(name,amount,category):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('''INSERT INTO expenses(name,amount,category)
                   VALUES(?,?,?)''',(name,amount,category))
    conn.commit()
    conn.close()

def delete_expense(expense_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('''DELETE FROM expenses
                   WHERE id=? ''',(expense_id,))
    conn.commit()
    conn.close()

def update_expense_(expense_id,name,amount,category):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('''UPDATE expenses
                   SET name=?,amount=?,category=?
                   WHERE id=?''',(name,amount,category,expense_id))
    conn.commit()
    conn.close()

def get_expense_by_id(expense_id):
    conn=get_connection()
    conn.row_factory=sqlite3.Row
    cursor=conn.cursor()
    cursor.execute('''SELECT * FROM expenses
                   WHERE id=?''',(expense_id,))
    expense=cursor.fetchone()
    conn.close()
    return expense

def filter_in_expense(name=None, category=None, min_amount=None, max_amount=None):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = "SELECT * FROM expenses WHERE 1=1"
    values = []

    if name:
        query += " AND name LIKE ?"
        values.append(f"%{name}%")

    if category:
        query += " AND category = ?"
        values.append(category)

    if min_amount:
        query += " AND amount >= ?"
        values.append(float(min_amount))

    if max_amount:
        query += " AND amount <= ?"
        values.append(float(max_amount))

    cursor.execute(query, values)
    expenses = cursor.fetchall()

    conn.close()
    return expenses

def total_expense(name=None,category=None,min_amount=None,max_amount=None):
    conn=get_connection()
    conn.row_factory=sqlite3.Row
    cursor=conn.cursor()
    query="SELECT SUM(amount) AS total, COUNT(*) AS count FROM expenses WHERE 1=1"
    values=[]
    if name:
        query+=" AND name LIKE ?"
        values.append(f"%{name}%")
    if category:
        query+=" AND category = ?"
        values.append(category)
    if min_amount:
        query+=" AND amount >= ?"
        values.append(min_amount)
    if max_amount:
        query+=" AND amount <= ?"
        values.append(max_amount)

    cursor.execute(query,values)
    result=cursor.fetchone()

    conn.close()
    return result

def total_summary(name=None,category=None,min_amount=None,max_amount=None):
    conn=get_connection()
    conn.row_factory=sqlite3.Row
    cursor=conn.cursor()
    qurey="SELECT category, SUM(amount) AS total , COUNT (category) AS count FROM expenses WHERE 1=1"
    values=[]
    if name:
        qurey+=" AND name LIKE ?"
        values.append(f"%{name}%")
    
    if category:
        qurey+=" AND category = ?"
        values.append(category)

    if min_amount:
        qurey+=" AND amount >= ?"
        values.append(min_amount)

    if max_amount:
        qurey+=" AND amount <= ?"
        values.append(max_amount)

    qurey+=" GROUP BY category"

    cursor.execute(qurey,values)
    result=cursor.fetchall()
    
    conn.close()
    return result